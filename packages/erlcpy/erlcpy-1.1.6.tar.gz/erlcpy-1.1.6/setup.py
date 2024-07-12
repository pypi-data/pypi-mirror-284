from setuptools import setup, find_packages

setup(
    name='erlcpy',
    version='1.1.6',
    packages=find_packages(),
    install_requires=['requests'],
    author='Missile / Arimuon',
    description='The First ERLC Python Wrapper',
    url='https://github.com/Arimuon/ErlcPY',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
