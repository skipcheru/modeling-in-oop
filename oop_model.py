
class Person(object):
    """
    Information about a Person. More general including name, email and address
    """
    def __init__(self, name, phone, email, address):
        """Create a Person with above attributes"""
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        """Return a readable format of a Person"""
        return """Name: {0} Phone: {1} Email: {2}  Address: {3} """\
            .format(self.name, self.phone, self.email, self.address)


class Student(Person):

    def __init__(self, name, phone, email, address, reg_number, course, fee_balance):

        super.__init__(name, phone, email, address)
        self.reg_number = reg_number
        self.course = course
        self.fee_balance = fee_balance

    def course(self):
        return self.course

    def is_enrolled(self):
        """ Implement enroll for a course here"""

class PartTimeStudent(Student):
    def __init__(self, name, phone, email, address, reg_number, course, class_days):
        super.__init__(name, phone, email, address, reg_number, course)
        self.class_days = class_days[:]

    def days_for_class(self):
        return self.class_days

"""Multiple Inheritance here"""

class Employee(Person):
    def __init__(self, name, phone, email, address, employee_number):

        super.__init__(name, phone, email, address)
        self.employee_number = employee_number


class Lecturer(Employee):
    def __init__(self, name, phone, email, address, employee_number, faculty, rank):

        super.__init__(name, phone, email, address, employee_number)
        self.faculty = faculty
        self.rank = rank


class Staff(Employee):
    def __init__(self, name, phone, email, address, employee_number, department):

        super.__init__(name, phone, email, address, employee_number)
        self.department = department

    def grade(self):
        """Implement employee grade here"""

