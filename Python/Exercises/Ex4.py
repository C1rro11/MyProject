#编写一个程序，该程序从控制台接受一个逗号分隔的数字序列，并生成一个列表和一个包含每个数字的元组。假设向该程序提供了以下输入：34,67,55,33,12,98 

def list_and_tuple(str):
    nums = str.split(',');
    tuplelist = tuple(nums);
    arraylist = list(nums);
    print(arraylist);
    print(tuplelist);

list_and_tuple("34,67,55,33,12,98");