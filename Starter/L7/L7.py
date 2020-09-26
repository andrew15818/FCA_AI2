import numpy as np
import matplotlib.pyplot as plt
# Activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Need backprop
def sigmoid_deriv(x):
    return sigmoid(x) * (1 - sigmoid(x))

def forward(x, w1, w2, predict=False):
    # Multiply our test info with the input layer



    # Create and add bias





    if predict:
        return z2
    return a1, z1, a2, z2

# Backprop function
def backprop(a2, z0, z1, z2, y):
    delta2 = z2 - y
    Delta2 = np.matmul(z1.T, delta2)
    delta1 = (delta2.dot(w2[1:,:].T)) * sigmoid_deriv(a1)
    Delta1 = np.matmul(z0.T, delta1)

    return delta2, Delta1, Delta2
# First column = bias
X = np.array([[1, 1, 0],
            [1, 0, 1],
            [1, 0, 0],
            [1, 1, 1]])

# Output
y = np.array([[1], [1], [0], [0]])

# Initial weights
w1 = np.random.randn(3, 5)
w2 = np.random.randn(6, 1)

LEARNING_RATE = 0.09

costs = []

epochs = 15000

m = len(X)

#Start training
for i in range(epochs):
    
    # Pass our input through the network


    # Calculate the error with backpropagation


    # Modify our weights



    # Add the costs



    if i % 1000 == 0:
        print(f'iteration: {i} Error: {c}')

print('Training complete.')

print('\nOriginal Input: ')
print(X)
# Make predictions

print('Percentages: ')
print(z3)
print('Predictions: ')
print(np.round(z3))

# Plot the cost
plt.plot(costs)
plt.show
