import pathlib
from setuptools import setup, find_packages

try:
    here = pathlib.Path(__file__).parent.resolve()
    long_description = (here / 'README.md').read_text(encoding='utf-8')
except:
    pass

VERSION = '0.2.1'
DESCRIPTION = 'some functions for list'
setup(
    name="PyListFunctions",
    version=VERSION,
    author="BL_30G",
    author_email="2842621898@qq.com",
    url="https://space.bilibili.com/1654383134",
    description=DESCRIPTION,
    long_description="There are some functions in this project for python list.You can give some advice for me to improve this project\nMy Bilibili:https://space.bilibili.com/1654383134",
    packages=find_packages('listFunctions'),
    package_dir={'': '.'},
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
