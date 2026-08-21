class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def __str__(self):
        return f"Person {self.name}, grade: {self.grade}"
    def __repr__(self):
        return f"<Person {self.name}, grade: {self.grade}>"
    def average_grade(self):
        return sum(self.grade)/len(self.grade)
    def display(self):
        print(f"Average grade of {self.name} is: {self.average_grade()}")
    @classmethod
    def class_method(cls):
        print(f"Class method of {cls}")
    @staticmethod
    def static_method():
        print("Static method is called")
student1 = Student("Nikhil",(90,90,93,90,91))
student2 = Student("Ankit",(90,90,93,90,91))
student1.display()
student2.display()
# all three are same
print(str(student1))
print(student1)
print(student1.__str__())

Student.class_method()
Student.static_method()



# Create a class Book with two types of hardcover only
class Book:
    TYPES = ("hardcover","paperback")
    def __repr__(self):
        return f"<Book {self.name}, {self.weight} kg>"
    def __init__(self,name,book_type,weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    @classmethod
    def hardcover(cls,name,weight):
        return cls(name,cls.TYPES[0],weight+100)
    @classmethod
    def paperback(cls,name,weight):
        return cls(name,cls.TYPES[1],weight+10)
book1=Book.hardcover("Harry Potter",100)
book2=Book.paperback("Harry Potter",100)
print(book1)
print(book2)

