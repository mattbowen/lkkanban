from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='lkkanban',
    version=version,
    description="",
    long_description="""\
""",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Matt Bowen',
    author_email='None',
    url='https://github.com/mattbowen/lkkanban',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
        'nose',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
    )
