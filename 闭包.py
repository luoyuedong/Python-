'''
闭包满足的条件：
1.必须有一个内嵌函数
2.内嵌函数必须引用外部函数中的变量
3.外部函数的返回值是内嵌函数

闭包中内函数修改外函数局部变量
1 在python3中，可以用nonlocal 关键字声明 一个变量， 表示这个变量不是局部
变量空间的变量，需要向上一层变量空间找这个变量。
2 在python2中，没有nonlocal这个关键字，我们可以把闭包变量改成可变类型数据
进行修改，比如列表。

使用闭包的过程中，一旦外函数被调用一次返回了内函数的引用，虽然每次调用内函数
，是开启一个函数执行过后消亡，但是闭包变量实际上只有一份，每次开启内函数都在
使用同一份闭包变量
'''

def outer(a):
    b = 10
    def inner():
        print(a+b)
    return inner


#修改闭包变量的实例
def outer2(a):
    b = 10
    c = [a]
    d = 10
    def inner():
        nonlocal b
        b+=1
        c[0] += 1
        print('b:',c[0])
        print('c:',b)
        print('d:',d)
    return inner

#闭包变量只有一份
def outer3(x):
    def inner(y):
        nonlocal  x
        x+=y
        return x
    return inner

if __name__ == '__main__':
    # demo = outer(5)
    # demo()
    # demo2 = outer(7)
    # demo2()

    demo3 = outer2(5)
    demo3()
    outer2(10)

    a = outer3(10)
    print(a(1))
    print(a(3))
