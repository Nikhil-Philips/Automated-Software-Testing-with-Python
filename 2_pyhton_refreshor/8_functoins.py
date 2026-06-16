def hello():
    print("Hello!")
hello()

# Important concept : shadowing a global var in local
x = 10
def add_func():
    a=int(input("Enter a number:"))
    #x=x+a #this line is wrong
    # x is not the global variable
    y=x+a
    print(y)
add_func()

def add(x,y):
    print(x+y)
add(5,6)