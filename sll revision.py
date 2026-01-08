# sll revision


class node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next


class SinlyLinklist:
    def __init__(self,head=None):
        self.head = head


    def InsertAtEnd(self,value):
        temp = node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                  t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1= t1.next
        print(t1.data)

obj = SinlyLinklist()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.printLL()