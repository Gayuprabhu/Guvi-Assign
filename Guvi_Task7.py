#Task 7
# program to create a file and write it 
def fun2():
  f=open(r"C:\Users\Gayu\Desktop\filenew\gayu.txt","a")
  f.write("Phyton Class start at 9:00 AM")
  f.close()
  fun2()

  #Program to read a file 
  def fun1():
    f=open(r"C:\Users\Gayu\Desktop\filenew\gayu.txt","r")
    f.read()
  fun1()