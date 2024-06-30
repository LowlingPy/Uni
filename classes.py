from datetime import date, datetime


def calculate_age(date_time):
    today = date.today()
    age = (today.year - date_time.year - ((today.month, today.day) < (date_time.month, date_time.day)))
    return age


class Person:
    def __init__(self, first_name, last_name, id_, birthday, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id_
        self.birthday = birthday

    @property
    def get_basic_info(self):
        return f'''
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Age: {calculate_age(self.birthday)}
        '''


class Employee(Person):

    def __init__(
            self, first_name, last_name, id, birthday, employees_id, contract_start_date, salary, job_title, *args,
            **kwargs
    ):
        super().__init__(first_name, last_name, id_, birthday, *args, **kwargs)
        self.employees_id = employees_id
        self.contract_start_date = contract_start_date
        self.salary = salary
        self.job_title = job_title

    @property
    def get_employee_info(self):
        basic_info = super().get_basic_info
        return f'''
        {basic_info}
        Job Title: {self.job_title}
        Salary: {self.salary}
        Years of service: {calculate_age(self.contract_start_date)}
        '''

    def change_salary(self, new_salary):
        self.salary = new_salary


class Teacher(Employee):
    p_a_report = []
    teaching_time = []

    def __init__(
            self, first_name, last_name, id_, birthday, employees_id, contract_start_date, salary, teacher_id, 
            field_of_study, *args, **kwargs
    ):
        super().__init__(
            first_name, last_name, id_, birthday, employees_id, contract_start_date, salary, 'Teacher',
            *args, **kwargs
        )
        self.teacher_id = teacher_id
        self.field_of_study = field_of_study
        self.rate = 'not set'

    @property
    def get_teacher_info(self):
        employee_info = super().get_employee_info
        return f'''
        {employee_info}
        Field of Study: {self.field_of_study}
        Rate: {self.rate}
        '''

    def p_a_check(self, status):
        if status.lower() not in ['p', 'a']:
            raise ValueError("Status must be 'p' for present or 'a' for absent.")
        Teacher.p_a_report.append((datetime.now(), status))

    def rate_list(self, grades_list):
        if not grades_list:
            self.rate = 'no grades'
        else:
            average = sum(grades_list) / len(grades_list)
            self.rate = average

    def set_teaching_time(self, classes):
        for class_info in classes:
            if len(class_info) != 3:
                raise ValueError("Each class info must be a tuple of (title, class day, class time).")
            Teacher.teaching_time.append(class_info)


class Student(Person):
    p_a_report = []
    classes_time = []

    def __init__(self, first_name, last_name, id_, birthday, number_of_terms, number_of_units, gpa, *args, **kwargs):
        super().__init__(first_name, last_name, id_, birthday, *args, **kwargs)
        self.number_of_terms = number_of_terms
        self.number_of_units = number_of_units
        self.gpa = gpa

    @property
    def get_student_info(self):
        basic_info = super().get_basic_info
        return f'''
        {basic_info}
        Number of Terms: {self.number_of_terms}
        Number of Units: {self.number_of_units}
        GPA: {self.gpa}
        '''

    def p_a_check(self, status):
        if status.lower() not in ['p', 'a']:
            raise ValueError("Status must be 'p' for present or 'a' for absent.")
        Student.p_a_report.append((datetime.now(), status))

    def set_classes_time(self, classes):
        for class_info in classes:
            if len(class_info) != 3:
                raise ValueError("Each class info must be a tuple of (title, class day, class time).")
            Student.classes_time.append(class_info)


class Course:
    def __init__(self, course_title, course_id, type_, *args, **kwargs):
        self.course_title = course_title
        self.course_id = course_id
        self.type = type_


# Example usage
teacher = Teacher("John", "Doe", "123", date(1980, 5, 15), "T001", date(2010, 8, 1), 50000, "TEA123", "Mathematics")
teacher.p_a_check('p')
teacher.rate_list([85, 90, 78])
teacher.set_teaching_time([("Math 101", "Monday", "09:00 AM"), ("Math 102", "Wednesday", "11:00 AM")])
print(teacher.get_teacher_info)
print(teacher.p_a_report)
print(teacher.teaching_time)

student = Student("Jane", "Doe", "456", date(2000, 7, 20), 6, 120, 3.8)
student.p_a_check('a')
student.set_classes_time([("History 101", "Tuesday", "10:00 AM"), ("Biology 101", "Thursday", "01:00 PM")])
print(student.get_student_info)
print(student.p_a_report)
print(student.classes_time)
