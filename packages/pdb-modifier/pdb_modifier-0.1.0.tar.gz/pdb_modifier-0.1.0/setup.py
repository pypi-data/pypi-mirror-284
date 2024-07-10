import os
from setuptools import setup, find_packages

setup(
    name='pdb_modifier',
    version='0.1.0',  # Update version as needed
    packages=find_packages(),
    description='A simple package to modify PDB files',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    author='Rustam',
    author_email='rustam2592@gmail.com',
    url='https://github.com/RustamBB/pdb_modifier',  # (Optional) Add a repository link
    install_requires=[],  # Add any dependencies your package has
    classifiers=[
        'Programming Language :: Python :: 3',
        # Add other classifiers as needed (https://pypi.org/classifiers/)
    ],
    entry_points={
        'console_scripts': [
            'modify-pdb = pdb_modifier.modify:modify_pdb', 
        ],
    },
)