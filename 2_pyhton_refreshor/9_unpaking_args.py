def multiply(*args):
    total = 1
    for arg in args:
        total*=arg
    print(total)
multiply(1,2,3,4,5,6)
sequence = [2,4,3,5]
multiply(*sequence)

def add(x,y):
    return x+y
nums={"x":5,"y":8}
print(add(nums["x"],nums["y"]))
# very importantoo
print(add(**nums))