from allclasses import Student, Course

fname = input("Enter the student first name :")
lname = input("Enter the student last name :")
degree = input("Enter the degree to register :")
c1 = input("Enter the course 1 to enroll :")
c2 = input("Enter the course 2 to enroll :")
c3 = input("Enter the course 3 to enroll :")
course1 = Course(c1)
course2 = Course(c2)
course3 = Course(c3)
courses = [course1,course2, course3]

student1 = Student(fname,lname)
student1.set_degree(degree)
student1.set_courses(courses)

course_list = student1.get_courses()
for course in course_list:
    print(" Course : ", course.get_name())

