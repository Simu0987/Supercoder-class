#Day3
#list comprehension
#for loop version
result=[]
for i in range(11):
    result.append(i)
print(result) 

###
print([i for i in range(11)]) 

#for loop version odd number
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)  
#OR 
print([i if i%2!=0 else i**2 for i in range(11)]) 

#for loop version even number
result=[]
for i in range(11):
    if i%2==0:
        result.append(i)
print(result) 
#OR
print([i for i in range(11) if i%2==0])

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for i in mat:
    for j in i:
        if j%2==0:
            result.append(j**3)     
    else:
        result.append(j**2)
print(result)
#OR
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
result.append([j**3 if j%2==0 else j**2 for j in i for i in mat])  

###2d
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for row in mat:
    row_data=[]
    for ele in row:
        if ele%2!=0:
            row_data.append(ele**2)
        else:
            row_data.append(ele**3)
    result.append(row_data)
print(result) 
#OR ####for 2d
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([[ele**2 if ele%2!=0 else ele**3 for ele in row]for row in mat])



#program number1
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result=[]
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)  
#OR
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
print([(i,mylist.index(i))for i in list_b])  

#program number2
#dictionary comprehention
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result={}
for i in list_b:
    result[i]=mylist.index(i)
print(result) 
#OR
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
print({i:mylist.index(i)for i in list_b}) 

#program number3
sentences=["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday","with our three lakh diya or earthen lamps","lit up simultaneously on the banks of the sarayu river"]
stopwords=["for","a","of","the","and","to","in","on","with"]
result=[]
for i in sentences:
    row_data=[]
    for j in i.split():
        if j not in stopwords:
            row_data.append(j)
    result.append(row_data)
print(result)  

#Program number4
array=list(map(int,input().split(",")))
num1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
num2=""
for i in l:
    num2+=str(i)
print(int(num2)+num1) 

#program number5
s=input().split(",")
stt=[]
num=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    num.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(num)):
    print(rotate(stt[i],num[i]))  '''


    


