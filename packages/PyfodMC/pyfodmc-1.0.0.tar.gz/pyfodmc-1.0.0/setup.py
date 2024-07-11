from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name='PyfodMC',
    version='1.0.0',
    description='Python Fermi-orbital descriptor Monte-Carlo (PyfodMC)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/opensic/pyfodmc',
    author='Kai Trepte',
    author_email='kai.trepte1987@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development'
    ],
    keywords=['Python', 'FLO-SIC', 'FODs'],
    license='APACHE2.0',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'ase',
        'numpy',
    ],
    python_requires='>=3.6'
)
