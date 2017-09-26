import os
from setuptools import find_packages, setup

VERSION = __import__('css_grid').__version__
NAME = 'django-css-grid'
URL = 'https://github.com/raiderrobert/django-css-grid/'

def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''

install_requires = ['django>=1.8']

setup(
    name=NAME,
    version=VERSION,
    author='Robert Roskam',
    author_email='me@robertroskam.com',
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,  # declarations in MANIFEST.in
    license='MIT',
    url=URL,
    download_url=URL+'/tarball/'+VERSION,
    description="A django app for creating css grids",
    long_description=read_file('README.md'),
    keywords=['pomodoro', 'time management', 'productivity'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False
)
