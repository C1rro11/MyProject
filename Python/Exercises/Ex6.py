import math;
'''
编写一个程序，根据给定的公式计算并打印该值：
Q = [（2 _ C _ D）/ H]的平方根
以下是C和H的固定值：
C为50。H为30。
D是变量，其值应以逗号分隔的顺序输入到您的程序中，例如，让我们假设以下逗号分隔的输
入顺
序被赋予了程序：
'''

C,H = 50,30
def calc(D):
    return math.sqrt((2*C*D)/H)
D = [int(i) for i in input().split(',')]
D = [int(i) for i in D] #转换字符串整数
D = [calc(i) for i in D] # 返回浮点值通过在d每个项目计算方法
D = [round(i) for i in D]# 所有的浮动值是圆形的
D = [str(i) for i in D]
print(",".join(D))
