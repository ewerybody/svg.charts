#!/usr/bin/env python
# Generated by jaraco.develop 2.16
# https://pypi.python.org/pypi/jaraco.develop

import io
import sys

import setuptools

with io.open('README.txt', encoding='utf-8') as readme:
	long_description = readme.read()

install_reqs = [
	'cssutils>=0.9.8a3',
	'python-dateutil>=2.0',
	'lxml>=2.0',
	'more_itertools',
	'six',
	'tempora>=1.3',
	'jaraco.itertools',
]

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_sphinx = {'release', 'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx'] + install_reqs if needs_sphinx else []

setup_params = dict(
	name='svg.charts',
	use_scm_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description="Python SVG Charting Library",
	long_description=long_description,
	url="https://bitbucket.org/jaraco/svg.charts",
	packages=setuptools.find_packages(),
	namespace_packages=['svg'],
	include_package_data=True,
	zip_safe=True,
	install_requires=install_reqs,
	setup_requires=[
		'setuptools_scm',
	] + pytest_runner + sphinx,
	tests_require=[
		'pytest',
	],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
