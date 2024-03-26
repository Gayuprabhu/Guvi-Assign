#Task 4
#1. Create a program class called circle with constructor which will take a list as an argument for the task.
#declare list oustide the class
list=[10,501,22,37,100,999,87,351]
#create a class with name circle
class Circle():
    #instance atributes
    def __init__(self,list):
       self.list=list
#create object for class and pass the list as agrument
cir=Circle(list)
cir.list

#2.Create proper member variables inside the task if required and use them when necessary.
class Circle():
 a=5
 def __privatemath(self):
   print("I am inside class circle")
 def hello(self):
  print("Private variable",Circle.a)
boa=Circle()
boa.hello()

#3.From the given List create two class Methods Area and Perimeter which will be going to calculate the Area
#create class circle
class circle():
    def __init__(self,radius):
        self.radius=radius
        #create method for area and return the area result
    def area(self):
        return self.radius**3.141
       #create method for perimeter and return the  result
    def perimeter(self):
        return 2*self.radius**3.141
    #create obj for circle class and pass the radius
obj=circle(7) 
#print the area and perimeter by calling the methods
print("area of circle",obj.area() )
print("perimetre is ",obj.perimeter() )   