#day2 program number1
def findletter():
    str1=input()
    dcount=0
    lcount=0
    for i in str1:
        if i.isalpha(): #to give the number of alphabet
            lcount=lcount+1
        elif i.isdigit():   #to give the number of digit
            dcount=dcount+1
        else:
            continue
    return [lcount,dcount]
print(findletter())   

#program number2
def find_pairs_of_length(lst,n):
    #n=input()
    #lst=[]
    pairs=0
    for i in range(1,len(lst)):
        for j in range(i+1,len(lst)):
            if i+j:
                pairs=pairs+1
            else:
                continue
    return pairs
lst=[1,2,7,4,5,6,0,3]
n=6
print(find_pairs_of_length(lst,n))

def find_pairs_of_length(numlist,n):
    count=0
    for x in numlist:
        index=numlist.index(x)+1
        for y in range(index,len(numlist)):
            if x+numlist[y]==n:
                count+=1
    return count
numlist=[1,2,7,4,5,6,0,3]
n=6
print(find_pairs_of_length(numlist,n)) 

#program number3
def fun3():
    str1=input()
    if len(str1)<2:
        return -1
    elif len(str1)==2:
        return str1+str1
    else:
        return str1[0:2]+str1[-2:]
print(fun3())  

#program number4
def fun4():
    str1=input()
    if len(str1)<3:
        return str1
    elif str1[-3:]=="ing":
        return str1+"ly"
    else:
        return str1+"ing"
print(fun4())  

#program number5
def check_double():
    number=int(input())
    num1=str(number*2)
    number=str(number)
    count=0
    for x in number:
        if x in num1:
            count+=1
        else:
            return False
    if count==len(number):
        return True
print(check_double())   

#program number6
def find_more_than_average():
    mark=0
    count=0
    for x in list_of_marks:
        marks+=x
    average=marks/len(list_of_marks)
    for x in list_of_marks:
        if x>average:
            count+=1
    percentage=(count+100)/len(list_of_marks)
    return percentage
print(find_more_than_average())
def generate_frequency():
    freq=[]
    global list_of_marks
    for x in range(26):
        count=0
        for y in list_of_marks:
            if x==y:
                count+=1
            freq.append(count)
    return freq
print(generate_frequency())
def sort_marks():
    global list_of_marks
    list_of_marks=sorted(list_of_marks)
    return list_of_marks
print(sort_marks())  

#program number7
def translate():
    list12=[]
    for i in list11:
        list12.append(dict11[i])
    return list12
dict11={"merry":"god","chirtmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
list11=["merry","chirtmas"]
print(translate()) 

#program number8
n1=int(input())
n2=int(input())
result=[]
array=[i for i in range(n1,n2+1)]
print(array)
for i in range(len(array)):
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)
c=0
for i in result:
    if sum(i)%2!=0:
        c+=1
print(c) 
