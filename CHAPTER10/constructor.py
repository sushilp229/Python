class employee:
    language = "python"
    salary = 300000
    period = "4"
    def __init__(self):
        print("i am creating an object")
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    def greet(self):
        print("good morning")
harry = employee()
harry.language = "java"
# print(harry.language, harry.salary, harry.period)
harry.greet()
employee.getinfo(harry)