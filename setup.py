#!/usr/bin/env python2

from setuptools import setup, find_packages
import os
from pip.req import parse_requirements


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def requirements(requirements_file='requirements.txt'):
    reqs_from_file = parse_requirements(
        os.path.join(os.path.dirname(__file__), requirements_file),
        session=False
    )
    reqs = []
    for r in reqs_from_file:
        if r.req:
            reqs.append(str(r.req))
        # else:
        #     reqs.append(str(r.link))
    return reqs


def get_private_deps(requirements_file='requirements.txt'):
    reqs = parse_requirements(
        os.path.join(os.path.dirname(__file__), requirements_file),
        session=False
    )
    return [str(r.link) for r in reqs if not r.req]


setup(
    name='dwr932',
    version='1.0',
    description='Wrapper around the D-Link DWR-932 API',
    author='Philipp Schmitt',
    author_email='philipp@schmitt.co',
    url='https://github.com/pschmitt/dwr932-api',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements(),
    dependency_links=get_private_deps()
)
