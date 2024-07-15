#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cnspy_rosbag2image',
    version="0.1.1",
    author='Roland Jung',
    author_email='roland.jung@aau.at',    
    description='ROS1 rosbag to image file converter.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aau-cns/cnspy_rosbag2image/',
    project_urls={
        "Bug Tracker": "https://github.com/aau-cns/cnspy_rosbag2image/issues",
    },    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    
    packages=find_packages(exclude=["test_*", "TODO*"]),
    python_requires='>=3.6',
    install_requires=['numpy', 'tqdm', 'pandas', 'argparse', 'PyYAML', 'rospkg', 'opencv-python', 'pycryptodomex', 'pycryptodome', 'gnupg', 'lz4'],
)
