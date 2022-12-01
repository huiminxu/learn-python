# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def print_hi2():
    # int
    a, b, c, d = 1, 2, 3, 4
    f = 5.5
    print(type(a), type(b), type(c), type(d), type(f))

    # string
    str = 'imooc'
    print(str, str[1:], str[0:3], str[3], str + 'Test', str * 2)

    # list (变量名称不要使用 list)
    list = ['abcd', 123, 123.45, 'imooc']
    tinylist = [123, 'imoc']
    # list(   ) 如果变量名称和方法名称一致，则会报错,list的增删改查
    print(list, tinylist, list[0], list[1:3], tinylist * 2)

    # tuple 元素不能改变
    tuple = ("abcd", 786, 'imooc', 70.2)
    tinytuple = (123, 'tuple')
    print(tuple, tinytuple, tuple[0], tuple[1:3], tinytuple * 2)

    # set 集合
    student = {'Tom', 'Mary', 123, 'T', 'Rose'}
    stu = set('Tom123')
    if "Rose" in student:
        print('在集合中')
    else:
        print('不在集合中')
    print(student, stu, student - stu, stu & student, stu | student, stu ^ student)

    # 字典
    dic = {}
    dic["one"] = "1-慕课网"
    dic[2] = "2-aimuku"

    tinydic = {"name": 'sjdbvj', 3: 'sndjakcndk'}
    print(dic["one"])
    print(tinydic)
    print(tinydic.keys())
    print(tinydic.values())
    d = ['1', 'a']
    d.append('2')
    print(d, ['a', 'b'])

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

if __name__ == '__main__':
    print_hi2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
