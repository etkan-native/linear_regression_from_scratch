#Liner_regression_from_scratch

import numpy as np

X = np.array([1500, 2000, 3000])  # house sizes
y = np.array([80, 100, 140])      # prices in lakhs

weight = 0 
bias = 0 

price = X * weight + bias 

loss = np.mean((price - y) ** 2)

learning_rate = 0.0000000001

for i in range(100000):
    price = X * weight + bias
    loss = np.mean((price - y) ** 2)
    weight = weight + learning_rate * np.mean((y - price) * X )
    bias = bias + learning_rate * np.mean(y - price)
    if i % 10000 == 0:
        print(loss)

print("Weight:", weight)
print("Bias:", bias)
print("Predictions:", X * weight + bias)

