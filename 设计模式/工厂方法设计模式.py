# coding=utf-8
# factory.py 工厂方法设计模式
# 根据传入参数的不同, 而返回对应的对象
# 案例:你去一家餐厅,给厨子'番茄'和'鸡蛋',厨子返回给你'番茄炒鸡蛋';给厨子'白糖'和'黄瓜',厨子返回给你'白糖拌黄瓜'


class TomatoesAndEgg:
    def __init__(self):
        self.data = "男士喜欢吃番茄炒蛋"

    def getData(self):
        return self.data


class SugarAndCucumber:
    def __init__(self):
        self.data = "女士喜欢吃的"

    def getData(self):
        return self.data


# 工厂方法: 根据传入参数的不同, 而返回对应的对象
def cook_factory(sex):
    if sex == "man":
        food = TomatoesAndEgg
    elif sex == "woman":
        food = SugarAndCucumber
    else:
        raise ValueError("请出入正确的性别: {}".format(sex))
    return food()


if __name__ == "__main__":
    man = cook_factory("man")
    woman = cook_factory("woman")

    data_man = man.getData()  # 返回String类型数据
    data_woman = woman.getData()  # 返回int类型数据
    # getData()返回不同类型的数据, 这在实际开发中是很常见的

    print(data_man)  # => 男士喜欢吃番茄炒蛋
    print(data_woman)