__author__ = 'luoyuedong'
__date__ = '2018/5/6 20:56'

import gevent
from gevent import monkey;monkey.patch_all()
import urllib.request
def get_body(i):
	print("start",i)
	urllib.request.urlopen("http://www.baidu.com")
	print("end",i)
tasks=[gevent.spawn(get_body,i) for i in range(100)]
gevent.joinall(tasks)
"""
说明：从结果来看，多线程与协程的效果一样，都是达到了IO阻塞时切换的功能。不同的是，多线程切换的是线程（线程间切换），协程
切换的是上下文（可以理解为执行的函数）。而切换线程的开销明显是要大于切换上下文的开销，因此当线程越多，协程的效率就越比多
线程的高。（猜想多进程的切换开销应该是最大的）

Gevent使用说明
monkey可以使一些阻塞的模块变得不阻塞，机制：遇到IO操作则自动切换，手动切换可以用gevent.sleep(0)（将爬虫代码换成这个，效果一样可以达到切换上下文）
gevent.spawn 启动协程，参数为函数名称，参数名称
gevent.joinall 停止协程


"""