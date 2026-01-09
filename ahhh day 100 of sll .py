# day 100 of sll iam too slow 
class Node:
    def __init__(self,info,next=None):
        self.next = next
        self.data = info


class sll:
    def __init__(self,head=None):
      self.head= head

    def InsertAtTheBeg(self,input):
        temp1=Node(input)
        if self.head == None:
            self.head = temp1
        else:
            temp1.next = self.head
            self.head = temp1

        
             
        
    def  InsertAtEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    

            







    def printLL(self):
        t1= self.head
        while t1 is not None:
            print(t1.data)
            t1= t1.next


obj = sll()
obj.InsertAtTheBeg(20)
obj.InsertAtEnd(10)

obj.printLL()