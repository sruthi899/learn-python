class employee:
    empcount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        employee.empcount += 1
    def displaycount(self):
        print("total employees:", employee.empcount)
    def displayemployee(self):
        print("name:", self.name, "age:", self.age)
emp1 = employee('sruthi',22 )
emp2 = employee('xyz', 30)
emp1.displayemployee()
emp2.displayemployee()
emp1.displaycount()
print("count:", employee.empcount)

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
print ("Total Employee %d" % Employee.empCount)


