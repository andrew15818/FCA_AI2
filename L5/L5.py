import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class LinearRegression():
    def __init__(self, learning_rate=0.001, batch_size=32, epochs=100):
        self.learning_rate =  learning_rate # Size of the step we take
        self.batch_size = batch_size
        self.epochs = epochs                    # Times we adjust our predictions

    # Calculate the best line
    def fit(self, X, Y):
        # First we set our slope and intercept to random value
        self.slope = np.random.rand(X.shape[1])
        self.intercept = np.random.rand(1)
        num_points = X.shape[0]
        
        for epoch in range(self.epochs):
            loss = 0
            for i in range(0, num_points, self.batch_size):

                # Get the coordinates for the current batch
                x = X[i: i + self.batch_size]
                y = Y[i: i + self.batch_size]

                # Get the prediction and loss
                y_pred = (x * self.slope) + self.intercept
                loss = y_pred - y

                # Get the gradient of slope and intercept
                slope_gradient = 2 * np.sum(x * loss) / len(x)
                int_gradient = 2 * np.sum(loss)
                
                # Update our guess for slope and intercept
                self.slope = self.slope - self.learning_rate * slope_gradient
                self.intercept = self.intercept - self.learning_rate * int_gradient
        print(f'Our final guess for slope: {self.slope}\tintercept:{self.intercept}')


    # Get the error between guess and actual values
    def error(self, x, y):
        error = np.mean((x - y) ** 2) 
        return error
        
    # Predict the best line according to slope and intercept we found
    def predict(self, x):
        prediction = x * self.slope + self.intercept 
        return prediction

def main():
    # Load Data 
    # Training Data
    train_df = pd.read_csv("train_data.csv")
    x_train = train_df['x_train'].to_numpy().reshape(-1, 1)
    y_train = train_df['y_train'].to_numpy().reshape(-1, 1)

    # Create a model class 
    model = LinearRegression()

    # Calculate the best slope and intercept for training set
    model.fit(x_train, y_train)

    # Testing Data
    test_df = pd.read_csv("test_data.csv")
    x_test = test_df['x_test'].to_numpy().reshape(-1, 1)
    y_test = test_df['y_test'].to_numpy().reshape(-1, 1)

    # Predict the line going through the testing data
    y_pred = model.predict(x_test)
    plt.plot(x_test, y_test, '.')
    plt.title("Testing data")
    plt.plot(x_test, y_pred, '-')
    plt.show()

if __name__=='__main__':
    main()
