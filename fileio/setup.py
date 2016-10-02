from setuptools import setup, find_packages
install_requires = ['stevedore']

setup(
    name='fileio',
    version='0.1',
    description='workflow arch written in plugin model',
    author='Suresh Kumar',
    author_email='sureshkumarr.s@gmail.com',
    url='https://github.com/sureshkvl/chainer',
    classifiers=[],
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'filedrivers': [
            'fileio = driver.fileio:Simple',
            ],
        },
    keywords='fileio',
    scripts=[],
    license="Apache",
    )
    
