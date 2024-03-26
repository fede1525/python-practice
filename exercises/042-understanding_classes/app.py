class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  def introduce(self):
    return f"Hello! I am {self.name}, I am {self.age} years old, and my current grade is {self.grade}."

  def study(self, hours):
    self.grade += hours * 0.5
    return f"After studying for {hours} hours, {self.name}'s new grade is {self.grade}."

student1 = Student("Ana", 20, 80)
student2 = Student("Ben", 18, 90)

print(student1.introduce())
print(student1.study(3))

print(student2.introduce())
print(student2.study(2)) 

