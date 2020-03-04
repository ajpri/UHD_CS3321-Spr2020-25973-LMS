import random
class Person:
    def __init__(self, fname, lname):
        self.__first_name = fname
        self.__last_name = lname

    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, fname):
        self.__first_name = fname
    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, lname):
        self.__last_name = lname
    def get_name(self):
        return self.get_first_name() + " " + self.get_last_name()

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname):
        self.__student_degree = ""
        self.__student_GPA = ""

    def get_student_degree(self):
        return self.__student_degree
    def set_student_degree(self, degree):
        self.__student_degree = degree
    def get_student_GPA(self):
        return self.__student_GPA
    def set_student_GPA(self, gpa):
        self.__student_GPA = gpa
    def get_student_info(self):
        return self.get_name() + "," + self.get_student_degree() + "," + self.get_stundent_GPA()
    
class Faculty(Employee):
    def __init__(self,firstname,lastname):
        super().__init__(firstname,lastname)
        self.__department = ''
        self.__specialization = ''
    def get_department(self):
        return self.__department
    def set_department(self,dept):
        self.__department = dept
    def get_specialization(self):
        return self.__specilization
    def set_specialization(self,sp):
        self.__specialization = sp
    def calculate_bonus(self):
        return self.get_emp_salary() * 0.20 + 1000.00
