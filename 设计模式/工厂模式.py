'''
解释：处理对象创建，客户端可以申请一个对象而不用知道对象被哪个class创建。可以方
便地解耦对象的使用和创建

模式特点：工厂根据条件产生不同功能的类。

程序实例：四则运算计算器，根据用户的输入产生相应的运算类，用这个运算类处理具体的运算。

代码特点：C/C++中的switch...case...分支使用字典的方式代替。使用异常机制对除数为0的情况进
行处理。
'''
class Operation:
    def GetResult(self):
        pass

class OperationAdd(Operation):
    def GetResult(self):
        return self.op1+self.op2


class OperationSub(Operation):
    def GetResult(self):
        return self.op1-self.op2


class OperationMul(Operation):
    def GetResult(self):
        return self.op1*self.op2


class OperationDiv(Operation):
    def GetResult(self):
        try:
            result = self.op1/self.op2
            return result
        except:
            print("error:divided by zero.")
            return 0

class OperationUndef(Operation):
    def GetResult(self):
        print("Undefine operation.")
        return 0

class OperationFactory:
    operation = {}
    operation["+"] = OperationAdd();
    operation["-"] = OperationSub();
    operation["*"] = OperationMul();
    operation["/"] = OperationDiv();
    def createOperation(self,ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op

if __name__ == "__main__":
    op = input("operator: ")
    opa = input("a: ")
    opb = input("b: ")
    opa = int(opa)
    opb = int(opb)
    factory = OperationFactory()
    cal = factory.createOperation(op)
    cal.op1 = opa
    cal.op2 = opb
    print(cal.GetResult())