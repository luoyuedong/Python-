# coding=utf-8
# factory_abstract 抽象工厂设计模式
# 抽象工厂, 有一组工厂方法, 每个工厂方法生产对应的对象
# 案例:你去一家餐厅吃饭, 厨子负责做'番茄炒蛋'和'白糖拌黄瓜'


class TomatoesAndEgg:
    def __init__(self):
        self.data = "番茄炒蛋"

    def getData(self):
        return self.data


class SugarAndCucumber:
    def __init__(self):
        self.data = "白糖拌黄瓜"

    def getData(self):
        return self.data


# 厨子
# 抽象工厂(可以有多个), 有一组工厂方法, 每个工厂方法生产对应的对象
class CookFactory:

    # 生产'番茄炒蛋'的工厂方法
    def cook_te(self):
        return TomatoesAndEgg()

    # 生产'白糖拌黄瓜'的工厂方法
    def cook_sc(self):
        return SugarAndCucumber()


if __name__ == "__main__":
    cook = CookFactory()

    man = cook.cook_te()
    woman = cook.cook_sc()

    data_man = man.getData()
    data_woman = woman.getData()

    print(data_man)  # => 番茄炒蛋
    print(data_woman)  # => 白糖拌黄瓜