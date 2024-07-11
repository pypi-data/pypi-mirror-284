from setuptools import setup
import setuptools

setup(
    name='knot_tube',
    version='0.2.3.2',
    description='A simple python library',
    author='yjianzhu',
    author_email='yjianzhu@mail.ustc.edu.cn',
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'rmsd',
        #'openbabel',
    ],
)