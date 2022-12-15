#Author: Opeyemi Ajisegiri
#Class: SDEV 300
#Assignment: Lab 4
"""
This program manipulates the matrices data inputted by the user after accepting
and validating the user details , name et al. Also, it generates a number of
password and password hashes to be checked if a popular password cracking
website can crack them.
"""
import re
import time
import string
import secrets
import hashlib
import numpy as np
import pandas as pd

def matrix_operation():
    """ Displaying and Getting the Menu Option for the Matrix """
    print("Select a Matrix Operation from the list below:\n")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Matrix Multiplication")
    print("d. Element by element multiplication")
    moperation = input("Enter an option using the preceeding character:\t")
    valid = False
    while valid is False:
        if moperation not in ['a','b','c','d']:
            moperation = input("Enter an option using the preceding character:\t")
        else:
            valid = True
    return moperation

def user_details():
    """ Gets and validates the personal details of the program user. """
    name = input("\nEnter your name [xxx xxx]: \t")
    nvalid = False
    while nvalid is False:
        if name.isalnum() == True:
            print("Re-enter your name: \n")
        else:
            nvalid = True
    email = input("Enter your email address[xxx@xxx.xxx]:\n")
    while(re.fullmatch(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email)) is None:
        print("Enter an actual E-mail address:")
        email = input("Enter your email address[xxx@xxx.xxx]:\n")
    pnumber = input("\nEnter your phone number(xxx-xxx-xxxx):\t")
    while(re.fullmatch(r'\d{3}-\d{3}-\d{4}',pnumber)) is None:
        print("The phone number you entered doesn't match.")
        pnumber = input("Re-enter your phone number(xxx-xxx-xxxx):\t")
    zipcode = input("Enter your zip code+4 (xxxxx-xxxx):\t")
    while(re.fullmatch(r'\d{5}-\d{4}',zipcode)) is None:
        print('The zipcode you enter does not match.')
        zipcode = input("Re-enter your zip code+4 (xxxxx-xxxx): \t")

def first_matrix():
    """ Gets and returns the first matrix from the user. """
    fm_valid = False
    while fm_valid is False:
        try:
            print(""" Enter the first 3x3 matrix
            [seprated by space (" "), one row at a time.]:""")
            matrix = []
            for numbers in range(3):
                numbers = list(map(int, input().split(' ')))
                matrix.append(numbers)
            fm_valid = True
            for value in enumerate(matrix):
                print(value)
            #for x in range(len(matrix)):
            #    print(matrix[x])
        except ValueError:
            print("Enter the correct number of numerical values")
    return matrix

def second_matrix():
    """ Gets and returns the second matrix from the user. """
    sm_valid = False
    while sm_valid is False:
        try:
            print("""Enter your second 3x3 matrix
            [seprated by space(" "), one row at a time]:""")
            matrix = []
            for numbers in range(3):
                numbers = list(map(int, input().split(" ")))
                matrix.append(numbers)
            sm_valid = True
            for value in enumerate(matrix):
                print(value)
        except ValueError:
            print("Enter the correct number of numerical values")
    return matrix

def display_result(rmatrix):
    """ Displays the result of the matrix operations. """
    for count,value in enumerate(rmatrix):
        print(count,value)
    #Replaced, to use enumerate
    #for x in range(len(rmatrix)):
    #    print(rmatrix[x])
    print("The transpose is: ")
    transp_result = np.transpose(rmatrix)
    for  count, value in enumerate(transp_result):
        print(count,value)
    #Using enumerate in place of the lines below
    #for x in range(len(rmatrix)):
    #    print(transp_result[x])
    dframe = pd.DataFrame(rmatrix)
    print(dframe)
    print("The row and column mean values of the results are:")
    #print("Row: ",dframe.mean(axis=1))
    #print("Column: ",dframe.mean(axis=0))
    ## The lines below throwing errors
    #print("Row: ",dframe.loc[:,rmatrix[0]].mean())
    #print("Column: ",dframe.loc[:,rmatrix[0][0]].mean(axis=0))

def generate_password():
    """
        Generates password based on user pre-requisites.
    """
    print("\nEnter the parameters needed to generate the password.")
    validation = False
    while validation is False:
        try:
            length = int(input("Enter the needed length of the password: \t"))
            while length < 10:
                length = int(input("Ten is the needed minimum:\t"))
            num = int(input("Enter the minimum number of numbers needed: \t"))
            while num < 2:
                num = int(input("The minimum number of numbers is 2: \t"))
            punc = int(input("Enter the minimum number of punctuations needed:\t"))
            while punc < 1:
                punc = int(input("The minimum number of punctuation is 1:\t"))
            lcase = int(input("Enter the minimum number of lowercase letters:\t"))
            ucase = int(input("Enter the minimum number of uppercase letters:\t"))
            total = num + punc + lcase + ucase
            if length < total:
                validation = False
                print("""The total number of parameters needed can't be more
                            than the length of the password.""")
            validation = True
        except ValueError:
            print("Enter a numeric value for each input")
    word = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(word) for i in range(length))
        if (sum(p.islower() for p in password) >= lcase
            and sum(p.isupper() for p in password) >= ucase
            and sum(p.isdigit() for p in password) >= num):
            print("\nThe password generated is '{}'\n".format(password))
            break
    return password

def main():
    """ Main Fucntion through which the users interacts with the program """
    print("************ Welcome to the Python Matrix Application *************")
    user_details()
    print("\nDo you want to play the Matrix Game?")
    game = input("Enter Y for Yes or N for No:\t")
    while game.lower() in ['y' or 'yes'] and game.lower() not in ['n', 'no']:
        fmatrix = first_matrix()
        smatrix = second_matrix()
        print("First Matrix\t\t\tSecond Matrix")
        for value in range(len(fmatrix)):
            print(fmatrix[value],"\t\t\t", smatrix[value])
        operation = matrix_operation()
        print(operation)
        if operation == 'a':
            result = np.add(fmatrix, smatrix)
        elif operation == 'b':
            result = np.subtract(fmatrix, smatrix)
        elif operation == 'c':
            result = np.matmul(fmatrix, smatrix)
        elif operation == 'd':
            result = np.multiply(fmatrix, smatrix)
        display_result(result)
        print("\nDo you want to continue playing the Matrix Game?")
        game = input("Enter Y for Yes or N for No:\t")
    print("*******************************************************************")
    for value in range(10):
        print("Password number ", value+1, ":\n")
        message = generate_password()
        message = message.encode()
        print(hashlib.md5(message).hexdigest())
        print(hashlib.sha256(message).hexdigest())
        print(hashlib.sha512(message).hexdigest())
    time.sleep(20)

if __name__ == "__main__":
    main()
