# -*- coding: utf-8 -*-
"""
README
"""
import os
from setuptools import setup, find_packages

install_requires = [
    # Frameworks
    "antlr4-python2-runtime",
]


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
    name="netlist-parser",
    version="0.0.0",
    author="USCPOSH",
    author_email="uscposh@ee.usc.edu",
    description="Description",
    long_description=__doc__,
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
    # namespace_packages=["netlist_parser"],
    packages=find_packages(exclude=["netlist_parser.tests"]),
    package_data={"netlist_parser": find_package_data("netlist_parser")},
    exclude_package_data={"netlist_parser": ["tests/*"]},
    zip_safe=False,
    install_requires=install_requires,
    test_suite="netlist_parser.tests"
)
