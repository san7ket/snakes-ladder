#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
setup(
    name="snakes_ladder",
    use_scm_version=True,
    description="",
    long_description="snake ladder",
    author="sjagtap",
    author_email="abc@redhat.com",
    packages=find_packages(),
    package_dir={"snakes_ladder": "snakes_ladder"},
    include_package_data=True,
    install_requires=[
        "pytest",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)