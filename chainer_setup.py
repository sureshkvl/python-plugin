from setuptools import setup, find_packages
install_requires = ['stevedore']

setup(
    name='chainer',
    version='0.1',
    description='workflow arch written in plugin model',
    author='Suresh Kumar',
    author_email='sureshkumarr.s@gmail.com',
    url='https://github.com/sureshkvl/chainer',
    classifiers=[],
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'myextensions': [
            'complex = myext.complex:Complex',
            'complex2 = myext.complex:Complex2',
            'complex3 = myext.complex:Complex3',
            'complex4 = myext.complex:Complex4',
            ],
        },
    keywords='chainer',
    scripts=[],
    license="Apache",
    )
    
