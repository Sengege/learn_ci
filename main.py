#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘trace_tristan@126.com‘
@file: main
@time: 11/3/18 下午11:51
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello CI!'


@app.route('/home')
def home():
    return '<h1>Home'
