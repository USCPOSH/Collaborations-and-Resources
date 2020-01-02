# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

install_requires = [
    "netlist-parser",
    "antlr4-python2-runtime;python_version<\"3\"",
#    "antlr4-python3-runtime;python_version>=\"3\"",
]


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def find_package_data(dirname):
    def find_paths(dirname):
        items = []
        for fname in os.listdir(dirname):
            path = os.path.join(dirname, fname)
            if os.path.isdir(path):
                items += find_paths(path)
            elif not path.endswith(".py") and not path.endswith(".pyc"):
                items.append(path)
        return items

    items = find_paths(dirname)
    return [os.path.relpath(path, dirname) for path in items]


setup(
    name="posh-py",
    version="0.0.0",
    author="USCPOSH",
    author_email="uscposh@ee.usc.edu",
    description="Description",
    long_description=read("README.md"),
    license="Apache2",
    url="https://github.com/USCPOSH/Sanitizer",
    classifiers=[
        "Topic :: Internet :: WWW/HTTP :: Application",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
    ],
    namespace_packages=["posh"],
    scripts=["bin/posh-main"],
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["posh.tests"]),
    package_data={"posh": find_package_data("src/posh")},
    exclude_package_data={"posh": ["tests/*"]},
    zip_safe=False,
    install_requires=install_requires,
    test_suite="posh.tests"  # ,
    # dependency_links=[
    #    "file://../netlist-parser/build#egg=netlist-parser-0.0.0"
    # ]
)
