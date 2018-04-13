import os
from multiprocessing import  Process

def run_proc(name):
    print('Child process %s (%s) Running...'%(name, os.getpid()))

if __name__ == '__main__':
    print('Parent proces %s.'% os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i)))
        p.start()

    p.join() #实现进程间的同步
    print('end')