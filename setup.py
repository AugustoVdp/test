import setuptools

with open("DESCRIPTION.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='setuptools_ejercicio',
    version='0.1.0',
    author='Augusto Van der Ploeg',
    author_email='vanderploeg.augusto@gmail.com',
    description='Ejercicio de setuptools',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/institutohumai/humai_utils',
    license='MIT',
    packages=['setuptools_ejercicios'],
    install_requires=['requests'],
)