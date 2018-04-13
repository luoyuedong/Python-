
'''
Python GC主要是使用引用计数来跟踪和回收垃圾，在引用计数的基础上，同过“标记-清除”
解决容器对象可能产生的循环引用问题，通过分代回收以空间换时间的方法提高垃圾回收效率

方法
1.引用计数
PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。当一个对象有新
的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，它的ob_refcnt就会减少.
引用计数为0时，该对象生命就结束了。
2.标记-清除机制
基本思路是先按需分配，等到没有空闲内存的时候从寄存器和程序栈上的引用出发，遍历以对象为节
点、以引用为边构成的图，把所有可以访问到的对象打上标记，然后清扫一遍内存空间，把所有没标
记的对象释放。
3.分代技术
将系统中的所有内存块根据其存活时间划分为不同的集合，每个集合为一个代，垃圾收集频率随着代的
存活时间的增大而减小，存活时间通常利用经过几次垃圾回收来度量。
python默认定义了三代对象的集合，索引数越大，对象存活时间越长
 当某些内存块M经过了3次垃圾收集的清洗之后还存活时，我们就将内存块M划到一个集合A中去，而新分配的内存都
 划分到集合B中去。当垃圾收集开始工作时，大多数情况都只对集合B进行垃圾回收，而对集合A进行垃圾回收要隔相
 当长一段时间后才进行，这就使得垃圾收集机制需要处理的内存少了，效率自然就提高了。在这个过程中，集合B中的
 某些内存块由于存活时间长而会被转移到集合A中，当然，集合A中实际上也存在一些垃圾，这些垃圾的回收会因为这
 种分代的机制而被延迟。
'''
__author__ = 'luoxiaodong'
class ClassA():
    def __init__(self):
        print('object id:%s'%str(hex(id(self))))

    def __del__(self):
        print('object del id: %s'%str(hex(id(self))))

def f1():
    while True:
        c1 = ClassA()
        del c1

#循环引用导致内存泄漏
def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2

#垃圾回收
import gc
import time
def f3():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
        print(gc.garbage)
        print(gc.collect())
        print(gc.garbage)
        time.sleep(10)


if __name__ == '__main__':
    # f1()
    # f2()
    gc.set_debug(gc.DEBUG_LEAK)
    f3()