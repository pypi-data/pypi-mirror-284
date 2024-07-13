import os
import codecs
from setuptools import setup, find_packages

try:
    readme = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(readme, 'ReadMe.md'), encoding="utf-8") as rd:
        long_description = rd.read()
except:
    pass

VERSION = '0.2.5'
DESCRIPTION = 'some functions for list（￣︶￣）↗　'
setup(
    name="PyListFunctions",
    version=VERSION,
    author="BL_30G",
    author_email="2842621898@qq.com",
    url="https://space.bilibili.com/1654383134",
    description=DESCRIPTION,
    long_description=str("""
There are some functions in this project for python list.
You can give some advice for me to improve this project.
My Bilibili:https://space.bilibili.com/1654383134
制作者：BL_30G
版权归属：BL_30G
安装要求：无任何依赖库
Python版本：3.9及以上
Version: 1.0
使用方法：from listFunctions import *
更新日志：
0.1：原始函数(暂且只有一个<(＿　＿)> )：tidy_up_list()
tidy_up_list特性(bug)：会将list内的str(float)自动转换成float
比如：str('3.1415926536')会转变成float(3.1415926536)
0.2：添加函数:deeply_tidy_up_list()和bubble_sort()
更改tidy_up_list()形参为：list
所有函数已添加自检条件，均可放心使用~
0.2.1：修复安装不了的问题（发癫写的setup.py，总之0.1~0.2的版本都安装不了
0.2.2：修复tidy_up_list()和deeply_tidy_up_list()遇空列表,字典,集合，会报错"ValueError: list.remove(x): X Not in List"的问题
别问我为什么没有以上的版本，原因是之前脑瘫整出来的包不测试直接上传，后面删了工程重新发了一遍（极悲 (包括0.2.3和0.2.4)
"""),
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'list', 'clean', 'functions'],
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14'
    ]
)
