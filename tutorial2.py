# QUESTION 1
q1_list = [1,2,3,4,1,2,3,4]  # 1.1
q1_list.append(2000)       # 1.2 option 1
q1_list += [2000]          # 1.2 option 2
q1_list = q1_list +[2000]  # 1.2 option 3
del q1_list[0]  # 1.3 Make sure you use square brackets here.
q1_list[-1] = 0              # 1.4 option 1
q1_list[7] = 0               # 1.4 option 2
q1_list[len(q1_list)-1] = 0  # 1.4 option 3
q1_list.insert(0,1)  # 1.5
# 1.6 option 1
for i in range(len(q1_list)):
    q1_list[i] += 10
# 1.6 option 2
q1_list = [i+10 for i in q1_list]
# 1.7 option 1
for i in range(len(q1_list)):
    q1_list[i] = 10
# 1.7 option 2
q1_list = [10 for i in q1_list]
# 1.7 not an option due to question requirement
q1_list = [10] * len(q1_list)
# 1.8
for i in range(len(q1_list)):
    q1_list[i] += i
# 1.8 extra learning
# q1_list = [value+index for value, index in enumerate(q1_list)]
# 1.9 best option
q1_list.clear()
# 1.9 not so readable option
q1_list = []


# QUESTION 2
num_of_squares = int(input('How many square numbers to generater? '))
list_of_sqaure = []
for i in range(0, num_of_squares):
    list_of_sqaure.append(i**2)
# list_of_sqare = [i**2 for i in range(0,num_of_squares)]
print(list_of_sqaure)


# QUESTION 3
fib_count = int(input('How many square numbers to generater? '))
fib_list = [0,1] # initialise first two numbers
for i in range(2, fib_count):
    fib_list.append(fib_list[i-2] + fib_list[i-1])
print(fib_list)

# QUESTION 4
num_list = []
user_input = ''
while not user_input.lower()=='quit':
    user_input = input('Enter an integer (enter QUIT/quit to quit): ')
    if user_input.lower()=='quit':
    	break
    num_list.append(int(user_input))
print('You have entered: ', end='')
for i in range(0, len(num_list)-1):
	print(num_list[i], end=", ")
print(num_list[-1], end=".")

# QUESTION 5
state_abb = {
	"NSW":"New South Wales",
	"ACT": "Australian Capital Territory",
	"NT": "Northern Territory",
	"QLD": "Queensland",
	"SA": "South Australia",
	"TAS": "Tasmania",
	"VIC": "Victoria",
	"WA": "Western Australia"
}
print(state_abb["QLD"])
print(state_abb["VIC"])

# QUESTION 6
user_info = {
	"first_name": "Amanda",
	"last_name": "Smith",
	"age": 20
}
print(user_info["first_name"])
user_info["last_name"] = "Harrison"
user_info["email"] = "a.harrison@gmail.com"
del user_info["age"]

# QUESTION 7
abb = input("Enter state NSW/ACT/NT/QLD/SA/TAS/VIC/WA: ")
print("You have entered "+ state_abb[abb])  # state_abb is from question 5

# QUESTION 8
newDict = {}
for i in [0,1]:
	key = input("Enter a key (string): ")
	val = input("Enter value: ")
	newDict.update({key:val})
print('We have a dictionary:', newDict)

# QUESTION 9
dic1={12:144, 13:169}
dic2={3:33, 4:44}
dic3={5:510, 6:632}
newDict = dic1.copy()
newDict.update(dic1)
newDict.update(dic2)
newDict.update(dic3)
print('Expected Result:', newDict)
# QUESTION 10
# duplicate of question 9
# QUESTION 11
school = {
	"classA": {
		"student": {
			"name": "Merlion Tan",
			"subjects": {
				"python": 70,
				"communications": 80
			}
		}
	}
}
print(school["classA"]["student"]["subjects"]["communications"])
# QUESTION 12
sampleDic = {
	"name": "Kelly",
	"interest": "badminton",
	"age": 32,
	"town": "Ang Mo Kio"
}
# option 1
sampleDic["district"] = sampleDic["town"]
del sampleDic["town"]
# option 2 (extra learning)
sampleDic["district"] = sampleDic.pop("town")

# QUESTION 13
inventory = {
	'coins': 500,
	'pouch': ['flint','twine','gemstone'],
	'haversack': ['wooden spear', 'dagger', 'fish', 'drumstick']
}
inventory['equipped'] = ['ruby','red potion', 'apple']
inventory['haversack'].remove('dagger')
inventory['coins']+=50
print(inventory)

# QUESTION 14
stock = {
	"sunblock": 25,
	"swimming cap": 2,
	"ear plugs": 4,
	"goggles": 15
}
prices = {
	"sunblock": 16,
	"swimming cap": 10,
	"ear plugs": 1.5,
	"goggles": 9.9
}
# part 1 option 1
keys = stock.keys()  # this method return data type dict_keys
keys_list = list(keys)  # convert to list data type
string_of_items_on_sale = ', '.join(keys_list)  #string the list together with ', '
print('Items available on sale: ' + string_of_items_on_sale)
# part 1 option 2
print('Items available on sale:', ', '.join(list(stock.keys())))
# part 2
total_cost = 0
for item in stock:
	total_cost += prices[item]*stock[item]

total_cost *= 1.07
print(f'Total cost: {total_cost:<.2f}')