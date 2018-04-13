import random
import time,threading

def thread_run(urls):
    print('Current %s is running..' % threading.current_thread().name)
    for url in urls:
        print('%s --->> %s' % (threading.current_thread().name,url))
        time.sleep(random.random())
    print('%s ended.' %threading.current_thread().name)

print('%s is running..' % threading.current_thread().name)

# t1 = threading.Thread(target=thread_run, name='Thread_1', args=(['url1','url2','url3'],))
# t2 = threading.Thread(target=thread_run, name='Thread_2', args=(['url4','url5','url6'],))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
print('%s ended.' % threading.current_thread().name)

class myThread(threading.Thread):
    def __init__(self,name,urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print('Current %s is running..' % threading.current_thread().name)
        for url in self.urls:
            print('%s --->> %s' % (threading.current_thread().name, url))
            time.sleep(random.random())
        print('%s ended.' % threading.current_thread().name)

print('%s is running..' % threading.current_thread().name)

t1 = myThread(name='Thread_1', urls=['url1','url2','url3'])
t2 = myThread(name='Thread_2', urls=['url4','url5','url6'])

t1.start()
t2.start()
t1.join()
t2.join()