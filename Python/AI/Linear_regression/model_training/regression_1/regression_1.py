import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import kagglehub as kgh
import shutil #for moving files
import math


dp_url = 'andonians/random-linear-regression'
path = kgh.dataset_download(dp_url)
target_folder = "./dataset"

if path:
    if not os.path.exists(target_folder):
        for file_name in os.listdir(path):
            source_file = os.path.join(path, file_name)
            target_file = os.path.join(target_folder, file_name)
            shutil.move(source_file, target_file)
            print(f"Moved {file_name} to {target_folder}")
    else:
        print(f"目標資料夾 {target_folder} 已存在！")
else:
    print("資料集下載失敗！")

train_set = pd.read_csv(os.path.join(target_folder, "train.csv"))
test_set = pd.read_csv(os.path.join(target_folder, "test.csv"))

train_set = train_set.dropna(subset=['x', 'y'])
x_train = train_set['x'].to_numpy()
y_train = train_set['y'].to_numpy()

def compute_cost(x,y,w,b):
    m = len(x)
    total_cost = 0
    for i in range(m):
        f_wb = w * x[i] + b
        cost_i = (f_wb - y[i]) ** 2
        total_cost += cost_i
    total_cost = (total_cost / (2*m))
    return total_cost

cost = compute_cost(x_train,y_train, 0, 0)

def compute_gradient(x,y,w,b):
    m = len(x)
    dj_dw = 0
    dj_db = 0
    f_wb = w*x + b
    for i in range(m):
        error_i = f_wb[i] - y[i]
        dj_dw += (error_i)*x[i]
        dj_db += error_i
    dj_dw = (dj_dw/m)
    dj_db = (dj_db/m)
    return dj_dw, dj_db

dj_dw, dj_db = compute_gradient(x_train,y_train, 0, 0)

def gradient_descent(x,y,w,b,*,compute_cost,compute_gradient,alpha,num_iters):
    J_history = [] # cost history
    w_history = []

    for i in range(num_iters):
        dj_dw, dj_db = compute_gradient(x,y,w,b)
        w = w - alpha * dj_dw
        b = b - alpha * dj_db
        if i<100000:
            cost = compute_cost(x,y,w,b)
            J_history.append(cost)
        if i % math.ceil(num_iters/20) == 0:
            w_history.append(w)
            print(f"Iteration {i:4d}: Cost {float(J_history[-1]):8.2f} ")
    return w, b, J_history, w_history


iterations = 20000
alpha = 1e-6
w_init = 0
b_init = 0
w, b, J_history, w_history = gradient_descent(x_train,y_train,w_init,b_init,compute_cost=compute_cost,compute_gradient=compute_gradient,alpha=alpha,num_iters=iterations)

print(f"w, b: {w}, {b}")

predicted = w*x_train + b
plt.plot(x_train, predicted, c = "b")
plt.scatter(x_train,y_train,marker="x",c="r")
plt.xlabel('feature(x)')
plt.ylabel('target(y)')
plt.title("Training Data")
plt.show()

test_set = test_set.dropna(subset=['x', 'y'])
test_x = test_set['x'].to_numpy()
test_y = test_set['y'].to_numpy()

output_test_y = w * test_x +b

print(f"error: {output_test_y-test_y}")

test_error = output_test_y - test_y
mask = test_y != 0
mape = np.mean(np.abs(test_error[mask]) / np.abs(test_y[mask])) * 100
print(f"correctness: {100-mape:.2f}%")

plt.plot(J_history) # plot the cost history
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title("Cost History")
plt.show()