# QUESTION 1

def triple(text):
    new_text = ''
    for letter in text:
        new_text += letter*3
    return new_text
# QUESTION 2
text = input('Enter a sentence: ')
print('Triple effect: '+triple(text))

# QUESTION 3

def next_number(num):
    if (num % 2 == 0):  # if even
        next_num = 3*num + 1
    else:
        next_num = 2*num + 2
    return next_num

# QUESTION 4
num = int(input('Enter the initial number: '))
print('Sequence: ')
i = 0
while num < 1000000:
    print('Step {0}: {1}'.format(i, num))
    num = next_number(num)
    i += 1
# '... this goes until the number becomes greater than i million then stops..'

# QUESTION 5
class Employee(object):
    """docstring for Employee"""
    def __init__(self, first_name, last_name, em_num, position, phone_ext):
        self.first_name = first_name
        self.last_name = last_name
        self.em_num = em_num
        self.position = position
        self.phone_ext = phone_ext

    # QUESTION 7
    def __str__(self):
        return 'Employee({},{},{},{},{})'.format(
            self.em_num,
            self.first_name,
            self.last_name,
            self.position,
            self.phone_ext)

    # QUESTION 9
    def __repr__(self):
        return '{} {} [{}] is a {}. Owl name: {}'.format(self.first_name, self.last_name,
                                                         self.em_num, self.position, self.phone_ext)

    # QUESTION 10
    def print_details(self):
        # Something extra!: the character that comes between : and < or > or ^ is used to fill the space instead
        print('{:->24}'.format('E '+ self.em_num+'--'))
        print('| {:<20} |'.format(self.first_name + ' ' + self.last_name))
        print('| {:<20} |'.format(self.position))
        print('| {:<20} |'.format(self.phone_ext))
        print('-'*24)

    # QUESTION 11
    @staticmethod
    def real_world_example():
        employee = Employee('Lim','Daniel','0101013QCT', 'SIM STAFF', '9123456')
        return employee



# QUESTION 5
em1 = Employee('Harry','Potter','0000001','Seeker','Hegwig')
em2 = Employee('Oliver','Wood','0000002','Keeper','Bludger')
em3 = Employee('George','Weasley','0000003','Beater','Errol ')
em4 = Employee('Fred','Weasley','0000004','Beater','Errol ')
em5 = Employee('Ginny','Weasley','0000005','Chaser','Pigwidgeon')

print(em1)  # QUESTION 6 & 8
# before you added the dunder method __str__
# prints <__main__.Employee object at 0x1234567890ABCDEF> 
# after adding the dunder method __str__
# prints Employee(0000001,Harry,Potter,Seeker,Hegwig)
print(em2)
print(em3)
print(em4)
print(em5)

# QUESTION 9 
print(repr(em1))
# Question 10
em1.print_details()
em2.print_details()
em3.print_details()
em4.print_details()
em5.print_details()

# QUESTION 12 - solution available on the site

# QUESTION 13
class Course():
    def __init__(self, description, course_code, credits):
        self.description = description
        self.course_code = course_code
        self.credits = credits

class Department():
    def __init__(self, name, department_code, courses = None):
        self.name = name
        self.department_code = department_code
        self.courses = courses
        if self.courses is None:
            self.courses = {}

    def add_course(self, description, course_code, credits):
        new_course = Course(description,course_code,credits)
        self.courses[course_code] = new_course
        return new_course

class Student():
    def __init__(self, name, student_num, modules=None):
        self.name = name
        self.student_number = student_num
        self.modules = modules
        if self.modules is None:
            self.modules = []

    def enrol(self, course):
        self.modules.append(course)

csit_dept = Department("Computer Science and Information Technology", "CSIT")
csit110 = csit_dept.add_course("Fundamental Programming with Python", "CSIT110", 6)
gunther = Student("Gunther", "Tan")
gunther.enrol(csit110)
for course in gunther.modules:
    print(course.description)
# or
# [print(i.description) for i in gunther.modules]