import random
import sys
import csv


def choices():
    global loggedIn
    print("Please choose what you would like to do.")
    choice = input("Would you like to register or login: ")
    if choice == "register":
         register()
    elif choice == "login":
         loggedIn = login()
    else:
        raise TypeError


def register():
    print("Please make a custom username and password")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("userinfo.txt", 'r')
    info = f.read()
    if name in info:
        print("Name Unavailable. Please Try Again")
    else:
      print("reload the program to login")
      f.close()
      f = open("userinfo.txt", 'w')
      info = info + " " + name + " " + password
    
      f.write(info)
    f.close()   
    sys.exit()

def login():
    global name 
    print("Please provide your username and password")
    name = str(input("username: "))
    password = str(input("Password: "))
    f = open("userinfo.txt", 'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        usr_password = info[index]
        if usr_password == password:
           print("Welcome Back, " + name)
           return True
        else:
            print("Password entered is wrong")
    else:
        print("Name not found. Please rerun program and register an account.")


def mainfunc():
    global average
    print(
        "Here are some averages to help you make an estimated guess if you are not 100% sure: "
    )
    print("average kWh per person is an estimated 56 kWh")
    print(
        "average weekly water usage per perosn in a household is 798 liters ")
    print(
        "the average gas consumption per person in a household is 46  cubic meteres of naturla gas a year"
    )
    print("the average cost per month for health is $75/person")
    print("the average car insurance is $24 a week")
    print("")
    print(" ")
    print(" ")

    # input variables holding values of different factors that contribute to user carbon footprint
    elecVar = int(input('What is your average weekly kWh usage: '))
    waterVar = int(
        input("How many liters of water do you use on average in a week: "))
    gasVar = int(input("How much gas do you use on average weekly: "))
    # Travel variables

    # if car prompt input for average km

    # if bus prompt input for average km
    # if tax/uber prompt input for average km

    # ask if they have flown anywhere in the past 2 weeks
    # if yes, ask distance traveled

    # service variables
    healthVar = int(input("How much do you spend monthly on health: "))
    recVar = int(input("How much do you spend monthly on recreation: "))
    eduVar = int(input("How much do you spend monthly on education: "))
    vehVar = int(input("What are you monthly vehicle costs: "))

    #constant efficiency factors
    elecConstant = 0.7
    waterConstant = 0.6
    fuelConstant = 0.22
    healthConstant = 0.3
    recConstant = 0.2
    eduConstant = 0.3
    vehConstant = 2.73

    #carbon footprint tip list
    tips = [
        "Drive less. Walk, take public transportation, carpool, rideshare or bike to your destination when possible. This not only reduces CO2 emissions, it also lessens traffic congestion and the idling of engines that accompanies it.",
        "Switch lights off when you leave the room and unplug your electronic devices when they are not in use.",
        "Installing a low-flow showerhead to reduce hot water use can save 350 pounds of CO2. Taking shorter showers helps, too.",
        ""
    ]
    # create variable for, good footprint, average footprint, and bad footprint
    averageEmission = 0.12

    # calculation function that take user inputs(national average will be used for efficienty factors)(weekly)
    def elecCalc(electricty):
        return electricty * elecConstant

    def waterCalc(water):
        return water * waterConstant

    def fuelCalc(fuel):
        return fuel * fuelConstant

    def healthCalc(health):
        return (health * healthConstant) / 4.5

    def recCalc(recreation):
        return (recreation * recConstant) / 4.5

    def eduCalc(education):
        return (education * eduConstant) / 4.5

    def vehCalc(vehicle):
        return (vehicle * vehConstant) / 4.5

    finalElecVal = elecCalc(elecVar)
    finalWaterVal = waterCalc(waterVar)
    finalGasVal = fuelCalc(gasVar)
    finalHealthVal = healthCalc(healthVar)
    finalRecVal = recCalc(recVar)
    finalEduVal = eduCalc(eduVar)
    finalVehVal = vehCalc(vehVar)

    average = (((finalElecVal + finalWaterVal + finalGasVal + finalHealthVal +
                 finalRecVal + finalEduVal + finalVehVal) / 7) / 907) / 1.102

    print("")
    print("")

    print("you carbon footprint for the week is: ", average)

    print(" ")

  
    if average < averageEmission:
        print("you have a good carbon footprint!")
        return True
    elif average > averageEmission:
        print("you have a bad carbon footprint")
    else:
        print("you have an average carbon footprint")

    if average > averageEmission:
        response = input(
            "would you like a tip to reduce your carbon footprint: ")
    
    if response == "yes":
        print("Here are some tips to reduce you carbon footprint: ")
        print(random.choice(tips))

def mergeSort(nums):
# Put items of nums into ascending order
  n = len(nums)
# Do nothing if nums contains 0 or 1 items
  if n > 1:
# split the two sublists
    m = n//2
    nums1, nums2 = nums[:m], nums[m:]
# recursively sort each piece
    mergeSort(nums1)
    mergeSort(nums2)
# merge the sorted pieces back into original list
    merge(nums1, nums2, nums)

def merge(lst1, lst2, lst3):
# merge sorted lists lst1 and lst2 into lst3
# these indexes keep track of current position in each list
  i1, i2, i3 = 0, 0, 0 # all start at the front
  n1, n2 = len(lst1), len(lst2)
# Loop while both lst1 and lst2 have more items
  while i1 < n1 and i2 < n2:
    if float(lst1[i1][1]) < float(lst2[i2][1]): # top of lst1 is smaller
      lst3[i3] = lst1[i1]
     # copy it into current spot in lst3
      i1 = i1 + 1
      i3 = i3 + 1
    else: # top of lst2 is smaller
      lst3[i3] = lst2[i2] # copy itinto current spot in lst3
      i2 = i2 + 1
      i3 = i3 + 1 # item added to lst3, update position
# Here either lst1 or lst2 is done. One of the following loops
# will execute to finish up the merge.
# Copy remaining items (if any) from lst1
  while i1 < n1:
    lst3[i3] = lst1[i1]
    i1 = i1 + 1
    i3 = i3 + 1
# Copy remaining items (if any) from lst2
  while i2 < n2:
    lst3[i3] = lst2[i2]
    i2 = i2 + 1
    i3 = i3 + 1

def binarySearch(alist, item):
  first = 0
  last = len(alist) - 1
  while first <= last:
    midpoint = (first + last)//2
    userstat = alist[midpoint]
    if userstat[0] == item:
      return midpoint

    if item < userstat[0]:
      last = midpoint-1
    else:
      first = midpoint + 1
  return -1

def main():
  global loggedIn
  global name 
  global average
  choices()
  if loggedIn == True:
    mainfunc()
    with open('userdatabase.csv', mode='r') as infile:
      reader = csv.reader(infile)
    
      mydict = {rows[0]:float(rows[1]) for rows in reader if len(rows) == 2}
    mydict[name] = average 
    mylist = [[key, val] for key, val in mydict.items()]
    #sort list
    mergeSort(mylist)
    index = binarySearch(mylist, name)
    if index != -1:
      print(f"you're ranked {index+1} out of {len(mylist)}")
    with open('userdatabase.csv', mode='w') as outfile:
      writer = csv.writer(outfile)
      writer.writerows(mylist)



    







main()




# Based on the value collected from the calculator if it is greater
# than the good average footprint the program would give the user
# recommendations on how to reduce their carbon footprint. Otherwise if it is less the user will be told to keep it upprint(elecCalc())
# data from the carbon footprint calculator will then be appended to a database that will be connect multiple users of this app


# database will sort the users into different percentile categories. The main goal is to be in the top 10%

# users weekly ranking will be presented to them alongside their carbon footprint
