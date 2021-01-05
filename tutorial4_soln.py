import copy

# QUESTION 1
def get_assessment_mark(assessment_name, mark_min, mark_max):
    assessment_mark = input('Enter {} mark ({}-{}): '.format(
    assessment_name, mark_min, mark_max))
    try:
        assessment_mark = int(assessment_mark)
    except ValueError as e:
        raise ValueError('Error: {} mark is invalid'.format(assessment_name))
    else:
        if (assessment_mark> mark_max) or (assessment_mark< mark_min):
            raise ValueError('{} mark must be betwwen {} and {}'.format(
            assessment_name,
            mark_min,
            mark_max))
        else:
            return assessment_mark
#QUESTION 2
done = False
assign = 0
project = 0
exam = 0
while not done:
    try:
        assign = get_assessment_mark("assignment", 0,20)
        project = get_assessment_mark("project", 0,30)
        exam = get_assessment_mark("final exam", 0,50)
    except Exception as e:
        print(e)
    else
        done = True
print('Total mark: {}'.format(assign+project+exam))

# Question 3
class Student():
    def __init__(self, name, student_num, modules=[]):
        self.name = name
        self.student_number = student_num
        self.modules = modules

    def enrol(self, course):
        self.modules.append(course)

    @classmethod
    def from_list(cls, input_list):
        output = []
        for each_item in input_list:
            student =  cls(each_item[0], each_item[1])
            output.append(student)
        return output
    
    @classmethod
    def from_dict(cls, input_dict):
        return cls(input_dict["name"], input_dict["student_number"])

    # Error in question. ignore this question
    def info(student_list):
        pass

    @staticmethod
    def greet():
        prints('Good Morning')
"""
# Examples of how to call the static or class method
list_of_students1 = Student.from_list([["John Snow", "135226"],["Peter Parker", "197439"]])
a_student = Student.from_dict({"name":"John Snow","student_number":"135226"})
Student.greet()  # prints 'Good Morning'
"""
# QUESTION 4
class CourseNotFoundError(Exception):
    def __init__(self, course, dpmt):
        self.course = course
        self.dpmt = dpmt
    def __str__(self):
        return 'The course {} is not provided by {}'.format(self.course, self.dpmt)

# QUESTION 5
class Department():
    def __init__(self, name, department_code, courses = {}):
        self.name = name
        self.department_code = department_code
        self.courses = courses

    def add_course(self, description, course_code, credits):
        new_course = Course(description,course_code,credits)
        self.courses[course_code] = new_course
        return new_course

    def find_course(self,course_code):
        if not course_code in self.courses.keys():
            raise CourseNotFoundError(course_code, self.name)
        else:
            return copy.deepcopy(self.courses[course_code])

try:
    csit_dept = Department("Computer Science and Information Technology", "CSIT")
    csit110 = csit_dept.add_course("Fundamental Programming with Python", "CSIT110", 6)
    csit_dept.find_course("SC101")
except CourseNotFoundError as e:
    print(e)

"""instance = Student('','')
instance.enrol()
Student.enrol() #ERROR!
Student.from_list([]) #works"""

# QUESTION 6
class Employee(object):
    """docstring for Employee"""
    def __init__(self, first_name, last_name, em_num, position, phone_ext):
        self.first_name = first_name
        self.last_name = last_name
        self.em_num = em_num
        self.position = position
        self.phone_ext = phone_ext

    @classmethod
    def from_dict(cls, input_dict):
        try:
            cls.validate_phone_num(input_dict.phone_ext):
        except ValueError:
            print('Invalid phone number!')
            return None
        else:
            return cls(input_dict["first_name"], input_dict["last_name"], input_dict["em_num"], input_dict["position"], input_dict["phone_ext"])

    @staticmethod
    def validate_phone_num(str_number):
        if str_number.startswith('+65') and len(str_number)==11:
            return True
        else:
            raise ValueError()
"""
# Examples of how to call the static or class method
new_employee = Employee.from_dict({"first_name": "Ginny", "last_name":"Weasley", "em_num": "135893", "position":"Chaser","phone_ext":"139874"})
Employee.validate_phone_num('+090123456789')
"""