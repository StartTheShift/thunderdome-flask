import sys
from setuptools import setup, find_packages

#next time:
#python setup.py register
#python setup.py sdist upload

version = open('thunderdome_flask/VERSION', 'r').readline().strip()

long_desc = """
Extension for thunderdome that helps integrate it with Flask.
"""

setup(
    name='thunderdome-flask',
    version=version,
    description='Thunderdome Flask integration',
    dependency_links=['https://github.com/etscrivner/thunderdome-flask/archive/{0}.tar.gz#egg=thunderdome-flask-{0}'.format(version)],
    long_description=long_desc,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='cassandra,titan,ogm,thunderdome',
    author='etscrivner',
    author_email='zenogais@gmail.com',
    url='https://github.com/etscrivner/thunderdome-flask',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
)
