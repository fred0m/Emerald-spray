#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='Emerald-spray',
    version='1.0.0',
    author='fredom',
    author_email='he@fredom.ink',
    url='https://github.com/fred0m/Emerald-spray',
    description=u'方便的将steam商店页面信息解析出来，并保存到本地',
    packages=['EmeraldSpray'],
    install_requires=["requests","BeautifulSoup4"]
)
