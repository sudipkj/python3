# This code demonstrates the bias-variance tradeoff using polynomial regression on synthetic data.
# Two hypotheses: Capture Linear relationship of data and non linear relationship of data
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline as mp

np.random.seed(2025) #Sets a random seed for reproducibility.

n_dataset = 30
n_sample = 20
noise_std =0.3
x_plot = np.linspace(0, 1, 100)
def true_function(x):
    return np.sin(2 * np.pi * x) #2*pi is used to create a full sine wave cycl

degrees = [1]

for index, degree in enumerate(degrees):
    predictions= []
    for j in range(n_dataset):
        # print(j, index, degree)
        check = np.random.rand(n_sample)
        x = np.sort(np.random.rand(n_sample))

        y = true_function(x) + np.random.normal(0, noise_std, size=n_sample)   # y = true_function(x) + noise for each data point

        #y = mx + c
        # print('x-> y', x, y)
        # plt.plot(x, y, 'ro', label='Data Points')
        # plt.show()

        #define the model
        model = mp(PolynomialFeatures(degree), LinearRegression())  #This allows linear models to fit nonlinear relationships.

        #Train the model - all data in x aer aer added to new list. ie final is list of list
        model.fit(x[:, np.newaxis], y)


        y_predict = model.predict(x_plot[:, np.newaxis])

        predictions.append(y_predict)

    predictions = np.array(predictions)
    mean_prediction = predictions.mean(axis=0)
    variance = predictions.var(axis=0)

    bais_squared = np.mean((mean_prediction - true_function(x_plot)) ** 2)
    noise = noise_std ** 2
    expected_loss = bais_squared + variance + noise
    print("expected_loss", expected_loss)
    print("bais_squared", bais_squared)
    print("variance", variance)

    for pred in predictions:
        plt.plot(x_plot, pred, color='gray')
    plt.plot(x_plot, true_function(x_plot), 'red', label='True Function')
    plt.plot(x_plot, mean_prediction, 'blue', label='Mean')
    plt.fill_between(x_plot, mean_prediction - np.sqrt(variance), mean_prediction + np.sqrt(variance), color='orange', alpha=0.4, label='Variance')
    plt.title(f'Polynomial Degree: {degree}')
    plt.legend()
    plt.ylim(-1.5, 1.5)
plt.show()
