import numpy
from time import time
from ase.geometry import get_distances
from ase.data import covalent_radii, atomic_numbers
import itertools

def timeit(f):
    """
        timeit
        Decorator write to stdout
    
        Input
            - f : function
    """
    def f0(*args, **kwargs):
        before = time()
        res = f(*args, **kwargs)
        after = time()
        print('elapsed time ({}) = {:12.4f} [s]'.format(f.__qualname__, after - before))
        return res
    return f0


class HelperFunctions():
    def read_atoms(self):
        '''
            Read the nuclear geometry
        '''
        from ase.io import read
        tmp = read(self.geometry)
        self.atomic_pos = tmp.get_positions()
        self.atomic_sym = tmp.get_chemical_symbols()
        self.atomic_num = tmp.get_atomic_numbers()
        if self.pbc:
            self.cell = tmp.get_cell()
            self.pbc_xyz = [True,True,True]
        else:
            self.cell = None
            self.pbc_xyz = None

    def check(self):
        '''
            Check dicts charge, switch_updn, ecp, and config
             - if atomic type is given -> use inddices instead
             - populate with default values
        '''
        dummy = [dict(),dict(),dict(),dict()]
        for s,sym in enumerate(self.atomic_sym):
            dummy[0][s] = 0
            dummy[1][s] = False
            dummy[2][s] = None
            dummy[3][s] = 'default'

        for t,to_check in enumerate([self.charge,self.switch_updn,self.ecp,self.config]):
            for key,value in to_check.items():
                for val in value:
                    if isinstance(val,str):
                        # must be atomic type -> set all indices of all atoms of this type to the value
                        for s,sym in enumerate(self.atomic_sym):
                            if sym == val:
                                dummy[t][s] = key
                    # Indices are provided explicitely -> just overwrite 
                    elif isinstance(val,int):
                        dummy[t][val] = key

        # Overwrite all dicts()
        self.charge      = dummy[0].copy()
        self.switch_updn = dummy[1].copy()
        self.ecp         = dummy[2].copy()
        self.config      = dummy[3].copy()



    def linear_planar(self):
        '''
            Check which atoms are in a planar or linear environment

              - differentiate bonds and lone linearity/planarity
                - e/g/ SO2: for bonds, need planarity on S; for lone, we do not

             for lone it really only matters if it is planar (CH3)
             for bonds, it matters whether we are in a linear or planar environment
             (CO2,SO2,..)

            Use connectivity matrix and distance matrix from assign_bonds()
        '''
        self.is_linear_planar = {}
        for s,sym in enumerate(self.atomic_sym):
            # now defined in assign_bonds
            ##  tmp = numpy.where(self.con_mat[0][s] != 0)[0].tolist()
            ##  # Add DN bonds, if not already in up channel
            ##  also = [new for new in numpy.where(self.con_mat[1][s] != 0)[0].tolist() if new not in tmp]
            ##  tmp.extend(also)
            ##  self.bond_partners.append(tmp)

            self.is_linear_planar[s] = "neither"
            if len(self.bond_partners[s]) == 0:
                self.is_linear_planar[s] = "neither"

            elif len(self.bond_partners[s]) == 1:
                if len(self.atomic_pos) == 2:
                    # Do this only for diatomics?
                    self.is_linear_planar[s] = "linear4bonds" # only linear for bonds; lones should be outside, not out of axis
            else:
                # take cross products of the vectors; check whether they align
                #self.is_linear_planar[s] = "TODO"
                bonds = []
                for partner in self.bond_partners[s]:
                    # use distance matrix from assign_bonds(): no need to recompute distances here!
                    # normalize it here -> no need to do it later
                    bonds.append(self.dist_vecs[s][partner]/numpy.linalg.norm(self.dist_vecs[s][partner]))
                ## For 2 partners: could be linear -> check whether bonds are aligned
                # could also be planar; SO2 -> check this!!!
                if len(self.bond_partners[s]) == 2:
                    # check angle of bonds; if 0 or 180 -> linear
                    cos_alpha = numpy.dot(bonds[0],bonds[1]) # already normalized, right?
                    if abs(cos_alpha) > 0.98:
                        self.is_linear_planar[s] = "linear4both"
                    # for two bonds, and not linear -> always planar
                    else:
                        self.is_linear_planar[s] = "planar4bonds"
                # For any more bonds: Check planarity
                else:
                    # use itertools to get all cross products between all bonds
                    cross_prods = [numpy.cross(combo[0],combo[1])/numpy.linalg.norm(numpy.cross(combo[0],combo[1])) for combo in list(itertools.combinations(bonds,2))]
                    # Now check all angles of all cross products
                    cos_angles  = [numpy.dot(combo[0],combo[1])                                                     for combo in list(itertools.combinations(cross_prods,2))]
                    # if all cosines of all angles are 1 or -1 (or close to it -> planar
                    check = [abs(cos) > 0.98 for cos in cos_angles]
                    if numpy.all(check): self.is_linear_planar[s] = "planar4both"
                    else:                self.is_linear_planar[s] = "neither"



    def write(self):
        '''
            Write the final xyz/cif file, including the FODs
        '''
        from ase import Atoms
        tmp_pos = self.atomic_pos.tolist()
        tmp_sym = self.atomic_sym.copy()
        for a,atm in enumerate(self.fods):
            for f,shell in enumerate(atm[0]):
                new_sym = "X"
                for fodpos in shell:
                    tmp_pos.append(fodpos)
                    tmp_sym.append(new_sym)

        for a,atm in enumerate(self.fods):
            for f,shell in enumerate(atm[1]):
                new_sym = "He"
                for fodpos in shell:
                    tmp_pos.append(fodpos)
                    tmp_sym.append(new_sym)

        
        new_atoms = Atoms(tmp_sym,tmp_pos,cell=self.cell)
        new_atoms.write(f"{self.output}")

    def get_charge_spin_dip(self):
        '''
            Compute charge, spin and point charge dipole based on FODs and atoms

            # Take core charge into account -> with ECPs this could be missleading
        '''
        charge = sum(self.atomic_num)
        spin   = 0
        for a,atm in enumerate(self.fods):
            for f,fod in enumerate(atm):
                for shell in fod:
                    charge -= len(shell)
                    if f == 0: spin += len(shell)
                    else:      spin -= len(shell)
        # point charge dipole
        center_atoms = numpy.sum(self.atomic_pos,axis=0)/len(self.atomic_pos)
        dip = numpy.zeros(3)
        for a,atm in enumerate(self.fods):
            for f,fod in enumerate(atm):
                for shell in fod:
                    for fodpos in shell:
                        dip -= (fodpos - center_atoms)
        return charge, spin, dip




    def rotmat(self,
               axis=[1,1,1],
               angle=0.):
        '''
            Define rotation matrix based on angle and axis,
              can be used by rotmat_around_axis and rotmat_vec1vec2
    
              axis needs to be normalized, angle in radians
        '''
        cos_a = numpy.cos(angle)
        sin_a = numpy.sin(angle)
    
        rotmat = numpy.zeros((3,3))
        rotmat[0,0] = cos_a + axis[0]**2 * (1.0 - cos_a)
        rotmat[0,1] = axis[0]*axis[1] * (1.0 - cos_a) - axis[2]*sin_a
        rotmat[0,2] = axis[0]*axis[2] * (1.0 - cos_a) + axis[1]*sin_a
        rotmat[1,0] = axis[1]*axis[0] * (1.0 - cos_a) + axis[2]*sin_a
        rotmat[1,1] = cos_a + axis[1]**2 * (1.0 - cos_a)
        rotmat[1,2] = axis[1]*axis[2] * (1.0 - cos_a) - axis[0]*sin_a
        rotmat[2,0] = axis[2]*axis[0] * (1.0 - cos_a) - axis[1]*sin_a
        rotmat[2,1] = axis[2]*axis[1] * (1.0 - cos_a) + axis[0]*sin_a
        rotmat[2,2] = cos_a + axis[2]**2 * (1.0 - cos_a)
        return rotmat
    
    def rotmat_around_axis(self,
                           axis=[1,1,1],
                           angle=0):
        '''
            Rotation matrix for axis and angle
              angle in radians
        '''
        # normalized axis
        axis = numpy.array(axis)/numpy.linalg.norm(axis)
    
        rotmat = self.rotmat(axis,angle)
        return rotmat
    
    def rotmat_vec1vec2(self,
                        vec1,
                        vec2):
        '''
            Rotmat for rotating vec1 into vec2
        '''
        tmp1 = vec1/numpy.linalg.norm(vec1)
        tmp2 = vec2/numpy.linalg.norm(vec2)
    
        cos_alpha = numpy.dot(tmp1,tmp2)
        if cos_alpha >  1.0: cos_alpha =  1.0
        if cos_alpha < -1.0: cos_alpha = -1.0
        angle     = numpy.arccos(cos_alpha)
    
        rot_axis = numpy.cross(tmp1,tmp2)
        # no rotation necessary
        # CAREFUL: If cos_alpha = -1 -> invert
        if rot_axis.tolist() == [0.,0.,0.]:
            rotmat = numpy.zeros((3,3))
            rotmat[0][0] = cos_alpha
            rotmat[1][1] = cos_alpha
            rotmat[2][2] = cos_alpha
            return rotmat

        axis     = rot_axis/numpy.linalg.norm(rot_axis)
        rotmat = self.rotmat(axis,angle)
        return rotmat

