import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate synthetic data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Fit linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict values
X_new = np.array([[0], [2]])
y_pred = model.predict(X_new)

# Plot
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_new, y_pred, color='red', linewidth=2, label='Linear fit')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()