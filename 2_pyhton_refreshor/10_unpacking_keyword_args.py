def name(**kwargs):
    print(kwargs)
def print_nicely(**kwargs): #packing
    # krawgs is a dictionary now
    name(**kwargs) #unpacking
    # they have passed two values to name function now
    for arg,value in kwargs.items():
        print(f"{arg}: {value}")
print_nicely(name="Bob",age=35)