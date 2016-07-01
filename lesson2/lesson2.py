'''
运用python打开一个txt文件，并读取里面内容，进行分割
'''

def querry():

    connection = open("data.txt")                 #利用open函数打开文件
    for each_line in connection:                  #for循环迭代
        print(each_line)

def insert():
    connection2 = open("data.txt","a")            #打开写入模式
    connection2.write("enjoy your python ")


def split_up():
    connection1 = open("data.txt")
    data = connection1.readline()
    data1 = connection1.readline()
    print(data)
    print(data1)
    (a,b) = data1.split(",",1)                    #分割函数，以逗号为分割，分割成两部分
    print(a)
    print(b)







if __name__ == '__main__':

    print("获取内容后分割数据")
    split_up()
    print("——————————————————")

    print("向文本中插入数据")
    insert()
    print("——————————————————")

    print("查询文本中的数据")
    querry()
