"""Assignment 2

Name: Sharwin Givakumar
Student number: 6652359
Subject code: CSIT110

"""
name = "Sharwin"
student_num = "6652359"  # Student number 
subject_code = 'CSIT110'  # CSIT110 or SP420


# ===========Insert your solution to Question 1 here =================#
def get_subscription():
    
    selectedChannels = {}
    cost = 0.0

    print("Channels available for subscription (price/mth) ")
    print("{0:<41}{1:>6}".format("Sports Group Pack","$21.40"))
    print("{0:<41}{1:>6}".format("Documentaries Pack","$15.32"))
    print("{0:<41}{1:>6}".format("FOX Movies Pack","$17.12"))
    print("{0:<41}{1:>6}".format("HBO Pack","$13.98"))
    print("{0:<41}{1:>6}".format("Cinema World","$9.56"))
    print("{0:<41}{1:>6}".format("Celestial Movies","$8.56"))
    print()
    
    askSelection = input("Subscribe to Sports Group Pack ? (Y/N): ")
    if (askSelection == "Y") or (askSelection == "y"):
        selectedChannels["Sports Group Pack"] = 21.40
        cost = cost + 21.40
    
    askSelection = input("Subscribe to Documentaries Pack ? (Y/N): ")
    if (askSelection == "Y") or (askSelection == "y"):
        selectedChannels["Documentaries Pack"] = 15.32
        cost = cost + 15.32
    
    askSelection = input("Subscribe to FOX Movies Pack ? (Y/N): ")
    if (askSelection == "Y") or (askSelection == "y"):
        selectedChannels["Fox Movies Pack"] = 17.12
        cost = cost + 17.12
    
    askSelection = input("Subscribe to HBO Pack ? (Y/N): ")
    if (askSelection == "Y") or (askSelection == "y"):
        selectedChannels["HBO Pack"] = 13.98
        cost = cost + 13.98

    askSelection = input("Subscribe to Cinema World ? (Y/N): ")
    if (askSelection == "Y") or (askSelection == "y"):
        selectedChannels["Cinema World"] = 9.56
        cost = cost + 9.56
    
    askSelection = input("Subscribe to Celestial Movies ? (Y/N): ")
    if (askSelection == "Y") or (askSelection == "y"):
        selectedChannels["Celestial Movies"] = 8.56
        cost = cost + 8.56
    print()

    print("Your selection:")
    for channel, price in  selectedChannels.items():
        print("- " + channel + " (${0:.2f})".format(price))
    
    print()
    print("Total Cost ${0:.2f}".format(cost))

# ======================= End of Question 1 ==========================#
# ===========Insert your solution to Question 2 here =================#
input_list = [ [1,3,3], [2,5,-1],[3,2],[4,5,3],[0,23],[1,2,3,4],[1] ]

def generate_qns_from_list(list):
    finalList = []
    stringEquation = ""
    productEquation = 1

    for x in range(0,len(list)):
        #print(list[x])
        for y in range(0,len(list[x])):
            
            if(len(list[x]) > 1):

                if(y < len(list[x]) - 1):
                    stringEquation = stringEquation + str(list[x][y]) + " x " 
                    productEquation = productEquation * list[x][y]
                else:
                    stringEquation = stringEquation + str(list[x][y]) 
                    
                equationList = {
                    'qns': stringEquation,
                    'ans': productEquation
                }

        stringEquation = ""
        productEquation = 1
        finalList.append(equationList)
    #print(finalList)


# ======================= End of Question 2 ==========================#
# ===========Insert your solution to Question 3 here =================#

class ShoppingCart:

    #class attribute
    server_url ="128.123.123.0"

    def __init__(self,account_id):
        self.account_id = account_id
        self.cart = {} 
    
    def add_item_to_cart(self,product,quantity):
       
        key = product
        if key not in self.cart:
            self.cart[key] = quantity
        else :
            self.cart[key] = self.cart[key] + quantity   
        
    def remove_item_from_cart(self,product,quantity):
        
        if product in self.cart:
            self.cart[product] = self.cart[product] - quantity
            if self.cart[product] == 0:
                del self.cart[product]
    
    @classmethod
    def get_url(cls):
        return cls.server_url

    def empty_cart(self):
        shoppingCart = self.cart
        return shoppingCart.clear()

    def count_items(self):
       noOfItems = 0 
       shoppingCart = self.cart
       for product in shoppingCart:
           noOfItems = noOfItems + shoppingCart.get(product)
        
       return noOfItems
     
# ======================= End of Question 3 ==========================#

# ===========Insert your solution to Question 4 here =================#
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
        weightSum = 0
        for key in weight:
            if key in result:
                weightSum = weightSum + (result[key] * weight[key])
        return int(weightSum)

def dict_to_class_obj(studentList):
    studentObjectList = []
    for i in studentList:
        student = Student(i)
        studentObjectList.append(student)
    
    return studentObjectList

# ======================= End of Question 4 ==========================#

def main():
    input_list = [ [1,3,3], [2,5,-1],[3,2],[4,5,3],[0,23],[1,2,3,4],[1] ]
    #Question 1
    get_subscription()
    print() 

    #Question 2
    generate_qns_from_list(input_list)
    print() 

    #Question 3
    newCart = ShoppingCart('1234567') 
    newCart.add_item_to_cart('fruit juice', 2) 
    newCart.add_item_to_cart('tissue box', 4) 
    newCart.add_item_to_cart('ice cream', 3)

    newCart.remove_item_from_cart('tissue box',1)
    newCart.remove_item_from_cart('fruit juice',2)

    newCart.count_items()
    #print(newCart.get_url())
    newCart.empty_cart() 
    newCart.count_items()
    

    #Question 4
    listOfStudentDict = []
    weights = {
        "assignment_1": 1.0,
        "examination_1": 9.0
    }
    
    student = {
        "name": "Fus Ro Dah",
        "result": {
            "assignment_1": 10,
            "assignment_2": 10,
            "examination_1": 10
        }
    }

    listOfStudentDict.append(student)
    
    student = {
        "name": "Foo Barry",
        "result": {
            "assignment_1": 1,
            "assignment_2": 2,
            "examination_1": 3
        }
    }

    listOfStudentDict.append(student)

    studentObjects = dict_to_class_obj(listOfStudentDict) #Question 4 part 1

    sum = 0
    for student in range(0,len(studentObjects)):  # Question 4 part 2
        sum = studentObjects[student].get_weighted_result(weights)
        #print("Weighted result : {0}".format(sum))


if __name__ == "__main__":
    main()
