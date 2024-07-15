from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

name = 'shellium'
version = '9'
author = 'GooseG4G'
email = 'danilnegusev@inbox.ru'
desc = 'The package provides a wrapper for working with chrome driver.'
url = 'https://github.com/GooseG4G/shellium'
packages = ['shellium']
requires = [
    'selenium',
    'selenium-wire',
    'setuptools',
    'blinker==1.7.0',
    'undetected_chromedriver'
]

setup(
    name=name,
    version=version,
    author=author,
    author_email=email,
    description=desc,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=url,
    packages=packages,
    install_requires=requires
)
