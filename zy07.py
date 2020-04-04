"""
================================
author:cuicui
time:2020/4/4
E-mail:2396954720@qq.com
================================
"""
# 初始化
books = [{'id':'1','name':'天龙八部','position':'A区1架'},
         {'id':'2','name':'倚天屠龙记','position':'A区2架'},
         {'id':'3','name':'射雕英雄传','position':'A区3架'},
         {'id':'4','name':'鹿鼎记','position':'A区4架'}
         ]

def print_menu():
    # 打印菜单
    print('-'*50)
    print('【1】:添加图书')
    print('【2】:删除图书')
    print('【3】:显示所有图书')
    print('【4】:退出')


def add_book():
    # 添加图书
    # new_book = dict(
    #     id = input('请输入图书编号:'),
    #     name = input('请输入书名:'),
    #     position = input('请输入图书位置:')
    # )
    # books.append(new_book)

    # 添加图书(需要考虑图书编号不能重复)
    new_book = {}   # 创建字典存储图书
    while True:
        new_book['id'] = input('请输入图书编号:')
        for book in books:  # 遍历出所有图书,判断该图书编号是否存在
            if book['id'] == new_book['id']:
                print('已存在该图书编号为:{},图书名称为:{},图书位置为:{}'.format(book['id'],book['name'],book['position']))
                print('图书编号不可以重复')
                break
        else:   #上述for循环没有找到重复书籍,进入else中
            new_book['name'] = input('请输入图书名称:')
            new_book['position'] = input('请输入图书位置:')
            # 将图书添加到图书列表中
            books.append(new_book)
            print('添加成功,返回菜单')
            break


def del_book():
    # 删除图书
    book_name = input('请输入要删除的书籍:')
    # 创建空列表,用来存放找到书籍
    find_list = []
    # 遍历所有的图书,将同名图书加入find_list中
    for book in books:
        if book_name == book['name']:
            find_list.append(book)
    # 判断查找到的书籍,是否大于0
    if len(find_list) != 0:
        print('共找到{}本{},信息如下:'.format(len(find_list),book_name))
        for book in find_list:
            print('编号:{},名称:{},位置:{}'.format(book['id'],book['name'],book['position']))
        id_num = input('请输入要删除的图书编号:')
        # 根据书籍编号删除对应的书籍
        for book in find_list:
            # 判断id是否相等
            if id_num == book['id']:
                # 书籍列表中,删除该书籍
                books.remove(book)
                print('删除成功,返回菜单')
                break
            else:
                print('输入编号输入有误')
    else:
        print('很抱歉,没有该书本信息')


def all_book():
    # 显示所有图书
    book_count = len(books) # 获取当前的图书总数量
    if book_count != 0:
        # 显示所有图书信息
        print('当前共有{}本书籍,所有的图书信息如下:'.format(book_count))
        for book in books:
            print('编号:{},名称:{},位置:{}'.format(book['id'],book['name'],book['position']))
            print('查询完毕,返回菜单页面')
    else:
        print('当前系统中没有任何书籍,返回菜单页面')


def main2():
    print('------欢迎进入图书管理系统------')
    while True:
        print_menu()    # 打印菜单
        num = input('请输入您的选项:')
        if num == '1':
            add_book()  # 添加图书
        elif num == '2':
            del_book()  # 删除图书
        elif num == '3':
            all_book()  # 查询所有图书
        elif num == '4':
            print('谢谢使用,程序即将关闭')
            break
        else:
            print('您选择的有误,请重新选择')


if __name__ == '__main__':
    main2()