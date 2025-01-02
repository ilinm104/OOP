# Задание № 4. Полевые испытания

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
            self.grades_to_lecturer = student.grades.copy()
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

# Данные первого студента
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

# Данные второго студента
best_student_2 = Student('Sara', 'Conor', 'female')
best_student_2.courses_in_progress += ['Python', 'Git', 'Java']
best_student_2.finished_courses = ['Введение в программирование']

# Данные первого проверяющего
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Git']

# Данные второго проверяющего
cool_mentor_2 = Reviewer('Kate', 'Rose')
cool_mentor_2.courses_attached += ['Python', 'Git', 'Java']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Git', 10)

cool_mentor_2.rate_hw(best_student_2, 'Python', 10)
cool_mentor_2.rate_hw(best_student_2, 'Git', 10)
cool_mentor_2.rate_hw(best_student_2, 'Python', 9)
cool_mentor_2.rate_hw(best_student_2, 'Git', 10)
cool_mentor_2.rate_hw(best_student_2, 'Java', 9)
cool_mentor_2.rate_hw(best_student_2, 'Java', 10)

# Данные первого лектора
lecturer = Lecturer('Some', 'Buddy')
lecturer.rate_hw(best_student)

# Данные второго лектора
lecturer_2 = Lecturer('Kate', 'Rose')
lecturer_2.rate_hw(best_student_2)

some_reviewer = cool_mentor.__str__()
av_lec = lecturer.average_rating()

lecturer_2.average_rating()

some_lecturer = lecturer.__str__()
best_student.average_rating()
some_student = best_student.__str__()

best_student_2.average_rating()

# ФУНКЦИЯ ДЛЯ ПОДСЧЕТА СРЕДНЕГО БАЛЛА ПО ВСЕМ СТУДЕНТАМ ПО КОНКТКРНОМУ КУРСУ

students = [best_student, best_student_2]

def stud(students):
    average_stud = {}
    for student in students:
        for key, value in student.grades.items():
            if key == key:
                average_stud[key] = sum(value) + sum(value) / len(students)
    return average_stud

print(stud(students))
         
# ФУНКЦИЯ ДЛЯ ПОДСЧЕТА СРЕДНЕГО БАЛЛА ЗА ВСЕ ЛЕКЦИИ ПО КОНКТКРНОМУ КУРСУ

lectors = [lecturer, lecturer_2]

def lect(lectors):
    average_lec = {}
    for lector in lectors:
        for key, value in lector.grades_to_lecturer.items():
            if key == key:
                #s = sum(lector.grades_to_lecturer[key].extend(lector.grades_to_lecturer[key]))
                average_lec[key] = sum(value) + sum(value) / len(lectors)
    return average_lec

print(lect(lectors))
                
