def hello(fname,lname,age):
    print("Hello", fname,lname, "of age", age)
    print("Have a nice day")

#hello("Atul","Swain",26)

def multiply(num1,num2):
    return num1*num2

x=multiply(23,3)
print(x)

#key word arg:
def hello(fname,lname,age):
    print("Hello", fname,lname, "of age", age)
    print("Have a nice day")

#hello(fname="Atul",age=26,lname="Swain")

#nested function call
print(round(abs(float(input("Enter a whole positive nnumber: ")))))