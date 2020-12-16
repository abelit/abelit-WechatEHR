# -*- encoding: utf-8 -*-
'''
@File    :   setup.py
@Time    :   2020/12/16 13:12:01
@Author  :   Abelit 
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
@Licence :   BSD-3-Clause
@Desc    :   None
'''


import setuptools

with open("requirements.txt", "r") as fh:
   requirements = fh.read().splitlines()

setuptools.setup(
    install_requires=[req for req in requirements if req[:2] != "# "],
)