class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None

    def push(self, n):
        s = node(n)
        s.next = self.head
        self.head = s
        #llist.printlist()

    def append(self, n):
        s = node(n)
        if self.head is None:
            self.head = s
        last = self.head
        while(last.next):
            last = last.next
        last.next = s
        #llist.printlist()

    def insertAfter(self, prev, n):
        s = node(n)
        s.next = prev.next
        prev.next = s
        #llist.printlist()

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

llist = linkedlist()
x = int(input("enter no of nodes:"))
while (x > 0):
    n = int(input("enter new data:"))
    a = int(input("choose 1 or 2 :"))
    if a == 1:
        llist.push(n)
    elif a == 2:
        llist.append(n)
    x -=1
llist.printlist()





# llist.push(1)
# llist.push(4)
# llist.push(9)
# llist.append(5)
# llist.insertAfter(llist.head, 8)
# llist.printlist()

