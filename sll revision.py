
class Node:
    def __init__(self,info,next=None):
        self.data= info
        self.next = next



class SLL:
    def __init__(self,head=None):
        self.head = head
        

    def InsertAtBeg (self, value):
        temp = Node(value)

        if self.head == None:
            self.head = temp

        else:
            temp.next = self.head
            self.head = temp


    def InsertAtEnd(self,input):
        temp1 = Node(input)
        if self.head != None:
            t1 = self.head
            while(t1.next != None):
                t1= t1.next      
            t1.next = temp1      
        else:
            self.head=temp1    



    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1= t1.next




obj= SLL()
obj.InsertAtBeg(10)
obj.InsertAtEnd(20)        


obj.printLL()