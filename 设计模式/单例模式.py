'''
单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被
称为单例类的特殊类。通过单例模式可以保证系统中一个类只有一个实
例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资
源。如果希望在系统中某个类的对象只能存在一个，单例模式是最好的
解决方案。

比如访问配置文件的内容
'''
#使用__new__方法

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


# s0 = Singleton()
# s1 = Singleton()
# print(id(s0))
# print(id(s1))

#使用装饰器
from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances
    return getinstance

@singleton
class Bar:
    pass

# b0 = Bar()
# b1 = Bar()
# print(id(b0))
# print(id(b1))

#使用元类可以控制类的创建过程
class Singleton(type):
    """
    元类继承type
    """
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance


class Bar(metaclass=Singleton):
    pass


b0 = Bar()
b1 = Bar()
print(id(b0))
print(id(b1))


#import方法
# mysingleton.py
#模块第一次导入生成pyc第二次导入直接加载pyc