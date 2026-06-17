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
student1 = Student("Nikhil",(90,90,93,90,91))
student2 = Student("Ankit",(90,90,93,90,91))
student1.display()
student2.display()
print(str(student1))
print(student1)
print(student1.__str__())