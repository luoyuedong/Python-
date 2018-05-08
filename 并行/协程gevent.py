from gevent import monkey;monkey.patch_all()
import gevent
from urllib import request
from gevent.pool import Pool

def run_task(url):
    print('visit --> %s' % url)
    response = request.urlopen(url)
    data = response.read()
    print('%d bytes received from %s.' % (len(data), url))
    return 'url:%s --->finish' % url

if __name__ == '__main__':
     urls = ['http://github.com/','https://www.python.org/','https://www.cnblogs.com/']
     pool = Pool(2)
     # greenlets = [gevent.spawn(run_task, url) for url in urls]
     # gevent.joinall(greenlets)
     results = pool.map(run_task, urls)
     print(results)
