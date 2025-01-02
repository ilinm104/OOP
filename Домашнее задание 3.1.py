# Задание № 3.1. Атрибуты и взаимодействие классов

class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_rating(self):
        rating = []
        for values in self.grades.values():
            for value in values:
                rating.append(value)
                self.average = sum(rating) / len(rating)
        return self.average

    def __str__(self):
        a = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        b = f'Средняя оценка за домашние задания: {self.average} \n'
        c = f'Курсы в процессе изучения: {self.courses_in_progress[0]}, {self.courses_in_progress[1]}\n'
        d = f'Завершенные курсы: {self.finished_courses[0]}'
        return a + b + c + d
        
class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_to_lecturer = {}

    def rate_hw(self, student):
        if isinstance(student, Student):
            self.grades_to_lecturer =student.grades.copy()
        else:
            return 'Ошибка'

    def average_rating(self):
        rating = []
        for values in self.grades_to_lecturer.values():
            for value in values:
                rating.append(value)
                self.average = sum(rating) / len(rating)
        return self.average
    
    def __str__(self):
        a = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        b = f'Средняя оценка за лекции: {self.average}'
        return a + b


class Reviewer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

# Данные первого студенка
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses = ['Введение в программирование']

# Данные первого проверяющего
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Git']

# Данные первого лектора
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Git', 10)

lecturers = Lecturer('Some', 'Buddy')
lecturers.rate_hw(best_student)

some_reviewer = cool_mentor.__str__()
av_lec = lecturers.average_rating()
some_lecturer = lecturers.__str__()
best_student.average_rating()
some_student = best_student.__str__()


print(some_reviewer)
print('\n')
print(some_lecturer)
print('\n')
print(some_student)





        
