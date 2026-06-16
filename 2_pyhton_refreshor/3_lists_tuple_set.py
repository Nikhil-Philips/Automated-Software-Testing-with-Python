l = ["apple", "banana", "cherry"]
t = ("apple", "banana", "cherry")
s = {"apple", "banana", "cherry"}
# indexing is allowed in list, tuple but not in set
# tuple is immutable list is mutable
l.append("mango")
l.remove("banana")
s.add("mango")
print(l)
print(t)
print(s)