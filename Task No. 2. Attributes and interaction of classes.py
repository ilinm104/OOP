class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer:
    def __init__(self, name, surname, average_grade=0.0):
        self.name = name
        self.surname = surname
        self.average_grade = average_grade

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.average_grade:.1f}"
        )

class Student:
    def __init__(
        self,
        name,
        surname,
        average_hw_grade=0.0,
        courses_in_progress=[],
        finished_courses=[],
    ):
        self.name = name
        self.surname = surname
        self.average_hw_grade = average_hw_grade
        self.courses_in_progress = courses_in_progress
        self.finished_courses = finished_courses

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.average_hw_grade:.1f}\n"
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )

# Создаем объекты
reviewer = Reviewer("Some", "Buddy")
lecturer = Lecturer("Some", "Buddy", 9.9)
student = Student(
    "Ruoy", "Eman", 9.9, ["Python", "Git"], ["Introduction to Programming"]
)

# Выводим информацию об объектах
print(reviewer)
print()
print(lecturer)
print()
print(student)
