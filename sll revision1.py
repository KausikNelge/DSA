class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class SLL:
    def __init__(self,head=None):
        self.head = head

    def InsertAtEnd(self,value):
        temp = Node(value)
        if (self.head != None):
            t1 = self.head
            while (t1.next != None):
                 t1 = t1.next
            t1.next = temp 
        else:
            self.head = temp

    def printLL(self):
        t1= self.head
        while t1 is not None:
             print(t1.data)
             t1=t1.next


obj=SLL()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.InsertAtEnd(40)


obj.printLL()