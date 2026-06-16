x = 5 , 11
print(x) # x is a tuple
y , z = x
print(y , z)
friends_age = { "Trishank":22, "Puneet":22, "Vinayak":27}
new = friends_age.items()
print(type(new))
print(list(friends_age.items()))
print(new)
# so this is destrucuring of tuple
for frnd,age in friends_age.items():
    print(age)

people = [("Bob",42,"Mechanic"),("James",24,"Artist"),("Harry",32,"Lecturer")]
for name,age,profession in people:
    print(f"Name is {name}, Age is {age}, Profession is {profession}")
name,_,profession = people[0]
print(profession)
*head , tail = [1,2,3,4,5]
print(head)
print(* head)#printing individual values
print(tail)
head,*tail = [1,2,3,4,5]
print(head)
print(tail)
print(*tail) #printing individual values
