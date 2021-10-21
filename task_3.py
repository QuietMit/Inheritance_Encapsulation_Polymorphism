# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print("Задача №3")
print()

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lect_rate(self, lecturer, course, lec_grade):
        if isinstance (lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [lec_grade]
            else:
                lecturer.grades[course] = [lec_grade]
        else:
            return print('Ошибка')
        
    def avg_grade(self):
        grade_list = list(self.grades.items()) 
        for tuple in grade_list:
            grade = 0
            for key, value in grade_list:
                grade += sum(value)/len(value) 
            grade = round(grade/len(grade_list), 1)
        return grade

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade()}\nKурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершённые курсы: Введение в программирование'
        
    def __gt__(self, other):
        if not isinstance(other, Student):
            return f'{other.name} {other.surname} is not a student!'
        if self.avg_grade() > other.avg_grade():
            return f'{self.name} {self.surname} победил по среднему баллу {other.name} {other.surname}'    
        else:
            return f'{self.name} {self.surname} проиграл по среднему баллу {other.name} {other.surname}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        
    def avg_grade(self):
        grade_list = list(self.grades.items()) 
        for tuple in grade_list:
            grade = 0
            for key, value in grade_list:
                grade += sum(value)/len(value) 
            grade = round(grade/len(grade_list), 1)
        return grade

    
class Lecturer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}'
        

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return f'{other.name} {other.surname} is not a Lecturer!'
        if self.avg_grade() > other.avg_grade():
            return f'{self.name} {self.surname} победил по среднему баллу {other.name} {other.surname}'    
        else:
            return f'{self.name} {self.surname} проиграл по среднему баллу {other.name} {other.surname}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка')

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
        


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
# best_student.courses_in_progress += ['Git']
new_student = Student('Richard', 'o`Neil', 'male')
new_studentess = Student('Lisa', 'Doherty', 'female')
new_student.courses_in_progress += ['Python']
new_studentess.courses_in_progress += ['Python']
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python'] 
check_person = Reviewer('Bill', 'Johnes')
new_reviewer = Reviewer('Darya', 'Alekseeva')
check_person.courses_attached = ['Python']
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
another_lecturer = Lecturer('Barry', 'Wyler')
another_lecturer.courses_attached += ['Python']
new_teacher = Lecturer('Ivan', 'Popov')
new_teacher.courses_attached += ['Python']
new_student.lect_rate(another_lecturer, 'Python', 10)
new_studentess.lect_rate(another_lecturer, 'Python', 10)
best_student.lect_rate(another_lecturer, 'Python', 10)
new_student.lect_rate(new_teacher, 'Python', 10)
new_studentess.lect_rate(new_teacher, 'Python', 10)
best_student.lect_rate(new_teacher, 'Python', 9)
new_student.lect_rate(some_lecturer, 'Python', 10)
new_studentess.lect_rate(some_lecturer, 'Python', 10)
best_student.lect_rate(some_lecturer, 'Python', 10)
new_student.lect_rate(some_lecturer, 'Python', 10)
new_studentess.lect_rate(some_lecturer, 'Python', 10)
best_student.lect_rate(some_lecturer, 'Python', 9)
new_student.lect_rate(some_lecturer, 'Python', 10)
new_studentess.lect_rate(some_lecturer, 'Python', 10)
new_student.lect_rate(some_lecturer, 'Python', 10)
new_studentess.lect_rate(some_lecturer, 'Python', 10)
check_person.rate_hw(best_student, 'Python', 10)
check_person.rate_hw(best_student, 'Python', 10)
check_person.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
check_person.rate_hw(best_student, 'Python', 9)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
check_person.rate_hw(new_studentess, 'Python', 8)
check_person.rate_hw(new_student, 'Python', 10)
check_person.rate_hw(new_student, 'Python', 9)
check_person.rate_hw(new_student, 'Python', 10)
check_person.rate_hw(new_studentess, 'Python', 10)
check_person.rate_hw(new_studentess, 'Python', 10)

# print(another_lecturer.lec_grades)
# print(f'Личный рейтинг преподавателя {another_lecturer.name} {another_lecturer.surname} {another_lecturer.lec_grades}')
print(some_reviewer)
# print(check_person)
print()
print(some_lecturer)
# print(another_lecturer)
# print(new_teacher)
print()
print(best_student)
# print(best_student.grades)
# print()
# print(new_studentess)
print()
print(best_student > new_student)
print(new_studentess > new_student)
print()
print(another_lecturer > new_teacher)
print(new_teacher > new_reviewer)
print(new_teacher > another_lecturer)