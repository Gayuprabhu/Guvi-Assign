#Task2
#1. Program to calculate the number of vowels


def Vowelcount (str):
 str="Guvi Geeks Network Private limited"
 #initate variable 
 count=0
 counti=0
 counto=0
 countu=0
 counte=0
 counttot=0
 #for loop
 for alpha in str:
     #if alpabet is present
     if (alpha=="a"):
         count=count+1
     if (alpha=="i"):
        counti=counti+1
     if (alpha=="e"):
        counte=counte+1
     if (alpha=="o"):
        counto=counto+1
     if (alpha=="u"):
        countu=countu+1 
     if (alpha=="a"or alpha=="i"or alpha=="e" or alpha=="o" or alpha=="u"):
        counttot=counttot+1
 print("No of vowels wise",count,counti,counto,countu) 
 print("No of vowels",counttot)
     
Vowelcount(str)

#Program 2
#pyramid
rows=20

#outer loop
for i in range(1,rows+1):
    #nested loop
    for j in range(1,i+1):
        print(j,end='')
#New line after each row
    print('')


#program 3
    #return a new string with vowels removed
str=input("Enter string") 
vowels="aieouAIEOU"
str1=""
for char in str:
    if char not in vowels:
        str1=str1+char
print("output string",str1)

#program4
# to count the unique characters 
s="GayathriPrabhu "
s1=""
for i in s:
    if i not in s1:
        s1 +=i
print(len(s1))

#Program5
#paldirome or not

def palidrome(string):
   reverse=''.join(reversed(string))
   if (string==reverse):
      return True
string="mom"
b=palidrome(string)
if(b):
   print("True")
else:
   print("False") 
#program6
   
 #program7
   #take a string and return most frquent character
   str="Gayathri"
#create 2 empty list
list1=[]
list2=[]
#iterate over the string
for i in str:
    if i not in  list1:
        list1.append(i) #append unique charac
        list2.append(str.count(i)) 
occ=max(list2)
a=list1[list2.index(occ)]
print("the frequent charcter",a) 

#program 8
#anagram
str1="earth"
str2="heart"
str1=sorted(str1.lower())
print("after sort string1",str1)
str2=sorted(str2.lower())
print("after str2 sort",str2)
#function
def anagram():
    if(str1==str2): #find both the sorted are same
        return True
    else:
        return False
print("is anagram",anagram()) #call the angram function

#program 9
#count the number of words
string="My name is Gayathri"
count =len(string.split())
print("The number of words",count)
    