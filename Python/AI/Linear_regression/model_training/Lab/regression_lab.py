import numpy as np #NumPy, a popular library for scientific computing
import matplotlib.pyplot as plt #Matplotlib, a popular library for plotting data
# plt.style.use('./deeplearning.mplstyle')

#Size (1000 sqft)	Price (1000s of dollars)  There are 2 data in a dataset.
#      1.0	        300
#      2.0	        500

# put feature and target variable into a matrix. 
x_train = np.array([1.0, 2.0]); #input feature
y_train = np.array([300.0, 500.0]); # output variable
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")

# m is the total number of training examples.
print(f"x_train.shape:{x_train.shape}" ) # x_train.shape will return a tuple of the shape of the array.
m = x_train.shape[0] #x_train.shape[0] is the length of the array.
print(f"number of training examples is: {m}")

#You will use (x (𝑖) , y (𝑖) ) to denote the  𝑖𝑡ℎ  training example. 
#Since Python is zero indexed, (x (0) , y (0) ) is (1.0, 300.0) and (x (1) , y (1) ) is (2.0, 500.0).
i = 0
x_i = x_train[i];
y_i = y_train[i];
print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})");

# scatter plot is a function in matplotlib, and it is used to plot data.
plt.scatter(x_train, y_train, marker='o' , c = 'r');
plt.title("Housing Prices");
plt.xlabel('Size (1000 sqft)');
plt.ylabel('Price (1000s of dollars)');
plt.show();


# since the function is f_w,b(x) = wx + b, so we need w and b now.
w = 100;
b = 100;

#now we have all the information, then we can use the function to make a prediction.
#for  𝑥(0) , f_wb = w * x[0] + b
#for  𝑥(1) , f_wb = w * x[1] + b

def comput_model_output(x, w, b):
    m = x.shape[0];
    f_wb = np.zeros(m); # return m numbers of 1-dimentional numpy array to y hat.
    for i in range(m):
        f_wb[i] = w * x[i] + b;
    return f_wb;

tmp_f_wb = comput_model_output(x_train, w, b);

#the plot the regression line.
plt.plot(x_train, tmp_f_wb, c = 'b', label = 'Our Prediction');
#plot the actual data
plt.scatter(x_train, y_train, marker = 'x', c = 'r', label = 'Actual Values');
# the purpose of plotting the actual data and the regression line is the see the diff between our prediction and the actual data.


plt.title("Housing Prices");
plt.xlabel('Size (1000 sqft)');
plt.ylabel('Price (1000s of dollars)');

#legend is the label of the plot.
plt.legend();
plt.show();