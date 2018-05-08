'''
“new”方法在Python中是真正的构造方法（创建并返回实例），通过这个方法
可以产生一个”cls”对应的实例对象，所以说”new”方法一定要有返回。
对于”init”方法，是一个初始化的方法，”self”代表由类产生出来的实例对
象，”init”将对这个对象进行相应的初始化操作。
如果（新式）类中没有重写”new”方法，Python默认是调用该类的直接父类的”new”
方法来构造该类的实例，如果该类的父类也没有重写”new”，那么将一直按照同样的规则
追溯至object的”new”方法，因为object是所有新式类的基类。
'''
class A(object):
    def __init__(self,*args,**kwargs):
        print( "init &&&&  %s" % self.__class__)
    def __new__(cls,*args,**kwargs):
        print("new &&&&  %s" % cls)
        return object.__new__(cls,*args,**kwargs) #去掉之后不能init

# a = A()

class Foo(object):
    def __new__(cls,*args,**kwargs):
        obj = object.__new__(cls,*args,**kwargs)
        #这里的object.__new__(cls,*args,**kwargs)等价于
        # super(Foo,cls).__new__(cls,*args,**kwargs)
        # object.__new__(Foo,*args,**kwargs)
        # Bar.__new__(cls,*args,**kwargs)
        # Student.__new__(cls,*args,**kwargs),即使Student和
        # Foo没有关系也是允许的，因为Student是由object派生的新类
        # 在任何新式类中，不能调用自身的__new__来创建实例，因为这会
        # 造成死循环，所以要避免出现这样的语法 Foo.__new__(cls,*args,**kwargs)
        # 或者 cls.__new__(cls,*args,**kwargs)
        print("Calling __new__ for %s" % obj.__class__)
        return obj

class Bar(Foo):
    def __new__(cls,*args,**kwargs):
        obj = object.__new__(cls,*args,**kwargs)
        print("Calling __new__ for %s" % obj.__class__)
        return obj

class Student(object):
    #Student没有__new__方法，那么会自动调用父类的__new__方法来
    #创建实例，即会自动调用object.__new__(cls)
    pass

class Car(object):
    def __new__(cls,*args,**kwargs):
        obj = object.__new__(Bar,*args,**kwargs)
        print( "Calling __new__ for %s" % obj.__class__)
        return obj

# foo = Foo()
# bar = Bar()
# stu = Student()
# car = Car()

#派生不可变类型
class Round2Float(float):
    def __new__(cls,num):
        num = round(num,2)
        obj = float.__new__(Round2Float,num)
        return obj

f=Round2Float(4.324599)
print(f)
