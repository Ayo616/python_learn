'''
学习  try except finally
新的打开方式  with open as
往文件中写数据  open("","w") 或者使用write
'''


from builtins import *


def test1():
    try:
        connection = open("noexsist.txt")
        connection.readline()
        connection.close()
    except:
        print("该文件不存在")


def test2():
    try:
        with open("noexsist.txt") as connection:  # 我们提倡使用这种方式
            connection.readline()
    except:
        print("该文件不存在，并且with语句帮我自动关闭文件")


def test3():
    info = ["hello python"]
    with open("data.txt", "a") as conn:
        print(info, file=conn)                       #两种方式都可以写入文件
        conn.write("hello")
        # print("why")


if __name__ == '__main__':
    test1()
    test2()
    test3()
