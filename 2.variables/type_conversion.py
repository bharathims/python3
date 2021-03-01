#!/bin/bash

from platform import python_version

'''
Data type conversion
Author: Bharathi M
Date: 2021-03-01
'''

print('Data Type Conversion - Python', python_version())
print('-----------------------------------', end=3*'\n')


x = 69 
print('X is ', x)
print('Number: ', x )
print('int(x): ', int(x))
print('float(x): ', float(x))
print('complex(x): ', complex(x))
print('str(x): ', str(x))
print('repr(x): ', repr(x))
print('chr(x): ', chr(x))
print('hex(x): ', hex(x))
print('oct(x): ', oct(x), end=3*'\n')


x = 'c'
print('X is ', x)
print('ord(x): ', ord(x))
print('tuple(x): ', tuple(x))
print('list(x): ', list(x))
print('set(x): ', set(x))
print('frozenset(x): ', frozenset(x), end=3*'\n')


x = (('one', 1), ('two', 2))
print('X is ', x)
print('dict(x): ', dict(x))
