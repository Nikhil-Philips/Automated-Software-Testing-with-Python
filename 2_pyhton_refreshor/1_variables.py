x = 15
price = 9.99
discount = 0.2
result = price * (1 - discount)
print(result)
name = "Nikhil"
print(name * 3)
greeting = f"Hello {name}"
name = "Vinayak"
print(f"Hello {name}")
print(greeting)

# template
greet = "Hello, {}"
# string using template
with_name = greet.format("Raj")
print(with_name)

# taking input
name = input("Enter your name: ")
number = int(input("Enter any number: "))
ans = number / 10.8
print(f"{ans:.3f}")