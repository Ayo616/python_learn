'''
我们来认识一个快速生成列表的方式：列表生成式

了解两个器：1、生成器 2、迭代器

总结：
生成器是对列表生成式的一种改进，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
定义generator的一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行


我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：

生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的
'''
#首先介绍列表生成器
from collections import Iterable


def test():
    list=[]
    for each in range(1,8):               #range()中的参数表示范围
        list.append(each)
    print(list)


    list=[x*x for x in range(1,9)]        #这种特别的写法很简便
    print(list)



def test1():
    list = (x*x for x in range(1,9))       #注意与上面的比较，这里是（）
    a=next(list)                           #注意这里可以用next()不断取得下一个值，当然也可以用循环
    print(a)
    for each in list:
        print(each)


def test2(max):                               #斐波拉契数列
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)                             #生成器的关键词yield
        a, b = b, a + b
        n = n + 1
    return 'done'

def test3():
    a=isinstance('abc', Iterable)             #用来判断是否为该类型，是返回true,反之
    print(a)

if __name__ == '__main__':

    test()
    #输出结果[1, 2, 3, 4, 5, 6, 7]
    #输出结果[1, 4, 9, 16, 25, 36, 49, 64]


    test1()
    #输出结果1, 4, 9, 16, 25, 36, 49, 64


    test2(6)
    #输出结果112358


    test3()
    #输出结果true