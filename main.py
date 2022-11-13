from Person import Person
from Student import Student
from Group import Group

x1 = Person('Petro', 'Petrow')
x_1 = Student('Peter', 'Petrow', '05.05.2000')
x_2 = Student('Peter', 'Petrow2', '05.05.2000')
g1 = Group('Python')
g1.add_students(x_1)
g1.add_students(x_2)
print(x1)
print(x_1)
print(g1)
