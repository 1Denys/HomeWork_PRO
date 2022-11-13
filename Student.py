class Student(Person):

    def __init__(self, name, surname, date_of_birth):
        super().__init__(name, surname)
        self.date_of_birth = date_of_birth
