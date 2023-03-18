a = int(input("Enter the number"))
if(a%3==0 and a%5==0):
 print("number is mul of both")
elif(a%5==0):
 print("number is mul of 5")
elif(a % 3 == 0):
 print("number is mul of 3")
else:
 print("Invaid") 


#print number 1 to 100
for i in range(1,100):
    print(i)

#print number 1 to 100
#print odd and even bet 1 to 100
for i in range(1,101):
    print(i,end=" ")
print()
for i in range(0,101,2):  #even
    print(i,end=" ")
print()
for i in range(0,101,3): #odd
    print(i,end=" ")
print()
for i in range(100,0,-1):
    print(i,end=" ")
print()

#break
for i in range(0,100):
    if(i==50):
        break
    else:
        print(i) 

#continue
for i in range(0,100):
    if(i==50):
        continue
    else:
        print(i) 

#pass
for i in range(0,100):
    if(i==50):
        pass
    else:
        print(i) 

#Function
#parameter are send right to left when data is send to function
def function1():
    print("Its a function")
function1()
def function2(num1,num2):
    print(num1,num2)
function2(10,20)
def fun3(num1,num2):
    num3=num1+num2
    return num3
print("output is",fun3(20,40))
print("output is",fun3(20,40.5))
print("output is",fun3('20',40))

#Positional arguments
def fun4(num1,num2,num3,num4):
    print(num1,num2,num3,num4)
fun4(20,30,40,50)
fun4(40,50,50)
fun4(20,30,40,50,80) 

#Keyword arguments
def fun5(num1,num2,num3,num4):
    print(num1,num2,num3,num4)
fun5(num4=20,num3=30,num2=40,num1=50)
fun5(num4=20,num3=20,num2=40,num1=50)

#default argument
def fun6(name,rollno,branch="cse",clgname="giet"):
    print(name,rollno,branch,clgname)
fun6("simran",79,)
fun6("Trupti",244,)
fun6("Bhaw",24,"cst")
fun6("Abhi",24,"cst") 

#Variable
def fun7(*var):  #n number of parameter
    for i in var:
        print(i,end=' ')
fun7(20,30,50)
print()
fun7(20,30,40,50)
print() 

def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
    return sum1
print(add(10,20))
print(add(10,20,30)) 

########################################

#program number1
a=int(input())
b=int(input())
c=int(input())
if(c==7):
    print(-1)
elif(b==7):
    print(c)
elif(a==7):
    print(b*c)
else:
    print(a*b*c) 

#program number2
country=input()
inramount=int(input())
if(country=="Europe"):
    print(inramount*0.01417)
elif(country=="British"):
    print(inramount*0.0100)
elif(country=="Austrilian"):
    print(inramount*0.02140)
elif(country=="Canadian"):
    print(inramount*0.02027)
else:
    print(-1) 

#program number3
c=int(input())
a=int(input())
total1=((a*37550)+(12516.6*c))
total2=total1*0.07
total3=total1+total2
ticketcost=(total3-(total3*0.1))
print(ticketcost) '''



