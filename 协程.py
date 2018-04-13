
'''
非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置，
作用相当于是暂停或开始执行函数
优点：
1.协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因
此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
2.不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程
中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多
'''

import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    c.__next__()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()




if __name__=='__main__':
    c = consumer()
    produce(c)