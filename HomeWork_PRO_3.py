class Student:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    def __str__(self):
        return f"{self.surname} {self.name[0]}."

class Group:
    def __init__(self, title, limitStud = 10):
        self.title = title
        self.limitStud = limitStud
        self.__students = []

    def add_Students(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError('Student must be in class Student')
        if student in self.__students:
            raise ValueError('Student in group')
        if len(self.__students) >=self.limitStud:
            raise GroupLimitError(f'Limit is {self.limitStud}')

        self.__students.append(student)

    def __str__(self):
        return f'{self.title}\n' + '\n'.join(map(str, self.__students))

class GroupLimitError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f'{self.message}'

if __name__ == '__main__':

    students = [ Student('Petrov', 'Peter'),
                 Student('Petrov', 'Peter'),
                 Student('Petrov', 'Peter'),
                 Student('Petrov', 'Peter'),
                ]
    group = Group('Python PRO', limitStud=7)

    for item in students:
        try:
            group.add_Students(item)
        except Exception as ex:
            print(item, ex)
    print(group)


