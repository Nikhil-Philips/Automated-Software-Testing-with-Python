friends_age = { "Trishank":22, "Puneet":22, "Vinayak":27}
print(friends_age["Vinayak"])
print(friends_age)
# list of dictioanries
friends = [
    {"name":"Trishank","age":22},
    {"name":"Puneet","age":22},
    {"name":"Vinayak","age":27}
]
print(friends[1]["name"])
for friend,age in friends_age.items():
    print(f"{friend} age is {age}")
if "Vinayak" in friends_age :
    print("Vinayak is a friend")
total_age = friends_age.values()
print(f"avg age is sum(total_age)/len(total_age))