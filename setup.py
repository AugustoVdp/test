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
    url='https://github.com/AugustoVdp/setuptools_ejercicio.git',
    project_urls = {
        "Bug Tracker": "https://github.com/AugustoVdp/setuptools_ejercicio/issues"
    },
    license='MIT',
    packages=['setuptools_ejercicio'],
    install_requires=['requests'],
)