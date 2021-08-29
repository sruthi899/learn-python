class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        mid = self.head
        count = 0
        while(temp):
            if count == 2:
                mid = mid.next
                count = 0
            print(temp.data)
            temp = temp.next
            count +=1

        print(mid.data)


#if __name__ == '__main__':
     llist = linkedlist()
     n = int(input("enter the no of nodes:"))
     m = n
     while(n>0):
         x = input(("enter the data:"))
         s = node(x)
         if m == n:
             llist.head = s
             temp = llist.head

         else:
             temp.next = s
             temp = temp.next
         n -=1
     llist.printlist()
    # llist.head = node(1)
    # second = node(2)
    # third = node(3)
    # llist.head.next = second
    # second.next = third
    # llist.printlist()
    # print(id(third))
    # print(id(second.next))
