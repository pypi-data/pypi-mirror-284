from setuptools import setup, Extension

setup(name='led_palindrome',
      version='1.0',
      description='A simple example',
      author='liuende',
      ext_modules=[Extension('led_palindrome', ['palindrome.c'])]
      )