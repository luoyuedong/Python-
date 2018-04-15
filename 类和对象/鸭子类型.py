'''
鸭子类型
实现了共同一种方法名
传递同一种类型
'''

class Cat(object):
    def say(self):
        print("i am a cat")

class Dog(object):
    def say(self):
        print("i am a fish")

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

company = Company(["a", "b", "c"])

class Duck(object):
    def say(self):
        print("i am a duck")

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


dog = Dog()
a = ["1", "2"]

b = ["3", "4"]
name_tuple = ["5", "6"]
name_set = set()
name_set.add("7")
name_set.add("8")
a.extend(Company('9'))
print(a)

