###

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end="")
            temp=temp.next
llist=LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
print("Given linked list")
llist.printList()
llist.reverse()
print("\nReversed linkedlist")
llist.printList()     '''


######
class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=1
        while temp is not None:
            temp=temp.next
            count+=1
        return count
    def insertAtBegining(self,value):   ###begining
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous=new_node
            self.head=new_node
    def printLinkedList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep="")
            temp=temp.next
    def insertAtEnd(self,value):     ###end
        new_node=Node(value)
        if self.isEmpty():
            self.insertAtBegining(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp =temp.next
            temp.next=new_node
            new_node.previous=temp
    def insertAtPosition(self,value,position):   ###position
        temp=self.head
        count=1
        while temp is not None:
            if count==position-1:
                break
            count+=1
            temp=temp.next
        if position==1:
            self.insertAtBegining(value)
        elif temp is None:
            print("There are less than {}-1 element in the linkedlist".format(positon,position))
        elif temp.next is None:
            self.insertAtEnd(value)
        else:
            new_node=Node(value)
            new_node.next=temp.next
            new_node.previous=temp
            temp.next.previous=new_node
            temp.next=new_node
    def deleteFromBegining(self):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements")
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.previous=None
    def deleteFromLast(self):
        if self.isEmpty():
            print("Linked list is empty cant delete elements.")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.previous.next=None
            temp.previous=None
    def deleteFromPosition(self,position):
        if self.isEmpty():
            print("Linked list is empty cant delete element.")
        elif position ==1:
            self.deleteFromBegining()
        else:
            temp=self.head
            count=1
            while temp is not None:
                if count ==position:
                    break
                temp = temp.next
                count=count+1
            if temp is None:
                print("There are less than {}elements in Linked list")
            elif temp.next is None:
                self.deleteFromLast()
            temp.previous.next=temp.next
            temp.next.previous=temp.previous
            temp.next=None
            temp.previous=None
            
            
##begining            
x=DoublyLinkedList()
print(x.isEmpty())
x.insertAtBegining(5)
x.printLinkedList()
x.insertAtBegining(15)
x.insertAtBegining(25)
x.insertAtBegining(35)
x.printLinkedList()
print("no of nodes",x.length())
##ebd
x=DoublyLinkedList()
print(x.isEmpty())
x.insertAtEnd(5)
x.printLinkedList()
x.insertAtEnd(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("no of nodes",x.length())
##position
x=DoublyLinkedList()
print(x.isEmpty())
x.insertAtEnd(5)
x.insertAtEnd(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("no of nodes",x.length())
x.insertAtPosition(8,2)
x.printLinkedList()



########






        
