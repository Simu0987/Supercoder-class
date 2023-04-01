####STACK

'''class Stack:
    def ___init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return Ture
        return False
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    def push(self,data):#data=5
        if(self.is_full()):
            print("The stack is full")
        else:
            self.__top+=1   #self.top=3
            self.__element[self.__top]=data
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            data=self.__element[self.__top]
            self.__top=-1
            return data
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__element[index])
                index=-1
    def get_max_sixe(self):
        return self.__max_size
ball_stack=Stack(4)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(5)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push()
ball_stack.display()
print("size if the stack",ball_stack.get_max_size())
print("the elment deleted",ball_stack.pop())
print("After deleting the element")
ball_stack.display()
print("size of the stack",ball_stack.get_max_size()) 




####QUEUE

class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is empty")
        else:
            self.__rear+=1
            self.__element[self.__rear]=data
    def enqueue(self):
        if(self.is_empty()):
            print("Queue is empty")
        else:
            data=self.__element[self._-front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size
queue1=Queue(10)
print("Is it full",queue1.is_full())
print("Is it empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)
queue1.display()
print("Element deleted",queue1.dequeue())
queue1.display()      


###Program 1 queue
class queue:
    def _init_(self,max_size):
        self.__max_size = max_size
        self._elements = ['None']* self._max_size
        self.__front = 0
        self.__rear = -1
    def is_full(self):
        if (self._rear == self._max_size-1):
            return True
        return False
    def is_empty(self):
        if(self._front > self._rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print('Queue is full')
        else:
            self.__rear += 1
            self._elements[self._rear] = data
            
        
    def dequeue(self):
        if(self.is_empty()):
            print('The queue is empty')
        else:
            data = self._elements[self._front]
            self.__front += 1
            return data
        
    def display(self):
        for index in range(self._front,self._rear+1):
            for i in range(1,10+1):
                if(self.__elements[index] % i ==0):
                    s = True
                else:
                    s = False
                    break
            if(s):
                print(self.__elements[index])
                
        
    def get_max_size(self):
        return self.__max_size
Queue1 = queue(10)
print('Is it full',Queue1.is_full())
print('Is it empty',Queue1.is_empty())
Queue1.enqueue(13983)
Queue1.enqueue(10080)
Queue1.enqueue(7113)
Queue1.enqueue(2520)
Queue1.enqueue(2500)
Queue1.display()   

###Problem number2
def merge_list(list1,list2):
    merged_data=""
    list2.reverse()
    for i in range(len(list1)):
        if(list[i] is None):
            list1[i]=""
        if(list2[i] is None):
            list2[i]=""
        merged_data+=str(list1[i])+str(list2[i])+" "
    return merged_data[:-1]
list1=['T','sk',None,'bl']
list2=['ue','is','y','he']
merged_data=merge_list(list1,list2)
print(merged_data)   


###problem number3

def check_numbers(number_queue):
    solution_queue1=Queue(5)
    while(not number_queue.is_empty()):
        status=0
        element=number_queue.dequeue()
        for i in range(1,11):
            if elememt%i!=0:
                status=1
                break
        if status==0:
            solution_queue1.enqueue(element)
    return solution_queue1 '''



####Linked List
##traversing a linked list
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
            print(printval.dadval)
            printval=printval.nextval
list=SLinkedList()
list.headval=Node("Mon")


    
