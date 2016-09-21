from setuptools import setup, find_packages

install_requires = ['stevedore']

setup(
    name='myplugin',
    version='1.0',
    classifiers=[],
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'myplugin = myplugin.main:main'
        ],
        'mydrivers': [
            'driver1 = myplugin.drivers.mydriver:Driver1',
            'driver2 = myplugin.drivers.mydriver:Driver2',
            ],
        },
    keywords='myplugin',
    )
