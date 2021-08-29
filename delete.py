# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class linkedlist:
#     def __init__(self):
#         self.head = None
#
#     def delete(self, key):
#         temp = self.head
#         if temp.data == key:
#             self.head = temp.next
#             temp =None
#             llist.printlist()
#         while(temp):
#             if temp.data == key:
#                 break
#             prev = temp
#             temp = temp.next
#         if temp == None:
#             return
#         prev.next = temp.next
#         temp = None
#         llist.printlist()
#
#
#     def printlist(self):
#         temp = self.head
#         while(temp):
#             print(temp.data)
#             temp = temp.next
# llist = linkedlist()
# x = int(input("enter no of nodes:"))
# m = x
# while (x > 0):
#     n = int(input("enter  data:"))
#     s = node(n)
#     if m ==x:
#         llist.head = s
#         temp = llist.head
#     else:
#         temp.next = s
#         temp = temp.next
#     x -=1
# llist.printlist()
# key = int(input("enter the key to be deleted:"))
# llist.delete(key)

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def delete(self):
        temp = self.head
        self.head = temp.next
        llist.printlist()

    def delete1(self):
        temp = self.head
        while (temp):
            if temp.next == None:
                prev.next = None
                break
            prev = temp
            temp = temp.next
        llist.printlist()

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next








llist = linkedlist()
x = int(input("enter no of nodes:"))
m = x
while (x > 0):
    n = int(input("enter  data:"))
    s = node(n)
    if m ==x:
        llist.head = s
        temp = llist.head
    else:
        temp.next = s
        temp = temp.next
    x -=1
llist.printlist()

while(llist.head != None):
    a = int(input("chose 1 or 2 :"))
    if a == 1:
        llist.delete()
        print("first node deleted.")
    elif a == 2:
        llist.delete1()
        print("last node deleted.")

print("linked list is empty now.")






