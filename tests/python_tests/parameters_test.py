#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from nose.tools import *
from utilities import execution_path

import mapnik

def setup():
    os.chdir(execution_path('.'))

def test_parameter_null():
    p = mapnik.Parameter('key',None)
    eq_(p[0],'key')
    eq_(p[1],None)

def test_parameter_string():
    p = mapnik.Parameter('key','value')
    eq_(p[0],'key')
    eq_(p[1],'value')

def test_parameter_integer():
    p = mapnik.Parameter('int',sys.maxint)
    eq_(p[0],'int')
    eq_(p[1],sys.maxint)

def test_parameter_double():
    p = mapnik.Parameter('double',float(sys.maxint))
    eq_(p[0],'double')
    eq_(p[1],float(sys.maxint))

def test_parameter_boolean():
    p = mapnik.Parameter('boolean',True)
    eq_(p[0],'boolean')
    eq_(p[1],True)
    eq_(bool(p[1]),True)


def test_parameters():
    params = mapnik.Parameters()
    p = mapnik.Parameter('float',1.0777)
    eq_(p[0],'float')
    eq_(p[1],1.0777)

    params.append(p)

    eq_(params[0][0],'float')
    eq_(params[0][1],1.0777)

    eq_(params.get('float'),1.0777)


if __name__ == "__main__":
    setup()
    [eval(run)() for run in dir() if 'test_' in run]
