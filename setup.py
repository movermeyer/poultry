import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

dirname = os.path.dirname(__file__)


with open(os.path.join(dirname, 'README.rst')) as f:
    long_description = f.read()
with open(os.path.join(dirname, 'CHANGES.rst')) as f:
    long_description += '\n' + f.read()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = 'tests'
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='poultry',
    version='1.5.0',
    description='A tweet collection manager.',
    long_description=long_description,
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    author='Dmitrijs Milajevs',
    author_email='dimazest@gmail.com',
    url='https://github.com/dimazest/poultry',
    license='MIT license',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'opster',
        'setuptools',
        'requests',
        'requests-oauthlib',
    ],
    entry_points={
        'console_scripts': [
            'poultry = poultry.main:dispatch',
        ],
    },
    cmdclass={'test': PyTest},
    tests_require=[
        'pytest>=2.4.2',
    ],
)
