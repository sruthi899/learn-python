#x = list(map(input().split()))
#print(x)
#print(type(x))
class computer:
    def __init__(self,cpu,ram) :
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("config is:", self.cpu, self.ram)
com1 = computer('i5', 5)
com2 = computer('rayzen 3', 8)
com1.config()
com2.config()
        