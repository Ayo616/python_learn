'''
学习定义函数、使用函数、以及着重对函数的参数进行解析

函数：1、自定义函数 2、内置函数（本语言中）
参数：1、必选参数 2、默认参数 3、可变参数 4、命名关键字参数 5、关键字参数



总结要点(先看例题再回头看总结)
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

'''

def test():
    print("this is method")        #h函数以def开头

def test1(x,y):
    print(x,y)

def test2(x,y=2):
    print(x,y)

def test3(*number):
    for each in number:
        print(each)

def test4(name,age,**kwargs):
    print(name,age)
    print(kwargs)

def test5(name,*,age):
    print(name)
    print(age)





if __name__ == '__main__':
    test()

    test1(4,5)
    #输出结果 4 5

    test2(4)
    #输出结果 42
    test2(4,5)
    #45，说明当函数设置时有默认参数，可以只传递一个未知参数即可。

    test3(1,2,3)
    #输出结构123
    test3(1,2,3,4,5,6)
    #输出结果123456
    data = [4,3,2,1]
    test3(*data)
    #输出结果4321

    test4("小明",23)
    #输出结果 小明 23
    test4("小明",23,gander="男",hobby="篮球")
    #输出结果 小明 23 {'gander': '男', 'hobby': '篮球'}

    test5("小明",age=24)
    #输出结果 小明 24
    test5("小明",age=25,gander="男")
    #报错，没有设置gander这个参数



