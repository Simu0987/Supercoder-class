
######Problem Number1
class Queue:
    def __init__(self, FQsize, SQsize):
        self.__max_size = FQsize + SQsize
        
        self.__Fmax = FQsize
        self.__Smax = SQsize

        self.__element1 = [None] * FQsize
        self.__front1 = 0
        self.__rear1 = -1

        self.__element2 = [None] * SQsize
        self.__front2 = 0
        self.__rear2 = -1

        self.__element3 = [None] * (FQsize + SQsize)
        self.__front3 = 0
        self.__rear3 = -1
    def is_full_element1(self):
        if(self.__rear1 == self.__Fmax - 1):
            return True
        return False
    
    def is_full_element2(self):
        if(self.__rear2 == self.__Smax - 1):
            return True
        return False
    

    def is_empty_element1(self):
        if(self.__front1 > self.__rear1):
            return True
        return False

    def is_empty_element2(self):
        if(self.__front2 > self.__rear2):
            return True
        return False

    def element1_enqueue(self,data):
        if(self.is_full_element1()):
            print("Queue full")
        else:
            self.__rear1 += 1
            self.__element1[self.__rear1] = data
    
    def element2_enqueue(self,data):
        if(self.is_full_element2()):
            print("Queue full")
        else:
            self.__rear2 += 1
            self.__element2[self.__rear2] = data

    def element1_dqueue(self):
        if(self.is_empty_element1()):
            # print("Empty queue 1")
            return -999
        else:
            data = self.__element1[self.__front1]
            self.__front1 += 1
            return data
    
    def element2_dqueue(self):
        if(self.is_empty_element2()):
            # print("Empty queue 2")
            return -999
        else:
            data = self.__element2[self.__front2]
            self.__front2 += 1
            return data
    def element3_enqueue(self,data):
        self.__rear3 += 1
        self.__element3[self.__rear3] = data
    
    def logic(self):
        c = 0
        while(c < self.__max_size):
            c+=1
            d1 = self.element1_dqueue()
            d2 = self.element2_dqueue()
            if(d1 != -999):
                self.element3_enqueue(d1)
            if(d2 != -999):
                self.element3_enqueue(d2)
    def display1(self):
        # print(self.__element1)
        print("First queue")
        for i in range(self.__front1, self.__rear1+1):
            print(self.__element1[i],end =  ' ')
        print()

    def display2(self):
        # print(self.__element2)
        print("Second Queue")
        for i in range(self.__front2,self.__rear2+1):
            print(self.__element2[i],end = ' ')
        print()
    
    def display3(self):
        # print(self.__element3)
        print("Final queue")
        for i in range(self.__front3, self.__rear3+1):
            print(self.__element3[i],end = ' ')
        print()

queue = Queue(2,3)
queue.element1_enqueue(1)
queue.element1_enqueue(2)
queue.display1()
queue.element2_enqueue(11)
queue.element2_enqueue(22)
queue.element2_enqueue(33)
queue.display2()
queue.logic()
queue.display3()



####Problem Number2
class Queue:

    def __init__(self,max_size):
        self.__max_size = max_size
        
        self.__elements = [None] * self.__max_size
        self.__evenly_divisible = [None] * self.__max_size
        
        self.__elementsFront = 0
        self.__elementsRear = -1

        self.__evenlyFront = 0
        self.__evenlyRear = -1
    
    def is_full(self):
        if(self.__elementsRear == self.__max_size - 1):
            return True
        else:
            return False
    
    def is_empty(self):
        if(self.__elementsFront > self.__elementsRear):
            return True
        else:
            return False
    
    def elementEnqueue(self, data):
        if(self.is_full()):
            print("~ the queue is full!")
        else:
            self.__elementsRear += 1
            self.__elements[self.__elementsRear] = data


    def evenlyEnqueue(self, data):
        self.__evenlyRear += 1
        self.__evenly_divisible[self.__evenlyRear] = data


    def logic(self):
        for i in range(self.__elementsFront, self.__elementsRear+1):
            c = 0
            for j in range(1,11):
                if(self.__elements[i] % j == 0):
                    c+=1
            if(c == 10):
                self.evenlyEnqueue(self.__elements[i])
                        

    def Elementsdisplay(self):
        for i in range(self.__elementsFront, self.__elementsRear+1):
            print(self.__elements[i], end= ' ')
        print()

    def display(self):
        for i in range(self.__evenlyFront, self.__evenlyRear+1):
            print(self.__evenly_divisible[i], end= ' ')
        print()

queue = Queue(5)
queue.elementEnqueue(13983)
queue.elementEnqueue(10080)
queue.elementEnqueue(7113)
queue.elementEnqueue(2520)
queue.elementEnqueue(2500)
queue.logic()
print("Original queue:-",end = ' ')
queue.Elementsdisplay()
print("After action:-", end = ' ')
queue.display()




#####Problem Number3
l1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
l2 = ['y' , 'tor', 'e', 'eps', 'ay', None, 'le', 'n']
w = ""
for i in range(0,len(l1)):
    w = w+str(l1[i]) + str(l2[len(l2)-i-1])+" "   
w.replace("None","")
print(w)
