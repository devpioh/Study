import numpy as np

def Step_function(x):
    return np.array(x > 0, dtype=np.int)

def Sigmoid(x):
    return 1 / (1 + np.exp(-x))

def Relu(x):
    return np.max(0, x);

def IdentityFunc(x):
    return x;

def Softmax(x):
    c = np.max(x)
    exp_x = np.exp(x - c) # overflow safe
    sum_exp_x = np.sum(exp_x)
    return exp_x / sum_exp_x