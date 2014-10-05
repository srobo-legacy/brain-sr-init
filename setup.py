#!/usr/bin/env python
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages

setup(
    name = "sr-init",
    version = "0.1",
    scripts=["src/rebooter",
             "src/sr-init"],
)
