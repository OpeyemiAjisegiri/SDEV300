#Author: Opeyemi Ajisegiri
#Class: SDEV 300
#Assignment: Lab 2
"""
 This Program utilizes a menu to prompt the user for inputs and compute results
utilizing the user inputs such as generating a secure password, calculating the
days left between now and a future date, percentage, volume et al.
"""

from datetime import date
import string
import secrets
import math
import time

def display():
    """    Displays the menu options.      """
    print("1. Generate Secure Password")
    print("2. Calculate and Format a Percentage")
    print("3. How many days from today until July 4, 2025?")
    print("4. Use the Law of Cosines to calculate the leg of a triangle.")
    print("5. Calculate the volume of a Right Circular Cylinder")
    print("6. Exit program")

def compute_days():
    """
         Calculates the numbers of days between the day the program
         is ran and a future date using the datetime library.
    """
    today = date.today()  #todays_date = datetime.date.today()
    future = date(2025, 6, 4)	#future_date = datetime.date(2025, 6, 4)
    time_diff = future - today
    print("\nHow many days from today until July 4, 2025?")
    print("Today's date is ", today)
    print("The future date is ", future)
    print("The number of days till {} are {} days\n".format(future,
                                                           time_diff.days))

def calculate_volume():
    """
        Calculates the volume of a right circular cylinder using
        the formular pi *(r squared) * h, outputting the result
        to three less significant figures after the decimal.
    """
    validation = False
    while validation is False:
        try:
            radius = int(input("Enter the radius of the cylinder:\t"))
            height = int(input("Enter the height of the cylinder:\t"))
            validation = True
        except ValueError:
            print("Enter a numeric value")
    volume = math.pi *((radius ** 2)* height)
    print("The volume of the cylinder is {:.3f} units cubed\n".format(volume))

def calculate_leg():
    """
        Calculates the third side of a triangle using the Laws of Cosine
        through the formular: c squared = (a squared + b squared) - 2ab Cos(C)
        outputting the result to two less significant figures after the decimal.
    """
    validation = False
    while validation is False:
        try:
            side_a = float(input("Enter the length of the first side:\t"))
            side_b = float(input("Enter the length of the second side:\t"))
            angle_c  = float(input("Enter the third angle of the triangle: \t"))
            validation = True
        except ValueError:
            print("Enter a numeric value")
    side_c = (side_a ** 2) + (side_b ** 2)
    side_c -= ((2*(side_a * side_b))*(math.cos(math.radians(angle_c))))
    print("The size of the leg is {} \n".format(round(math.sqrt(side_c),2)))

def calculate_percentage():
    """
        Calculates the percentage of a number based on the number(s)
        entered by the user and outputs it to user-defined decimal places.
    """
    validation = False
    while validation is False:
        try:
            base = int(input("Enter the base value(denominator): \t"))
            percentile = int(input("Enter the percentile value(numerator): \t"))
            decimal = int(input("Enter the number of decimal places to display:\t"))
            validation = True
        except ValueError:
            print("Enter a numeric value")
    percentage = (100*(percentile/base))
    print("The percentage is ",f"{percentage:.{decimal}f}", "%.\n")

def generate_secure_password():
    """
        Generates a secure password based on the parameters entered by the user.
        Although, it's presumed that the minimum parameters for a secure
        password are 11 characters, 2 punctuations, 2 numbers, 1 capital letter
        and 1 small letter.
    """
    validation = False
    while validation is False:
        try:
            length = int(input("Enter the needed length of the password: \t"))
            while length < 11:
                length = int(input("Eleven is the needed minimum:\t"))
            num = int(input("Enter the minimum number of numbers needed: \t"))
            while num < 2:
                num = int(input("The minimum number of numbers is 2: \t"))
            punc_comp = int(input("Enter the minimum number of punctuations needed:\t"))
            while punc_comp < 2:
                punc_comp = int(input("The minimum number of punctuation is 2:\t"))
            low_case = int(input("Enter the minimum number of lowercase letters:\t"))
            up_case = int(input("Enter the minimum number of uppercase letters: \t"))
            validation = True
        except ValueError:
            print("Enter a numeric value for each input")
    word = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(word) for i in range(length))
        if (sum(p.islower() for p in password) >= low_case
            and sum(p.isupper() for p in password) >= up_case
            and sum(p.isdigit() for p in password) >= num):
            #and sum(p.punctuation() for p in password) >= punc_comp
            print("The password generated is '{}'\n.".format(password))
            break

"""
  The main function; it prompts the user for a menu option,
  performs tasks based on the option selected by the user and
  his/her input.
"""
print("Welcome To The Secure Computation Python Application")
display()
menu = int(input("Enter the menu option:\t"))
while menu not in (6,0):   #while menu != 6 and menu != 0:
    if menu == 1:
        print("\nGenerate Secure Password")
        generate_secure_password()
    elif menu == 2:
        print("\nCalculate and Format a Percentage")
        calculate_percentage()
    elif menu == 3:
        compute_days()
    elif menu == 4:
        print("\nUse the Law of Cosines to calculate the leg of a triangle.")
        calculate_leg()
    elif menu == 5:
        print("\nCalculate the volume of a Right Circular Cylinder")
        calculate_volume()
    elif menu == 6:
        break
    display()
    menu = int(input("Enter the menu option:\t"))
print("Thanks for using this application, see you soon")
time.sleep(5)
