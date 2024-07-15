# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='pyfino',
    version='1.0.1',
    description='可以实现节点自动化消息协同的框架',  # 描述信息
    author='xuwh',  # 作者
    author_email='xuwhdev@gmail.com',
    url='http://xuwh.net',
    #packages=['myPackage','myPackage.inner'], # 包名
    packages=find_packages(), # 会递归查找当前目录下的所有包名
)