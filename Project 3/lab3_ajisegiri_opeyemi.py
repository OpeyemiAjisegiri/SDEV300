""" This program is a secure python based Population Census Program
    through which a user can display, update and analyze the population
    census nd state detail of any state in the country. """
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#Global variable detailling the States, State Capital,
#Population, and State Flower of each state.
state_details =  {'Alabama':{'State': 'Alabama','Capital': 'Montgomery', 'population': 4887681,
                              'flower':'lab3_state_flowers/alabama.jpg'},
                'Maryland':{'State': 'Maryland','Capital': 'Annapolis', 'population': 6035802,
                             'flower':'lab3_state_flowers/maryland.jpg'},
                'Virginia':{'State':'Virginia','Capital': 'Richmond', 'population': 8501286,
                            'flower':'lab3_state_flowers/virginia.jpg'},
                'Florida':{'State': 'Florida','Capital': 'Tallahassee', 'population': 21244317,
                           'flower':'lab3_state_flowers/florida.jpg'},
                'Washington':{'State': 'Washington', 'Capital': 'Olympia', 'population': 7523869,
                            'flower':'lab3_state_flowers/washington.jpg'},
                'Connecticut': {'State':'Connecticut','Capital':'Hartford','population': 3571520,
                             'flower':'lab3_state_flowers/connecticut.jpg'},
		'Alaska':{'Capital':'Juneau','State':'Alaska','population':735139,
                          'flower':'lab3_state_flowers/alaska.jpg'},
		'Arizona':{'Capital':'Phoenix','State':'Arizona','population':7158024,
                           'flower':'lab3_state_flowers/arizona.jpg'},
		'Arkansas':{'Capital':'Little Rock','State':'Arkansas','population':3009733,
                            'flower':'lab3_state_flowers/arkansas.jpg'},
		'California':{'Capital':'Sacramento','State':'California','population':39461588,
                              'flower':'lab3_state_flowers/california.jpg'},
		'Colorado':{'Capital':'Denver','State':'Colorado','population':	5691287,
                            'flower':'lab3_state_flowers/colorado.jpg'},
		'Delaware':{'Capital':'Dover','State':'Delaware','population':965479,
                            'flower':'lab3_state_flowers/delaware.jpg'},
		'West Virginia':{'Capital':'Charleston','State':'West Virginia','population':1804291,
                            'flower':'lab3_state_flowers/west_virginia.jpg'},
		'Wisconsin':{'Capital':'Madison','State':'Wisconsin','population':5807406,
                             'flower':'lab3_state_flowers/wisconsin.jpg'},
		'Wyoming':{'Capital':'Cheyenne','State':'Wyoming','population':577601,
                           'flower':'lab3_state_flowers/wyoming.jpg'},
		'Georgia':{'Capital':'Atlanta','State':'Georgia','population':10511131,
                           'flower':'lab3_state_flowers/georgia.jpg'},
		'Hawaii':{'Capital':'Honolulu','State':'Hawaii','population':1420593,
                          'flower':'lab3_state_flowers/hawaii.jpg'},
		'Idaho':{'Capital':'Boise','State':'Idaho','population':1750536,
                         'flower':'lab3_state_flowers/idaho.jpg'},
		'Illinois':{'Capital':'Springfield','State':'Illinois','population':12723071,
                            'flower':'lab3_state_flowers/illinois.jpg'},
		'South Dakota':{'Capital':'Pierre','State':'South Dakota','population':878698,
                            'flower':'lab3_state_flowers/south_dakota.jpg'},
		'Tennessee':{'Capital':'Nashville','State':'Tennessee','population':6771631,
                             'flower':'lab3_state_flowers/tennessee.jpg'},
		'Texas':{'Capital':'Texas','State':'Illinois','population':28628666,
                         'flower':'lab3_state_flowers/texas.jpg'},
		'Utah':{'Capital':'Salt Lake City','State':'Utah','population':3153550,
                        'flower':'lab3_state_flowers/utah.jpg'},
		'Vermont':{'Capital':'Montpelier','State':'Vermont','population':624358,
                           'flower':'lab3_state_flowers/vermont.jpg'},
		'Indiana':{'Capital':'Indianapolis','State':'Indiana','population':6695497,
                           'flower':'lab3_state_flowers/indiana.jpg'},
		'Iowa':{'Capital':'Des Moines','State':'Iowa','population':3148618,
                        'flower':'lab3_state_flowers/iowa.jpg'},
		'Kansas':{'Capital':'Topeka','State':'Kansas','population':2911359,
                        'flower':'lab3_state_flowers/kansas.jpg'},
		'South Carolina':{'Capital':'Columbia','State':'South Carolina','population':5084156,
                        'flower':'lab3_state_flowers/south_carolina.jpg'},
		'Kentucky':{'Capital':'Frankfort','State':'Kentucky','population':4461153,
                        'flower':'lab3_state_flowers/kentucky.jpg'},
		'Rhode Island':{'Capital':'Providence','State':'Rhode Island','population':1058287,
                        'flower':'lab3_state_flowers/rhode_island.jpg'},
		'Louisiana':{'Capital':'Baton Rouge','State':'Louisiana','population':4659690,
                        'flower':'lab3_state_flowers/louisiana.jpg'},
		'Pennsylvania':{'Capital':'Harrisburg','State':'Pennsylvania','population':12800922,
                        'flower':'lab3_state_flowers/pennsylvania.jpg'},
		'Maine':{'Capital':'Augusta','State':'Maine','population':1339057,
                         'flower':'lab3_state_flowers/maine.jpg'},
		'Massachusetts':{'Capital':'Boston','State':'Massachusetts','population':6882635,
                        'flower':'lab3_state_flowers/massachusetts.jpg'},
		'Michigan':{'Capital':'Lansing','State':'Michigan','population':9984072,
                        'flower':'lab3_state_flowers/michigan.jpg'},
		'Minnesota':{'Capital':'St. Paul','State':'Minnesota','population':5606249,
                        'flower':'lab3_state_flowers/minnesota.jpg'},
		'Oregon':{'Capital':'Salem','State':'Oregon','population':4181886,
                        'flower':'lab3_state_flowers/oregon.jpg'},
		'Mississippi':{'Capital':'Jackson','State':'Mississippi','population':2981020,
                        'flower':'lab3_state_flowers/mississippi.jpg'},
		'Oklahoma':{'Capital':'Oklahoma City','State':'Oklahoma','population':3940235,
                        'flower':'lab3_state_flowers/oklahoma.jpg'},
		'Missouri':{'Capital':'Jefferson City','State':'Missouri','population':6121623,
                        'flower':'lab3_state_flowers/missouri.jpg'},
		'Ohio':{'Capital':'Columbus','State':'Ohio','population':11676341,
                        'flower':'lab3_state_flowers/ohio.jpg'},
		'Montana':{'Capital':'Helena','State':'Montana','population':1060665,
                        'flower':'lab3_state_flowers/montana.jpg'},
		'North Dakota':{'Capital':'Bismarck','State':'North Dakota','population':758080,
                        'flower':'lab3_state_flowers/north_dakota.jpg'},
		'North Carolina':{'Capital':'','State':'North Carolina','population':10381615,
                        'flower':'lab3_state_flowers/north_carolina.jpg'},
		'Nebraska':{'Capital':'Lincoln','State':'Nebraska','population':1925614,
                        'flower':'lab3_state_flowers/maryland.jpg'},
		'New York':{'Capital':'Albany','State':'New York','population':19530351,
                        'flower':'lab3_state_flowers/new_york.jpg'},
		'Nevada':{'Capital':'Carson City','State':'Nevada','population':3027341,
                        'flower':'lab3_state_flowers/nevada.jpg'},
		'New Hampshire':{'Capital':'','State':'New Hampshire','population':1353465,
                        'flower':'lab3_state_flowers/new_hamsphire.jpg'},
		'New Jersey':{'Capital':'Trenton','State':'New Jersey','population':8886025,
                        'flower':'lab3_state_flowers/new_jersey.jpg'},
		'New Mexico':{'Capital':'Santa Fe','State':'New Mexico','population':2092741,
                        'flower':'lab3_state_flowers/new_mexico.jpg'}
		}

def menu_display():
    """ Displays the menu options to the user. """
    print("""1. Display all U.S. States in Alphabetical order along
                with the Capital, State Population, and Flower.""")
    print("""2. Search for a specific state and display the appropriate
                Capital name, State Population, and an image of the
                associated State Flower.""")
    print("""3. Provide a Bar graph of the top 5 populated States showing
                their overall population.""")
    print("""4. Update the overall state population for a specific state.""")
    print("5. Exit the program")

def menu_option():
    """ Accepts the menu chosen by the user and validates the input
            before utilizing it in the program. """
    is_valid = False
    while is_valid is False:
        try:
            menu = int(input("Enter a menu option using the number preceeding it:"))
            is_valid = True
        except ValueError:
            print("Enter a numerical value")
    return menu

def specific_state_details():
    """ Prints out the details of a chosen to the screen. """
    valid_state = False
    while valid_state is False:
        state = input("Enter a state:\t")
        if state.isalpha() is True:
            if state in state_details.keys():
                print("\n",state,":\t",state_details[state],"\n")
                flower = state_details[state]['flower']
                img = mpimg.imread(flower)
                imgplot = plt.imshow(img)
                plt.show()
            else:
                print("State not found\n")
            valid_state = True
        else:
            print("Enter a correct state")
            continue

def update_state(state):
    """ Updates the population detail of a specific[chosen] state
        and prints the updated details to the screen. """
    valid_population = False
    while valid_population is False:
        try:
            population = int(input("Enter the recent census:\t"))
            if state in state_details.keys():
                state_details[state]['population'] = population
                print("\n",state,":\t",state_details[state],"\n")
            valid_population = True
        except ValueError:
            print("Enter a numerical value")

def census():
    """ Prints the details of each state to the screen in both the
        ascending and descending order as chosen by the user."""
    valid = False
    while valid is False:
        try:
            order = int(input("Enter order of display,[[1: ASC] OR [2:DSC]]:\t"))
            if order not in range(1,2):
                print("Enter one of the two digits [1 OR 2]")
            valid = True
            if order == 1:
                print("\n")
                for key in sorted(state_details.keys()):
                    print(key, end='   ')
                    print(state_details[key])
                print("\n")
            elif order == 2:
                print("\n")
                for key in sorted(state_details.keys(), reverse=True):
                    print(key, end='   ')
                    print(state_details[key])
                print("\n")
        except ValueError:
            print("Enter a numerical value.")

def most_populated_states():
    """ Prints a bar graph to the screen of the most populated states """
    #temp= sorted(state_details.items(), key = lambda x: x[1]['population'])
    #print(temp)
    temp_list = [i['population'] for i in state_details.values()]
    temp_state = [i['State'] for i in state_details.values()]
    plt.bar(temp_state[-5:],temp_list[-5:])
    plt.show()

def main():
    """ The main function of the program through which the user interacts
            with the program. """
    print("Welcome to the Secure State Details Application")
    menu_display()
    menu = menu_option()
    while menu in range(1,5):
        if menu == 1:
            census()
        elif menu == 2:
            specific_state_details()
        elif menu == 3:

            most_populated_states()
        elif menu == 4:
            valid_state = False
            while valid_state is False:
                state = input("Enter a state:\t")
                if state.isalpha() is True:
                    if state in state_details.keys():
                        update_state(state)
                    else:
                        print("State not found\n")
                    valid_state = True
                else:
                    print("Enter a correct state")
                    continue
        menu_display()
        menu = menu_option()
    print("Thank you for using this application, see you soon.")
    time.sleep(30)

if __name__ == "__main__":
    main()
