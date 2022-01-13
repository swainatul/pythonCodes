name = "Atul" # global scope
def display_name():
    name= "code" #local variable and only available inside this function
    #print(name)
display_name()
#print(name)

#arguments

def add(*args):
    sum=0
    for i in args:
        print(i)
        sum+=i
    return sum
print(add(1,4,5,6,7,4))