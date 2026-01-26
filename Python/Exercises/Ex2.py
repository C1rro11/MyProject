#编写一个程序，可以计算给定数字的阶乘，结果应以逗号分隔的顺序打印在一行上，假设向程序提
#供了以下输入：8然后，输出应为：40320

def factorial(n):
    if n == 0 or n == 1:
        return 1;
    else:
        return n * factorial(n-1);

print(factorial(8));