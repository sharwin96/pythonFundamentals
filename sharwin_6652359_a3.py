""" 
    Template for Assignment 3
    Use this template for submission.
    - This template includes an example function.
    - Note that the template uses 4 space for indenation
      which you may choose to replace as tabs
"""
import random

student_name = 'Sharwin'
student_uow_id = '6652359'
course_code = 'CSIT110'

"""Insert your solution between these lines"""

def myClass_get_int_unit_test(inputClass):

    """
     This example takes in a class definition as input,
     then instantiates a class object and test its method
     in a try except system.
    """
    try:
        obj = inputClass(-1)
        obj.name = "sharwin" 
        obj.get_integer()
    except ValueError as ve :
        return "V"
    except AttributeError as ae:
        return "A"
    except:
        return "O"
    

def question1():
    # A class with one method
    class MyClass():    
        def __init__(self,integer):
            self.integer = integer
        
        def get_integer(self):
            if(self.integer < 0 ):
                raise ValueError
            return self.integer
            
    # test the get int unit method
    return myClass_get_int_unit_test(MyClass)

def question2 (inputOne,inputTwo):
    allUnitPrices ={}

    try:
        for goods in range(0,len(inputTwo)):
            goodsName = inputTwo[goods]
            try:
                unitPrice = inputOne[goodsName][0] / inputOne[goodsName][1]
                allUnitPrices[goodsName] = unitPrice
            except ZeroDivisionError:
                allUnitPrices[goodsName] = -1
            except KeyError :
                allUnitPrices[goodsName] = None
    
    except:
        allUnitPrices.clear()
    
    return allUnitPrices

class AssessmentNotFoundError(Exception):

    def __init__(self,assessment,student_name):
        self.assessment = assessment
        self.student_name = student_name
    
    def __str__(self):
        return "{} results cannot be found in {}'s results".format(self.assessment,self.student_name)



class Student:

    def __init__(self,student):
        self.name = student["name"]
        self.result = student["result"]
        self.student = {
            "name" : self.name, 
            "results" : self.result 
        }

    def get_weighted_result(self,weight):

        result = self.result
        name = self.name
        weightSum = 0
        
        for key in weight:
            try:
                if(key not in result):
                    raise AssessmentNotFoundError(key,name)
                elif(key in result):
                    weightSum = weightSum + (result[key] * weight[key])
            except AssessmentNotFoundError as ae:
                print(str(ae))
            
        return int(weightSum)

def dict_to_class_obj(studentList):
    studentObjectList = []

    for i in studentList:
        student = Student(i)
        studentObjectList.append(student)
    
    return studentObjectList

class InvalidDepthError(Exception):

    def __init__(self):
        self.message = "Invalid Depth"

    def __str__(self):
        return self.message

class WaterBody():
    RHO = 997
    G = 9.81

    def __init__(self,volume):
        self.volume = volume 
    
    @staticmethod
    def get_hydrostatic_pressure(depth):
        if(type(depth) != float):
            depth = float(depth)

        if (depth < 0 ):
            raise InvalidDepthError
        else:
            hydroStaticPressure = WaterBody.RHO * WaterBody.G * depth

        return hydroStaticPressure 
    
    def get_water_mass(self):
        max = WaterBody.RHO * self.volume
        return max
    
    @staticmethod
    def is_large(volume):
        if(volume > 100):
            return True
        else:
            return False
    
    @staticmethod
    def is_medium(volume):
        if(volume >= 50 ) and (volume <= 100):
            return True
        else:
            return False

    @staticmethod
    def is_small(volume):
        if (volume < 50):
            return True
        else:
            return False

    @classmethod
    def spawn(cls):
        randomNumber = random.randint(1,300)
        return cls(randomNumber)


class SingaporeNumbers:

    @staticmethod
    def car_plate_checksum(numbers):
        alphabetNumbers = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,
                            "J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,
                            "R":18,"S":19,"T":20,"U":21,"P":22,"W":23,"X":24,"Y":25,"Z":26}
        
        correspondingRemainders = {0:"A", 1:"Z", 2:"Y", 3:"X", 4:"U", 5:"T", 6:"S", 7:"R", 8:"P", 
                                    9:"M", 10:"L", 11:"K", 12:"J", 13:"H", 14:"G", 15:"E", 16:"D", 17:"C", 18:"B"}

        multipliables = [9,4,5,4,3,2]

        numbersToList = [] #collate the letters from numbers into a list
        for i in range(0,len(numbers)):
            numbersToList.append(numbers[i])
        #print("Input Numbers : {}".format(numbersToList))

        #separate the letters and digits into individual lists
        listForLetters = []
        listForDigits = []
        
        for i in range(0,len(numbersToList)):
            try:
                if numbersToList[i].isalpha() == True:
                    raise Exception
            except Exception :
                listForLetters.append(numbersToList[i])

            else:
                listForDigits.append(int(numbersToList[i]))

        if len(listForDigits) == 3 :
            listForDigits.insert(0,0)
        elif len(listForDigits) == 2:
            listForDigits.insert(0,0)
            listForDigits.insert(1,0)
        elif len(listForDigits) == 1:
            listForDigits.insert(0,0)
            listForDigits.insert(1,0)
            listForDigits.insert(2,0)
        
        #print("Part thats is letters : {}".format(listForLetters))
        #print("Part thats is digits : {}".format(listForDigits))

        lettersToDigits = [] # stores the letter that were converted to digits
        lastIdx = len(listForLetters) - 1
        secondLastIdx = len(listForLetters) - 3

        if len(listForLetters) == 1:
            for key in alphabetNumbers:
                if key == listForLetters[0]:
                    lettersToDigits.append(alphabetNumbers[key])
            lettersToDigits.insert(0,0)

        else:
            for key in alphabetNumbers:
                for i in range(lastIdx,secondLastIdx,-1):
                    if key == listForLetters[i]:
                        lettersToDigits.append(alphabetNumbers[key])
        
        #print("After converting the letter to digits : {}".format(lettersToDigits))
        
        finalDigits = [] #contains all the digits in the combination after conversion
        lettersToDigits.extend(listForDigits)
        finalDigits.extend(lettersToDigits)
        
        #print("Final combination of digits : {}".format(finalDigits))

        multiplyDigits = [] #multiply the numbers with the given set of multipliables
        for i in range(0,len(finalDigits)):
            multiplyDigits.append(finalDigits[i] * multipliables[i])
        
        #print("After multiplying with multipliables : {}".format(multiplyDigits))

        sumAfterMultiplied = 0 #get the sum of the multiplied numbers
        for i in range(0,len(multiplyDigits)):
            sumAfterMultiplied += multiplyDigits[i]
        #print("sum of multiplied numbers : {}".format(sumAfterMultiplied))

        getRemainder = sumAfterMultiplied % 19
        #print("The remainder after mod 19 : {}".format(getRemainder))

        checksum = correspondingRemainders[getRemainder]
        #print("Checksum : " + checksum)

        return checksum
    
    @staticmethod
    def magic_num_checksum(numbers):
        
        checkDigit = {
            10 : "A",9 : "B",8 : "C", 7 : "D", 6 : "E",
            5: "F", 4: "G", 3 : "H", 2: "I",1 : "Z",0 : "J"
        }

        weights = [2,7,6,5,4,3,2]
        numberList = []

        #convert the string a integer and then append it to a list
        for i in range(0,len(numbers)):
            numberList.append(int(numbers[i]))
        
        #print(numberList)

        #multiply with the values in weights list and add them together
        sum = 0
        for i in range(0,len(weights)):
            sum += numberList[i] * weights[i]

        #print(sum)
        
        # get the check digit d
        getDigits = sum % 11

        #print(getDigits)

        digit = ""
        #check with the list
        for i in range(0 , len(checkDigit)):
            if i == getDigits:
                digit = checkDigit[i]
        return digit

    



def main():
    """an example function that creates a class and feeds into
    the class into the myClass_demo_unit_test for testing
    You are free to create your own test subjects that raise
    errors to test your code here."""
    
    #question 1
    qn1 = question1()
    print(qn1)
    
    #question 2
    firstInput = {
        "vinegar" : [120.100],
        "ketchup" : [950,1000],
        "apples" : [850,1100],
        "oranges" : [1050,0]
    }

    secondInput = ["ketchup","oranges","pear"]
    q2Output = question2(firstInput,secondInput)
    print(q2Output)


    #question3 
    listOfStudentDict = []
    weights = {
        "test": 1.0,
        "examination_1": 9.0
    }

    student = {
        "name": "Tom",
        "result": {
            "assignment_1": 10,
            "assignment_2": 10,
            "examination_1": 10
        }
    }
    listOfStudentDict.append(student)

    studentObjects = dict_to_class_obj(listOfStudentDict) 
    sum = 0
    
    for student in range(0,len(studentObjects)):
        sum = studentObjects[student].get_weighted_result(weights)
        print("Weighted result : {0}".format(sum))
    
    ##Question 4### 

    pool = WaterBody(31.42)
    print(pool.get_hydrostatic_pressure(1) )
    print(pool.get_water_mass() )

    try:
        pool.get_hydrostatic_pressure(-1)
    except Exception as e:
        print(e)

    pool.is_small(pool.volume)
    pool.is_medium(pool.volume)
    pool.is_large(pool.volume)

    randomWater = WaterBody.spawn()

    ### QUESTION 5 ###
    ### part 1 ###
    number1 = SingaporeNumbers()
    number2 = SingaporeNumbers()
    number3 = SingaporeNumbers()

    num1 = number1.car_plate_checksum("SBS3229")
    print("number1 = " + num1)
    num2 = number2.car_plate_checksum("E23")
    print("number2 = " + num2)
    num3 = number3.car_plate_checksum("SS11")
    print("number3 = " + num3)

    number = SingaporeNumbers()


    #Question 5 part2
    num = number.magic_num_checksum("9629247")
    print("number = " + num)

if __name__ == '__main__':
    main()