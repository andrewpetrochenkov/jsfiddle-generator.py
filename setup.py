import setuptools

setuptools.setup(
    name='jsfiddle-generator',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
