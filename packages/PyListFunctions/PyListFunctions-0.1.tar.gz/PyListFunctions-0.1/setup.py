import os
import codecs
from setuptools import setup, find_packages

readme = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(readme, 'ReadMe.md'), encoding="utf-8") as rd:
    long_description = rd.read()

VERSION = '0.1'
DESCRIPTION = 'some functions for list(now only one😶)'
setup(
    name="PyListFunctions",
    version=VERSION,
    author="BL_30G",
    author_email="2842621898@qq.com",
    url="https://space.bilibili.com/1654383134",
    description=DESCRIPTION,
    long_description="There are some functions in this project for python list, even though it's only one function\nYou can give some advice for me to improve this project\nMy Bilibili:https://space.bilibili.com/1654383134",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'list', 'clean'],
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
