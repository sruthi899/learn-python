class node:
    def __init__(self,data):
        self.data = data
        self.next = None



class linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def reverse(self):
        prev = None
        cur = self.head

        while (cur != None):
            nxt = cur.next
            #change direction
            cur.next = prev
            #shifting node
            prev = cur
            cur = nxt
        self.head = prev
        print("the reversed list is:")
        llist.printlist()
    def push(self, data):
        self.data = data
        s = node(data)
        s.next = self.head
        self.head = s


llist = linkedlist()
n = int(input("enter no of nodes:"))
m = n
while (n> 0):
    x = input("enter data:")
    s = node(x)
    if m == n:
        llist.head = s
        temp = llist.head

    else:
        temp.next = s
        temp = temp.next
    n -=1
print("the linked list is:")
llist.printlist()
llist.reverse()
#llist.printlist()



