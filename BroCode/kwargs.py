#Kwargs
def hello (**kwargs):
    print('Hello',end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title='Mr.',fname='Atul',mname='kumar',lname='Swain')