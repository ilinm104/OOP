# Задание № 2. Атрибуты и взаимодействие классов

class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        
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


class Reviewer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

lecturers = Lecturer('Some', 'Buddy')
lecturers.rate_hw(best_student)
 
print(lecturers.grades_to_lecturer)
        
