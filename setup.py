# coding: utf-8

from setuptools import setup


requires = ["requests>=2.14.2", "pycryptodome>=3.8.2"]


setup(
    name='lineworks',
    version='0.0.5',
    description='It is a package that implements the server API and the Talk Bot API among the LINE WORKS APIs.',
    url='https://pypi.org/project/lineworks',
    author='Rei Suzuki',
    author_email='re1yanwork@gmail.com',
    license='MIT License',
    keywords='LINEWORKS',
    packages=[
        'lineworks',
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)