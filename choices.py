import random
import sys

#Functions
def validation(num):
    return str(num).isdigit() and num>0 and num<5;

def randomNumber(max):
    randNo = random.randint(1,max)
    return randNo;

def lunchChooser(num):
    if num == 1:
        print "Greenwich Salad\n"
    elif num == 2:
        print "Switch Burrito\n"
    elif num == 3:
        print "CCP\n"
    return;

def vacationChooser(num):
    if num == 1:
        print "Europe\n"
    elif num == 2:
        print "USA\n"
    elif num == 3:
        print "South East Asia\n"
    elif num == 4:
        print "Japan/ Korea\n"
    elif num == 5:
        print "Australia\n"
    return;

def happyChooser(num):
    if num == 1:
        print "Yes :)\n"
    elif num == 2:
        print "No :(\n"
    return;


#Printing
print("\n")
print("\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~ Choices ~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")
print("\n")

print("Input which choices you would like me to choose:\n")
print("1) What should I eat for lunch?\n")
print("2) Where should I go next for vacation?\n")
print("3) Should I be happy?\n")
print("4) Exit\n")

choice = input("Your input: ")

while not validation(choice):
    print "Please enter a number from 1 to 4\n"
    choice = input("Your input: ");

if choice == 1:
    lunchChooser(randomNumber(3))
elif choice == 2:
    vacationChooser(randomNumber(5))
elif choice == 3:
    happyChooser(randomNumber(2))
elif choice == 4:
    sys.exit(1)