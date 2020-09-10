import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class LinearRegression():
    def __init__(self, learning_rate=0.001, batch_size=32, epochs=100):
        # Size of the step we take

        # We will see the dataset in batch-sized chunks 

        # Times we see the entire set of points


    # Calculate the best line
    def fit(self, X, Y):
        # First we set our slope and intercept to random value



        
        for epoch in range(self.epochs):
            loss = 0
            for i in range(0, num_points, self.batch_size):

                # Get the coordinates for the current batch



                # Get the prediction and loss



                # Get the gradient of slope and intercept


                
                # Update our guess for slope and intercept


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


    # Calculate the best slope and intercept for training set


    # Testing Data
    test_df = pd.read_csv("test_data.csv")
    x_test = test_df['x_test'].to_numpy().reshape(-1, 1)
    y_test = test_df['y_test'].to_numpy().reshape(-1, 1)

    # Predict the line going through the testing data
   




if __name__=='__main__':
    main()
