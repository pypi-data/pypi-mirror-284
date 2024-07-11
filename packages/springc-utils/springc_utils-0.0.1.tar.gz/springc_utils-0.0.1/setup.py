# -*- coding: utf-8 -*-
#############################################
# File Name: setup.py
# Author: SpringC
# Mail: xxxxx@126.com
# Created Time:  2024-07-11
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "springc_utils",      #这里是pip项目发布的名称
    version = "0.0.1",  #版本号，数值大的会优先被pip
    keywords = ("pip", "SpringC"),
    description = "A successful sign for python setup",
    long_description = "A successful sign for python setup",
    license = "MIT Licence",

    url = "https://github.com/SpringCCC/myutils",     #项目相关文件地址，一般是github
    author = "SpringC",
    author_email = "jiqimaohw@gmail.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy"]          #这个项目需要的第三方库
)
