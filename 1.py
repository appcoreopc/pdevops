from abc import ABCMeta, abstractmethod

class Person:
  @classmethod
  @abstractmethod
  def sayHello(cls):
    print("hello")

class Employee(Person):
    def __init__(self):
        pass

    def saySomething(self):
        self.sayHello()
    # def sayHello(self):
    #     print("ok ok ok")

    
a = Employee()
a.sayHello()

a.saySomething()