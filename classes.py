from datetime import date


def calculateAge(birthDate):
    today = date.today()
    age = (today.year - birthDate.year -
           ((today.month, today.day) <
            (birthDate.month, birthDate.day)))

    return age


class Person:

    def __init__(self, first_name, last_name, id, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.birthday = birthday

    @property
    def get_basic_info(self):
        return f'''
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Age: {calculateAge(self.birthday)}
        '''


class Employee(Person):

    def __init__(self, first_name, last_name, id, birthday,
                 employees_id, contract_start_date, salary, job_tittle):
        super().__init__(first_name, last_name, id, birthday)
        self.employees_id = employees_id
        self.contract_start_date = contract_start_date
        self.salary = salary
        self.job_tittle = job_tittle

    @property
    def get_employee_info(self):
        super().get_info
        return f'''
        Job Title: {self.job_tittle}
        Salary: {self.salary}
        Years of service: {calculateAge(self.contract_start_date)}
        '''

    def change_salary(self, new_salary):
        self.salary = new_salary


class Teacher(Employee, Person):

    def __init__(self, first_name, last_name, id, birthday,
                 employees_id, contract_start_date, salary,
                 teacher_id, field_of_study):
        super().__init__(first_name, last_name, id, birthday,
                         employees_id, contract_start_date, salary)
        self.job_tittle = 'Teacher'
        self.teacher_id = teacher_id
        self.field_of_study = field_of_study

    @property
    def get_teacher_info(self):
        super().get_employee_info
        return f'''
        Field of study: {self.field_of_study}
        '''


class Student(Person):
    def __init__(self, first_name, last_name, id, birthday,
                 number_of_terms, number_of_units, gpa):
        super().__init__(first_name, last_name, id, birthday)
        self.number_of_terms = number_of_terms
        self.number_of_units = number_of_units
        self.gpa = gpa

    @property
    def get_student_info(self):
        super().get_basic_info
        return f'''
        Number of terms: {self.number_of_terms}
        Number of units: {self.number_of_units}
        GPA: {self.gpa}'''


class Course:
    def __init__(self, course_title, course_id, type):
        self.course_title = course_title
        self.course_id = course_id
        self.type = type
