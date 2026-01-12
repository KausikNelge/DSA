
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
            self.head = temp   # so you have initilized the node empty ( self.head == none) so the temp value which is tee input it should 

        else:
            temp.next = self.head
            self.head = temp


    def InsertAtMid(self,value,x ):
        temp = Node(value)
        t1 = self.head
        while t1.next != None:
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp    
            t1 = t1.next


