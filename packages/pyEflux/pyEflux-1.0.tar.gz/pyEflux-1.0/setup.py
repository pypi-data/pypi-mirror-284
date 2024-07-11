from setuptools import setup, find_packages

setup(
name='pyeflux',
version='1.0',
author='Brunet Theo, Stphen Chapman',
author_email='theo.brunet@univ-amu.fr',
description='Package used to constrain a metabolic model with the Efflux method (constrain based on proteomic or transcriptomic data)',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent'
],
python_requires='>=3.6'
)