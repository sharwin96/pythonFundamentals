
#name = "Sharwin Givakumar"
#student_num = "6652359"
#subject_code = "CSIT110"


######## Question 1 #######
import re 

def question1():
    input_firstNumber = input("Please enter the first integer : ")
    firstNumber = int(input_firstNumber)

    input_secondNumber = input("Please enter the second integer : ")
    secondNumber = int(input_secondNumber)

    input_thirdNumber = input("Please enter the third integer : ")
    thirdNumber = int(input_thirdNumber)

    productOfTheNumber = firstNumber * secondNumber * thirdNumber

    if(productOfTheNumber < 0):
        productOfTheNumber = productOfTheNumber * (-1)

    print("Display equation using string addition : "+ input_firstNumber + " x " + input_secondNumber + " x " + input_thirdNumber + " = " + str(productOfTheNumber) )

######### End of Question 1 #########

######## Question 2 ########
def question2():
    enter_firstSubjectCode = input("Enter the 1st subject code : ")
    enter_firstSubjectTitle = input("Enter the lst subject title : ")
    enter_firstSubjectCreditPts = input("Enter the 1st subject credit points : ")
    firstSubjectCreditPts = int(enter_firstSubjectCreditPts)

    enter_secondSubjectCode = input("Enter the 2nd subject code : ")
    enter_secondSubjectTitle = input("Enter the 2nd subject title : ")
    enter_secondSubjectCreditPts = input("Enter the 2nd subject credit points : ")
    secondSubjectCreditPts = int(enter_secondSubjectCreditPts)

    totalCreditPts = firstSubjectCreditPts + secondSubjectCreditPts

    print("Your chosen subjects: ")
    print("{0}: {1}".format(enter_firstSubjectCode,enter_firstSubjectTitle))
    print("{0}: {1}".format(enter_secondSubjectCode,enter_secondSubjectTitle))
    print("Total credit points: {0}".format(totalCreditPts))

########## End of Question 2 ########

######### Question 3 #########
def question3():
    adultPrice = 39.00
    childPrice = 26.50
    babyPrice = ""
    

    noOfAdultTix = input("How many adult tickets you want to order : ")
    noOfAdults = int(noOfAdultTix)
    totalCostAdultTix = adultPrice * noOfAdults 
    totalCostAdultTixDollar = "${0:.2f}".format(totalCostAdultTix) 

    noOfChildTix = input("How many children (3-12 years old) tickets : ")
    noOfChild = int(noOfChildTix)
    totalCostChildTix = childPrice * noOfChild
    totalCostChildTixDollar = "${0:.2f}".format(totalCostChildTix) 

    noOfBabyTix = input("How many children (<3 years old) tickets : ")
    noOfBaby = int(noOfBabyTix)
    if noOfBaby < 1 :
        babyPrice = "$0.00"
    else:
        babyPrice = "free"

    totalNumberOfPeople = noOfAdults + noOfChild + noOfBaby
    totalCost = totalCostChildTix + totalCostAdultTix
    totalCostDollar = "${0:.2f}".format(totalCost) 

    print("{0:<20}{1:^17}{2:>15}".format("Type","Number of tickets","Cost"))
    print("{0:<20}{1:^17}{2:>15}".format("Adult",noOfAdultTix,totalCostAdultTixDollar))
    print("{0:<20}{1:^17}{2:>15}".format("Children (3-12y.o.)",noOfChildTix,totalCostChildTixDollar))
    print("{0:<20}{1:^17}{2:>15}".format("Children (<3)",noOfBabyTix,babyPrice))
    print("{0:<20}{1:^17}{2:>15}".format("Total",totalNumberOfPeople,totalCostDollar,))
###### End of Question 3 #######

###### Question 4 ######
def question4():
    assn_mark = input("Enter your assignment mark: ")
    assignment = int(assn_mark)

    project_mark = input("Enter your project mark: ")
    project = int(project_mark)

    exam_mark = input("Enter your final exam mark: ")
    exam = int(exam_mark)
    
    total_marks = assignment + project + exam 
    
    grade = ""
    if(total_marks >= 90 and exam >= 20):
        grade = "A"
    elif(total_marks >= 75 and exam >= 20):
        grade = "B"
    elif(total_marks >= 60 and exam >= 20):
        grade = "C"
    elif(total_marks < 60 and exam <20):
        grade = "Fail"
    else:
        grade = "Fail"
    
    print("Your marks :")
    print("{0:<22}{1:>4}".format("Assignment:",assignment))
    print("{0:<22}{1:>4}".format("Project:",project))
    print("{0:<22}{1:>4}".format("Final exam:",exam))
    print("{0:<22}{1:>4}".format("Grade:",grade))

###### end of question 4 ######


######### Question 5 ############
def question5():

    user_input = True 
    fileNameCopy = ""
    storeNames = ""

    while(user_input == True):
        fileName = input("FileName? ")

        if(fileName == ""):
            user_input = False
        else:
            fileNameCopy = fileName
            cleanNames = re.sub("[\(\[].*?[\)\]]", "", fileNameCopy)

            storeNames = storeNames + cleanNames 
            
    print(storeNames)

######### end of question 5 #########


if name == "Sharwin Givakumar":
    print("Name :", name)
    print("Student No. :", student_num)
    print("Student Code. :", subject_code)
    print('QUESTION 1')
    question1()
    print('QUESTION 2')
    question2()
    print('QUESTION 3')
    question3()
    print('QUESTION 4')
    question4()
    print('QUESTION 5')
    question5()




        

        


        









