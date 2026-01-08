# learning sll in dsa by chai aur code

class Node:
    def  __init__(self,info,next=None):
        self.data= info
        self.next = next

class SinglyLinkedlist:
    def __init__(self,head=None):
        self.head = head


    def inserstAtEnd(self,value)