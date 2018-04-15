
class Date:
    #构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year)>0 and (int(month) >0 and int(month)<=12) and (int(day) >0 and int(day)<=31):
            return True
        else:
            return False

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

#自省是通过一定的机制查询到对象的内部结构
class Person:
    """
    人
    """
    name = "user"

class Student(Person):
    def __init__(self, scool_name):
        self.scool_name = scool_name

if __name__ == "__main__":
    user = Student("慕课网")

    #通过__dict__查询属性
    # print(user.__dict__)
    # user.__dict__["school_addr"] = "北京市"
    # print(user.school_addr)
    # print(Person.__dict__)
    # print(user.name)
    a = [1,2]
    print(dir(a))

