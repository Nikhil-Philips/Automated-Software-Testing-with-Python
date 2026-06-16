numbers = [1,2,3,4,5,6,7,8,9,10]
double = [x * 2 for x in numbers]
triple = [x * 3 for x in numbers]
print(double)
print(triple)
friends = ["Aman" , "Aarav" , "Raj" , "Abhay" , "Vinayak"]
friends2 = ["Aman" , "Aarav" , "Raj" , "Abhay" , "Vinayak"]
start_s = [friend for friend in friends if friend.startswith("A")]
print(friends)
print(start_s)
print(friends is friends2)
print(friends[0] is friends2[0])
print("friends", id(friends), "friends2" , id(friends2))
print(friends == friends2)