# This code demonstrates the bias-variance tradeoff using polynomial regression on synthetic data.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline as mp

np.random.seed(2000) #Sets a random seed for reproducibility.

n_dataset = 1
n_sample = 20
noise_std =0.3
x_plot = np.linspace(0, 1, 100)
def true_function(x):
    return np.sin(2 * np.pi * x) #2*pi is used to create a full sine wave cycl

degree = [1]

for index, degree in enumerate(degree):
    predictions= []
    for j in range(n_dataset):
        # print(j, index, degree)
        x = np.sort(np.random.rand(n_sample))
        tf = true_function(x)
        npRandonNormal = np.random.normal(0, noise_std, n_sample)
        y = true_function(x) + np.random.normal(0, noise_std, n_sample)

        #define the model
        model = mp(PolynomialFeatures(degree), LinearRegression())

        #Train the model
        model.fit(x[:, np.newaxis], y)


        y_predict = model.predict(x_plot[:, np.newaxis])

        predictions.append(y_predict)

    predictions = np.array(predictions)
    mean_prediction = predictions.mean(axis=0)
    variance = predictions.var(axis=0)

    for pred in predictions:
        plt.plot(x_plot, pred, color='gray')
    plt.plot(x_plot, true_function(x_plot), 'red', label='True Function')

plt.show()
