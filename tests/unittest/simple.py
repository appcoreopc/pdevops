from unittest.mock import Mock, patch

class Employee:
    def __init__(self, a):
        self.a = a         

    def add(self, a, b):
        self._validate(a)
        return self.a.add(a,b)
    def _validate(self, a):
        if a > 0:
            return a
        else:            
          raise "error!"

class Adder: 

    def add(self, a, b):
        return a + b


mock = Mock()
emp = Employee(mock)
emp.add(10, 20)
mock.add.assert_called()


with patch.object(emp, '_validate', wraps=emp._validate) as monkey:
         emp.add(100, 200)
         monkey.assert_called_with(100)