import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1.0, 2.0, 3.0, 7.6, 3.4, 8.2, 6.2, 9.2, 7.1, 5.4])           #(size in 1000 square feet)
y_train = np.array([300.0, 500.0, 700.0, 1000.0, 500.0, 1200.0, 800.0, 1300.0, 900.0, 600.0])           #(price in 1000s of dollars)

def compute_cost(x,y,w,b):
    m = x.shape[0];
    J_wb = 0;
    for i in range(m):
        f_wb = w * x[i] + b;
        J_wb += (f_wb - y[i])**2;
    J_wb = 1/(2*m) * J_wb;
    return J_wb;

w = 100
b = 0

print(f"compute_cost: {compute_cost(x_train,y_train,w,b)}");





