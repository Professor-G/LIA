# -*- coding: utf-8 -*-
"""
Created on Fri Aug 3 13:30:11 2018

@author: danielgodinez
"""
from setuptools import setup, find_packages, Extension


setup(
    name="MicroLIA",
    version="2.0.1",
    author="Daniel Godines",
    author_email="danielgodinez123@gmail.com",
    description="Machine learning classifier for microlensing",
    license='GPL-3.0',
    url = "https://github.com/Professor-G/MicroLIA",
    classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python :: 3',	   
],
    packages=find_packages('.'),
    install_requires = ['numpy','scikit-learn', 'scikit-optimize', 'astropy','scipy','peakutils',
        'progress', 'matplotlib', 'optuna', 'boruta', 'BorutaShap', 'xgboost', 'scikit-plot',
        'tensorflow', 'pandas', 'dill', 'opencv-python'],
    python_requires='>=3.7,<4',
    include_package_data=True,
    test_suite="nose.collector",
    package_data={
    '': ['Miras_vo.xml'],
},

)
