#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 12:56:35 2017

@author: stepan
"""

import sys, os, pickle
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def get_data():
    (x_train, t_train), (x_test, t_test) =\
        load_mnist(flatten=True, normalize=False)
    return x_test, t_test
    

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def preditct(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    
    return y

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def sigmoid(x):
    return 1/(1+ np.exp(-x))

x, t = get_data()
network = init_network()

accurancy_cnt = 0
for i in range(len(x)):
    y = preditct(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accurancy_cnt += 1
print("Accurancy:" + str(float(accurancy_cnt)/ len(x)))


#img = x[0]
#label = t[0]
#print(label)
#img = img.reshape(28, 28)
#img_show(img)