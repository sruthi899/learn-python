class stack:
    def __init__(self):
        self.stack =[]
    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def remove(self):
        if len(self.stack) <= 0:
            return ("no element in stack")
        else:
            self.stack.pop()
    def top(self):
        return self.stack[-1]

s = stack()
x = int(input("enter no of data:"))
while x > 0:
    data = int(input("enter data:"))
    s.add(data)
    x -=1
#print(s.remove())
print(s.top())
