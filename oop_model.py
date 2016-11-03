from abc import abstractclassmethod


# Class person is the base class
class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    # Print Person object in a readable format
    def __str__(self):
        return """Name: {0} Phone: {1} """.format(self.name, self.phone)


class Student(Person):
    def __init__(self, reg_number, *args, **kwargs):
        self.reg_number = reg_number
        self.course = []
        self.grades = []
        self.program = None
        super().__init__(*args, **kwargs)

    @abstractclassmethod
    def add_course_grade(self, course, grade):
        # this method must be implemented in all inheriting objects
        pass

    @property
    def enroll(self, program):
        self.program = program
        return self

    def is_enrolled(self):
        if self.enroll is not None:
            return "Enrolled in :", self.enroll


class PartTimeStudent(Student):
    def __init__(self, student_type, *args, **kwargs):
        self.class_days = []
        self.student_type = student_type
        super().__init__(*args, **kwargs)

    def add_course_grade(self, course, grade):
        self.course.append(course)
        self.grades.append(grade)

    def student_type(self):
        return self.student_type


class Employee(Person):
    def __init__(self, employee_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.employee_number = employee_number


class Lecturer(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.faculties = []

    def add_faculty(self, faculty):
        self.faculties.append(faculty)


class Staff(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.departments = []
        self.staff_ranks = []

    # Add staff to department
    def add_department(self, department):
        self.department.append(department)

    # Add Staff ranks
    def add_faculty(self, level):
        self.staff_ranks.append(level)


student = Student("sam", "1223445", "f3333")
print(student)
print(student.is_enrolled())

