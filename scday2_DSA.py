#Traversing a linked list

class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SLinkedList:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
list=SLinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3
list.AtBegining("Sun")
list.listprint()



##Function to add new node
def AtEnd(self,newdata):
    Newnode=Node(newdata)
    if self.headval is None:
        self.headval=NewNode
        return
    laste=self.headval
    while(laste.nextval):
        laste=laste.nextval
    laste.nextval=NewNode
##print the linked list
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
list=SLinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3
list.AtEnd("Sun")
list.listprint()



##Function to add node
def InBetween(self,middle_node,newdata):
    if middle_node is None:
        print("The mentioned node is absent")
        return
    NewNode=Node(newdata)
    NewNode.nextval=middle_node.nextval
    middle_node.nextval=NewNode
##print the linked list
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
list=SLinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3
list.Inbetween(list.headval.nextval.nextval,"Fri")
list.listprint()



#############
class Node:
    def __init__(self,data):
        self.item=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.start_node=None
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n=self.start_node
            while n is not None:
                print(n.item," ")
                n=n.ref
    def insert_at_start(self,data):
        new_node=Node(data)
        if self.start_node is None:
            self.start_node=new_node
            return
        n=self.start_node
        while n.ref is not None:
            n=n.ref
        n.ref=new_node
    def delete_at_start(self):
        if self.start_node is None:
                print("The list has no element to delete")
                return
            self.start_node=self.start_node.ref
    def delete_at_end(self):
        if self.start_node is None:
                print("The list has no element to delete")
                return
        n=self.start_node

    def insert_at_index(self,index,data):
        if index==1:
            new_node=Node(data)
            new_node.ref=self.start_node
            self.start_node=new_node
        i=1
        n=self.start_node
        while i<index-1 and n is not None:
            n=n.ref
            i=i+1
        if n is None:
            print("Index out of Bound")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
new_linked_list=LinkedList()

        
        

    












