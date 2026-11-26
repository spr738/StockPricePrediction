"""Starter workflow for exploring Google historical stock-price data."""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the training data
dataset_train = pd.read_csv("Google_Stock_Price_Train.csv")
print("Shape:", dataset_train.shape)
print(dataset_train.head())

# Select the opening-price column
training_set = dataset_train.iloc[:, 1:2].values
print("Training data shape:", training_set.shape)
print(training_set[:5])

# Visualize the training prices
plt.plot(training_set, label="Google Stock Price — Training Set")
plt.xlabel("Time")
plt.ylabel("Google Stock Price")
plt.legend()
plt.show()
