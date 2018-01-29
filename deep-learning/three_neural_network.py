#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:07:53 2017

@author: stepan
"""
import numpy as np

def sigmoid(x):
    return 1/(1+ np.exp(-x))

def identify_function(x):
    return x

def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
    network['W2'] = np.array([[0.1, 0.4],[0.2, 0.5], [0.3, 0.6]])
    network['W3'] = np.array([[0.1, 0.3],[0.2, 0.4]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['b2'] = np.array([0.1, 0.2])
    network['b3'] = np.array([0.1, 0.2])
    
    return network

def forword(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identify_function(a3)
    
    return y


network = init_network()
x = np.array([1.0, 0.5])
y = forword(network, x)
print(y)