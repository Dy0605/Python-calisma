class Calc(object):

    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b

    def add(self):
        return self.value1 + self.value2
    
    def substrac(self):
        return self.value1 - self.value2
    
    def multiply(self):
        return self.value1 * self.value2
    
    def division(self):
        return self.value1 / self.value2
    

v1 = int(input("choose first number: "))

selection = input("choose: add(1), substrac(2), multiply(3), division(4): ")

v2 = int(input("choose second number: "))

c1 = Calc(v1,v2)

if selection == "1":
    print(f'result: {c1.add()}')
elif selection == "2":
    print(f'result: {c1.substrac()}')
elif selection == "3":
    print(f'result: {c1.multiply()}')
elif selection == "4":
    print(f'result: {c1.division()}')
