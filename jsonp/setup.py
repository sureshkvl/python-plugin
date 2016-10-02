from setuptools import setup, find_packages
install_requires = ['stevedore']

setup(
    name='jsonp',
    version='0.1',
    description='workflow arch written in plugin model',
    author='Suresh Kumar',
    author_email='sureshkumarr.s@gmail.com',
    url='https://github.com/sureshkvl/chainer',
    classifiers=[],
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'jsonparser': [
            'simple = ext.jsonp:Parser',
            ],
        },
    keywords='jsonp',
    scripts=[],
    license="Apache",
    )
    
