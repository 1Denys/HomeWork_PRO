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
