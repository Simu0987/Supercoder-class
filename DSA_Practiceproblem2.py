

########Problem Number1
#l1=[11,8,23,7,25,15]
#l2=[6,33,50,31,46,78,16,34]
#double=[8,23,25]
#without creating result node
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
        
    def double_check(self):
        start=self.headval
        while(start is not None):
            inlist=list2.headval
            while(inlist is not None):
                if(start.dataval*2 == inlist.dataval):
                    print(start.dataval)
                    break
                else:
                    inlist=inlist.nextval
            start=start.nextval
#list1
list1=Slinkedlist()
list1.headval=Node(11)
e1=Node(8)
e2=Node(23)
e3=Node(7)
e4=Node(25)
e5=Node(15)
#linking the list
list1.headval.nextval=e1
e1.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
#list2
list2=Slinkedlist()
list2.headval=Node(6)
f1=Node(33)
f2=Node(50)
f3=Node(31)
f4=Node(46)
f5=Node(78)
f6=Node(16)
f7=Node(34)
#linking the list
list2.headval.nextval=f1
f1.nextval=f2
f2.nextval=f3
f3.nextval=f4
f4.nextval=f5
f5.nextval=f6
f6.nextval=f7
print("first list is")
list1.listprint()
print("second list is")
list2.listprint()
print("The list of double is")
list1.double_check()


#######Problem Number2
#A,n,*,/,a,p,p,l,e,*,a,/,d,a,y,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,r,*,a,w,a,y
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    def joining(self):
        str1=""
        start=self.headval
        while(start is not None):
            if(start.dataval =='*' or start.dataval == '/'):
                if(start.nextval.dataval=='*' or start.nextval.dataval=='/'):
                    str1+=" "
                    str1+=(start.nextval.nextval.dataval).upper()
                    start=start.nextval.nextval.nextval
                else:
                    str1+=" "
                    start=start.nextval
            else:
                str1+=start.dataval
                start=start.nextval
        return str1
list1=Slinkedlist()
list1.headval=Node('A')
e1=Node('n')
e3=Node('*')
e4=Node('/')
e5=Node('a')
e6=Node('p')
e7=Node('p')
e8=Node('l')
e9=Node('e')
e10=Node('*')
e11=Node('a')
e12=Node('/')
e13=Node('d')
e14=Node('a')
e15=Node('y')
e16=Node('*')
e17=Node('*')
e18=Node('k')
e19=Node('e')
e20=Node('e')
e21=Node('p')
e22=Node('s')
e23=Node('/')
e24=Node('*')
e25=Node('a')
e26=Node('/')
e27=Node('/')
e28=Node('d')
e29=Node('o')
e30=Node('c')
e31=Node('t')
e32=Node('o')
e33=Node('r')
e34=Node('*')
e35=Node('a')
e36=Node('w')
e37=Node('a')
e38=Node('y')
#linking the list
list1.headval.nextval=e1
e1.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=e8
e8.nextval=e9
e9.nextval=e10
e10.nextval=e11
e11.nextval=e12
e12.nextval=e13
e13.nextval=e14
e14.nextval=e15
e15.nextval=e16
e16.nextval=e17
e17.nextval=e18
e18.nextval=e19
e19.nextval=e20
e20.nextval=e21
e21.nextval=e22
e22.nextval=e23
e23.nextval=e24
e24.nextval=e25
e25.nextval=e26
e26.nextval=e27
e27.nextval=e28
e28.nextval=e29
e29.nextval=e30
e30.nextval=e31
e31.nextval=e32
e32.nextval=e33
e33.nextval=e34
e34.nextval=e35
e35.nextval=e36
e36.nextval=e37
e37.nextval=e38
print(list1.joining())

