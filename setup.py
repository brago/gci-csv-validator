from setuptools import setup

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="gci-validator",
    version="0.0.3",
    url="https://github.com/arthelon/gci-csv-validator",
    long_description=readme(),
    description="CSV validator for the Google Code-in web API",
    author="Daniel Hsing",
    author_email="hsing.daniel@gmail.com",
    license="MIT",
    scripts=["bin/gci-validator"],
    install_requires=[
        "docopt"
    ]
)
