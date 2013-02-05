#!/usr/bin/env python

from distutils.core import setup, Extension

DISTUTILS_DEBUG=True

setup(name='spi',
	version='1.0',
	description='Python module for communicating with an SPI device.',
	author='Thomas Preston',
	author_email='thomasmarkpreston@gmail.com',
	license='GPLv3',
	url='http://pi.cs.man.ac.uk/interface.htm',
	ext_modules=[Extension('spi', ['spi.c'])],
)