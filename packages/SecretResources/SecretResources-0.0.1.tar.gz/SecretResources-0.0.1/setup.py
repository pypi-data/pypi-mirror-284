#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="SecretResources",  # Required
    version="0.0.1",  # Required
    description="Get config info from platform",  # Optional
    author="lzk",  # Optional
    author_email="1714476383@qq.com",  # Optional
    packages=find_packages(),
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.7, <4",
    install_requires=["requests"],  # Optional
)
