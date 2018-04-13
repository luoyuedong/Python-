'''
　动态的给原有对象添加一些额外的职责,面向切面编程(AOP),
多用于和主业务无关,但又必须的业务,如:登录认证、加锁、权限
检查等
'''
#简单装饰器模式
def handle_func(func):
    def new_func(*args, **kwargs):
        print("Hello,everyone!")
        func(*args, **kwargs)
        print("Thank you!")
    return new_func


@handle_func
def old_func(name, age):
    print("My name is %s,I'm %d years old!" % (name, age))


# 原调用方式
name = "Jet"
age = 18
old_func(name, age)

#带参数装饰器模式
def before():
    print("Hello,everyone!")


def after():
    print("Thank you!")


def handle_args(before, after):
    def handle_func(func):
        def new_func(*args, **kwargs):
            before()
            func(*args, **kwargs)
            after()
        return new_func
    return handle_func


@handle_args(before, after)    # Python语法糖
def old_func(name, age):
    print("My name is %s,I'm %d years old!" % (name, age))


# 原调用方式
name = "Jet"
age = 18
old_func(name, age)
