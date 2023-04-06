##Linear search
'''def linearSearch(array,n,x):
    for i in range(0,n):
        if (array[i]==x):
            return i
    return -1
array = [2,4,0,1,9]
x= 1
n=len(array)
result = linearSearch(array,n,x)
if(result == -1):
    print("Element not found")
else:
    print("elemnt found at index:",result)  


##Binary search 
def binarySearch(array,x,low,high):
     while low<=high:
         mid = low +(high - low)
         if array[mid]==x:
             return mid
         elif array[mid]<x:
            low = mid+1
         else:
            high = mid -1
     return -1
array = [3,4,5,6,7,8,9]
x=7
result = binarySearch(array,x,0,len(array)-1)
if result!=-1:
    print("element is present at index" + str(result))
else:
    print("not found") 


#######
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val)+"->",end='')
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val)+"->",end='')   
def preorder(root):
    if root:
        print(str(root.val) + "->",end="")
        preorder(root.left)
        preorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("Inorder Traversal")
inorder(root)
print("\nPreorder Traversal")
preorder(root)
print("\nPostorder Traversal")
postorder(root)       '''



############
##Binary Search tree operations
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.key)+"->",end='')
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.left,key)
    return node
#####Deleting a node
def deleteNode(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left=deleteNode(root.left,key)
    elif(key>root.key):
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=
root = None
root = insert(root, 0)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)
print("Insert Traversal:",end="")
inorder(root)


#####Problem number1
#A train is identified by its name and list of compartments. The compartments are identified by its name,total seating capacity and the number
#of passengers. Implement the class Train as given in the class diagram. 
#Write a python program to implement the following: count_compartments()- returns the total number of compartments in the train check_vacancy()
#-returns the count of the compartments in which more than 50% of the seats are vacant Note :Compartment list is maintained as a linked list
#where data in each node refers to a compartment.

class Node:
    def __init__(self,name,occ,tot):
        self.name = name
        self.occup = occ
        self.total = tot
        self.next = None
        
class Compartment:
    def __init__(self):
        self.head = None

    def addcompartment(self,node):
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node
    def returntrain(self):
        return self.head

class Train:
    def __init__(self,train_name,compartment_list):
        self.__train_name=train_name
        self.__compartment_list = compartment_list
        
    def get_train_name(self):
        return self.__train_name
    def get_compartment_list(self):
        first = self.__compartment_list.head
        while first is not None:
            print(first.name)
            first = first.next
    def count_compartments(self):
        first = self.__compartment_list.head
        cnt=0
        while first is not None:
            cnt+=1
            first = first.next
        print(cnt)
    def check_vacancy(self):
        first = self.__compartment_list.head
        cnt=0
        while first is not None:
            tot = first.total
            occ = first.occup
            emp = (tot-occ)/tot
            if emp>=0.5:
                cnt+=1
            first= first.next
        print(cnt)
    
e1 = Node("SL",250,450)
e2 = Node("2AC",125,280)
e3 = Node("3AC",120,300)
e4 = Node("FC",160,300)
e5 = Node("1AC",100,210)
c = Compartment()
c.addcompartment(e1)
c.addcompartment(e2)
c.addcompartment(e3)
c.addcompartment(e4)
c.addcompartment(e5)
t = Train("DHNBD ALLEPY",c)
t.count_compartments()
t.get_compartment_list()
t.get_train_name()
t.check_vacancy()




#######Problem number2
###Mary is a kindergarten teacher. She has given a task to the chidren after teaching them a list of words. The task is find the unknown words
#(other than the words they already know) from the given text. Write a python function which accepts the text and the known list of words and
#returns the set of unknown words found.


def unknownwords(text,vocab):
    s = set()
    for wd in text.split():
        if wd not in vocab:
            s.add(wd)
    if len(s)==0:
        return -1
    return s
unknownwords("the sun rises in the east",["sun","in","east","doctor","day"])
        
        



