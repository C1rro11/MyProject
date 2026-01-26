#定义一个至少具
#有两个方法的类：
#getString：从控制台输
#入获取字符串
#printString：以大写字母打印字符串
#还请包括简单的测试功能
#来测试类方法。

class define_class:
    def get_String(self):
        self.s = input();
    
    def print_String(self):
        print(self.s.upper());

A = define_class();
A.get_String();
A.print_String();