'''
Pool可以指定数量的进程供用户调用，默认大小是CPU的核数，当有新的请求
提交到Pool中，如果池没有满，那么就会创建一个新的进程用来执行请求，
但如果池中的进程数到达规定的最大值，请求就会等待知道池中有进程结束。
'''

from multiprocessing import Pool
import os,time,random

def run_task(name):
    print('Task %s (pid = %s) is running...' % (name, os.getpid()))
    time.sleep(random.random()*3)
    print('Task %s end.'% name)

if __name__ == '__main__':
    print('Current process %s' % os.getpid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task,args=(i,))
    print('Waiting all done')
    p.close()
    p.join()
    print('All done')