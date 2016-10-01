from setuptools import setup, find_packages
install_requires = ['stevedore']

setup(
    name='chainer1',
    version='0.1',
    description='workflow arch written in plugin model',
    author='Suresh Kumar',
    author_email='sureshkumarr.s@gmail.com',
    url='https://github.com/sureshkvl/chainer',
    classifiers=[],
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'extensions': [
            'simple = extensions.simple:Simple',
            'simple2 = extensions.simple:Simple2',
            'simple3 = extensions.simple:Simple3',
            'simple4 = extensions.simple:Simple4',
            ],
        },
    keywords='chainer',
    scripts=[],
    license="Apache",
    )
    
