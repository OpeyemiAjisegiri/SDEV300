#Author: Opeyemi Ajisegiri
#Class:  Building Secure Python Applications [SDEV 300]
#File: lab1_ajisegiri_opeyemi

"""
    The program registers the user to vote. It does using a while loop that becomes
true or false based on if the user decides to or not to continue with the registration
process. This prompt and condition is asked at regular intervals in the registration
breaking the loop whenever the user enters a "No".
Also, each response is error check with the exception of the user's name.
    Age: The user has to be above 18 and below 120 years old.
    Citizienship: The user must be a citizen of the United States of America.
A message is printed if any of the requirements are not met explaining why but when
each requirement is met, the user is asked for the proper two letter abbreviation
[checked] of their state and their zipcode before a congratulatory message is
printed.
"""
import time

print("Welcome to the Voter Registration Application, Python Edition.\n\n")
registring = input("Do you want to register to vote in the United States?[Yes/No]\t")
while registring.lower() not in ["no", "n"] and registring.lower() in ["yes", "y"]:
    first_name = input("Enter your first name: \t")
    last_name = input("Enter your last name: \t")
    registring = input("Do you want to continue the registration process[Yes/No]?\t")
    if registring.lower() in ["no", "n"]:
        break
    age = int(input("Enter your age: \t"))
    if age > 120:
        print("Please check the age again.")
        age = int(input("Enter your age: \t"))
    elif age < 18:
        print("""\n\nThanks for using the application,{0} {1}.
                Sadly, you are currently too young to vote;
                please return when you are 18 and above """.format(first_name, last_name))
        break
    registring = input("Do you want to continue the registration process[Yes/No]?\t")
    if registring.lower() in ["no", "n"]:
        break
    citizenship = input("Are you a U.S. citizen? [Yes/No] \t")
    if citizenship.lower() in ["yes", "y"]:
        state_of_residence = input("Enter your state of residence: \t")
        if len(state_of_residence) < 2 or len(state_of_residence) > 2:
            print("Enter the proper abbreviation of your state")
            state_of_residence = input("Enter your state of residence: \t")
        zipcode = input("Enter your zipcode: \t")
        if len(zipcode) > 5 or len(zipcode) < 5:
            print("Enter the proper zipcode")
            zipcode = input("Enter your zipcode: \t")
        print("\n\nCongratulations, you have been registered to vote.")
        print("Here is the information you registered with: ")
        print("Name[first, last]: {0} {1}".format(first_name, last_name))
        print("Age: {}".format(age))
        print("Citizenship: {}".format(citizenship))
        print("State: {}".format(state_of_residence))
        print("Zipcode: {}".format(zipcode))
        print("""Thanks for using the Voter Registration Application.
                Your voter registration card will be shipped within 3 weeks.""")
    else:
        print("""\n\nThanks for using the application,{0} {1}.
                You are not eligle to vote in the United States
                of America.""".format(first_name, last_name) )
    break
print("Thanks you for using the application.")
time.sleep(30)
