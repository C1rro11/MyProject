#使用给定的整数n，编写程序以生成包含（i，ixi）的字典，该字典为1到n之间的整数（都包括在内）。然后程序应打印字典。假设向程序提供了以下输入：8 
# 然后，输出应为：{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


def dictionary(n):
    result = {};
    for i in range(1, n + 1):
        result[i] = (i) * (i);
    return result;

print(dictionary(8));
