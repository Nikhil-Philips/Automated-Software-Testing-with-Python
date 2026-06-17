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

# Lambda functions
sub = lambda x,y :x-y
print(sub(5,6))

# important
def double(n):
    return n*2
sequence = [1,2,3,4,5]
doubled1 =  list(map(double,sequence))
doubled2 = [ double(x) for x in sequence]
doubled3 = [(lambda x : x*2)(x) for x in sequence]
doubled4 = list(map(lambda x:x*2,sequence))
