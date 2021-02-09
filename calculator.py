class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b    

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b

    def check_operand(self):
        if self.operand == "+":
            result = self.add()
            print(result)
        elif self.operand == "-":
            result = self.subtract()
            print(result)
        elif self.operand == "*":
            result = self.multiply()
            print(result)
        elif self.operand == "/":
            result = self.divide()
            print(result)

