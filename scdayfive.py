
###DAY 5
#Program number1
class Vehicles:
    def __init__(self,vehicle_id,vec_type,cost):
        self.__vehicle_id=vehicle_id
        self.__vec_type=vec_type
        self.__cost=cost
    def purchase(self):
        if self.__vec_type=="Two wheeler":
            amount = 0.02*self.__cost
        elif self.__vec_type=="Four wheeler":
            amount = 0.06*self.__cost
        print("Vehicles type:",self.__vec_type,  "Vehicles cost:",self.__cost,  "Vehicles id:",self.__vehicle_id)
        print("Premium amount:",amount)
vehicle1=Vehicles("Bike","Two wheeler",32000)
vehicle2=Vehicles("Tesla","Four wheeler",8804000)
amount=vehicle1.purchase()
amount=vehicle2.purchase()  


#Program number2
class Student:
    def __init__(self,student_id,marks,age):
        self.__student_id=student_id
        self.__marks=marks
        self.__age=age
    def validate_age(self):
        if self.__age > 20:
            print("True")
        else:
            print("False")
    def validate_marks(self):
        if self.__marks > 0 and self.__marks < 100:
            print("True")
    def check_qualification(self,courseid,fees):
        self.__fees=fees
        self.__courseid=courseid
        if self.__age >20 and self.__marks >= 65:
            print("True")
            if self.__marks >85:
                self.__fees = self.__fees-(self.__fees*0.25)
                print(self.__fees)
                print(self.__courseid)
            else:
                print(self.__fees)
                print(self.__courseid)
        else:
            print("False")
        #print("Student id:",self.__student_id, "Marks:",self.__marks, "Age:",self.__age)
student1=Student(244,90,22)
student1.check_qualification(1002,15500) '''


#Program number3
class Customer:
    def validate_quantity(self,pizza_no):
        self.__pizza_no=pizza_no
        if self.__pizza_no <= 5 and self.__pizza_no >= 1:
            print("true")
        else:
            print("false")
class Pizzaservice:
    def validate_pizza_type(self,pizzatype):
        self.__pizzatype=pizzatype
        if self.__pizzatype end
        



        
        




        
        
    
    
