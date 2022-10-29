class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name}'

class Student(Person):

    def __init__(self, name, surname, date_of_birth):
        super().__init__(name, surname)
        self.date_of_birth = date_of_birth

class Group:

    def __init__(self, title, max_students = 10):
        self.title = title
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students and student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def search(self, surname):
        res = []
        for item in self.students:
            if item.surname == surname:
                res.append(item)
        return res
    def __str__(self):
        return f'{self.title}\n\t' + '\n\t'.join(map(str, self.students))

x_1 = Student('Peter', 'Petrow', '05.05.2000')
x_2 = Student('Peter', 'Petrow2', '05.05.2000')
x_3 = Student('Peter', 'Petrow3', '05.05.2000')
x_4 = Student('Peter', 'Petrow4', '05.05.2000')

z = Group('Python')
z.add_students(x_1)
z.add_students(x_2)
z.add_students(x_3)
z.add_students(x_4)

print(z)
