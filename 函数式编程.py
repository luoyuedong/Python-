#filter 函数
a = [1,2,3,4,5,6,7]
b = filter(lambda x:x>5, a)
print(list(b))


# map函数是对一个序列的每个项依次执行函数，下面是对一个序列每个项都乘以2：
b = map(lambda x:x*2, a)
print(list(b))

#reduce函数是对一个序列的每个项迭代调用函数，下面是求3的阶乘：
from functools import reduce
b = reduce(lambda x,y:x*y,a)
print(b)