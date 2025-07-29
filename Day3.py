# Bias Variance tradeoff

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline as mp

np.random.seed(2000)

n_dataset = 30
n_sample = 20
noise_std =0.3
x_plot = np.linspace(0, 1, 100)
print(x_plot)

def true_function(x):
    return np.sin(2 * np.pi * x)

degree = [1]

