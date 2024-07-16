#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages  # 这个包没有的可以pip一下

setup(
    name="pyf_pagination",  # 这里是pip项目发布的名称
    version="0.0.5",  # 版本号，数值大的会优先被pip
    keywords=["pip", "pyf_pagination"],  # 关键字
    description="一个用于 Django REST 框架的自定义分页包",  # 描述
    long_description="一个用于 Django REST 框架的自定义分页包",
    license="MIT Licence",  # 许可证
    url="https://github.com/",  # 项目相关文件地址，一般是github项目地址即可
    author="ycx",  # 作者
    author_email="ycx3030@126.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["djangorestframework"],  # 这个项目依赖的第三方库
)
