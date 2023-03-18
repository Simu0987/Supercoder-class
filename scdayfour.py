#DAY 4
1) false
2) true
3) true
4) false
5) true  

#Exapme1
class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num()) 

#Example2
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=Shoe(1000,"canvas")
print("the uique id of the object",id(s1))
print(s1) 


#Example3
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    def __str__(self):
        return "Shoe with price:" + str(self.price)+" and material:" + self.material
s1=Shoe(1000,"canvas")
print(s1)  

#Example4
class Mobile:
    def __init__(self,price,brand):
        print(id(self))
        self.price=price
        self.brand=brand
        self.total_price=None
    def display(self):
        print("Displaying details:")
    def purchase(self):
        if self.brand == "oneplus":
            discount =10
        else:
            discount=5
        self.totalprice=self.price - self.price * (discount/100)
        print("Total price of", self.brand,"mobile is",self.total_price)
        print("Calculating price:")
mob1=Mobile("Apple",20000)
mob2=Mobile("oneplus",10000)
mob1().purchase
mob2().purchase()
#mob1.amount  

#Example5
class Customer:
    def __init__(self, cust_id,name, age, wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.wallet_balance=wallet_balance
    def update_balance(self,amount):
        if amount < 1000 and amount>0:
            self.wallet_balance += amount
    def show_balance(self):
        print("The balance is:",self.wallet_balance)
c1=Customer(100,"Gopal",24,1000)
c1.update_balance(500)
c1.show_balance() 
        
##private = if there is __ before instance variable
##public = if there is not any __ before variable
##getter and setter function used for to get and set the varibale
##self is not a keyword used for the locate the address

#Example6
class Customer:
    def __init__(self, cust_id,name, age, wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance
    def set_balance(self,amount):
        if amount < 1000 and amount>0:
            self.__wallet_balance += amount
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100,"Gopal",24,1000)
print(c1.get_wallet_balance())
c1.set_balance(50000)
print(c1.get_wallet_balance())  

#Example7
class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("Dam length",dam1.get_length())  

#Example8
class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(False,True)
print(rate)   


#Example9
class Table:
    def __init__(self):
        print(id(self))
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(dining_table,back_table,front_table)
print(dining_table,back_table,front_table)



###############################################
#Program number1 
import sys
def nearest_palindrome():
    num=int(input())
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
print(nearest_palindrome())  

##program number2
def hospital(patient_medical_list,specialitiesss):
    max_visit=0
    P=patient_medical_list.count("P")
    E=patient_medical_list.count("E")
    O=patient_medical_list.count("O")
    if P>E and P>O:
        specility=specialities["P"]
    elif E>O:
        specility=specialities["E"]
    else:
        specility=specialities["O"]
    return specility
specialities={"P":"Peditrics","O":"Orthopedics","E":"Ent"}
patient_medical_list=[300,"P",302,"O",403,"E",401,"P",308,"P"]
specility=hospital(patient_medical_list,specialities)
print(specility)  

#program number3
str1=input()
str2=input()
for i in str1:
    for j in str2:
        if i==j:
            print(j,end="")


n=list(set(str1)and set(str2))
for i in n:
    print(i,end="")     






        
        




        
        
    
    
