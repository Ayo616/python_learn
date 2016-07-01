
'''列表是python中最基本的知识，它相当于是集合，它不需要定义类型，并且在集合中能存放不同类型的元素

'''

def test():
    list=[1,2,3,4,5,6,7]
    print(list)                 #输出整个列表
    print(len(list))            #输出列表的长度

    list.append(8)              #在列表最后添加元素
    print(list)

    list.pop()                  #删除列表最后的元素
    print(list)

    list2=[8,9,10]              #拼接列表
    list.extend(list2)
    print(list)

    list.remove(5)              #删除列表中某个指定元素
    print(list)

    list.insert(0,0)            #向指定位置插入元素
    print(list)



if __name__ == '__main__':
    test()


'''输出结果如下

[1, 2, 3, 4, 5, 6, 7]
7
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 6, 7, 8, 9, 10]
[0, 1, 2, 3, 4, 6, 7, 8, 9, 10]

'''