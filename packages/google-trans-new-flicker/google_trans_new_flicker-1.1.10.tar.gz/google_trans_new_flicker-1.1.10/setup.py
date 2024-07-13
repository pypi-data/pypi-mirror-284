#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Flicker
#############################################


from setuptools import setup, find_packages

setup(
    name = "google_trans_new_flicker",
    version = "1.1.10",
    description = "A free and unlimited python tools for google translate api.",
    long_description = "fix v1.1.9: json.decoder.JSONDecodeError: Extra data: line 1 column 300 (char 299)",
    license = "MIT Licence",
    url = "https://github.com/FlickerMi/google_trans_new",
    author = "Flicker",
    author_email = "libmi@foxmail.com",
    packages = find_packages(),
    py_modules=["google_trans_new/constant", "google_trans_new/google_trans_new"]
)