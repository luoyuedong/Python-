'''
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访
问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器：
'''

#迭代器
list = [1,2,3,4]
it = iter(list)
print(next(it))
print(next(it))

#使用for循环
list = [1,2,3,4]
it = iter(list)
for x in it:
    print(x,end=" ")
print('\n')

#调用一个生成器函数，返回的是一个迭代器对象。
import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()