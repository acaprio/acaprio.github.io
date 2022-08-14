# * Zookeeper Monitoring System
# * Will ask for input and display cooresponding information
# * from the specified file
# * @author acaprio

import json


# Opens animal file to be read 
# containing list of animals and information about their care 
def animalFile():
    file = open('animals.json',"r")
    data = json.loads(file.read())
    return data

# Opens habitat file to be read 
# containing list of habitats and information on their status   
def habitatFile():  
    file = open('habitats.json',"r")
    data = json.loads(file.read())
    return data

def main():
    # set up of variables
    firstOption = ""    #first menu option - string
    secondOption = ""   #second menu option - string
    exit = False        #exit - boolean
    contents = ""       #file contents - string
    details = {}        #details read from file - dictionary

    # Initial welcome message and loop till exit is true (chosen by user)
    print("Welcome to the ABC Zoo monitoring system.\n")
    while (not exit) :
        # will ask for menu until user exits
        # display first menu options
        print("Please select an option to monitor")
        firstOption = input("1. animal\n2. habitat\n3. exit\n")
        # switch for first options chosen by user
        if (firstOption=="3"):
            exit = True
            print("\nGoodbye!\n")
            break
        # switch for option 2 chosen by user
        # will print the details for desired animal or habitat
        elif (firstOption=="1"):
            details = animalFile()
            print("\nPlease select an option to see details:")
            print("1. Lions\n2. Tigers\n3. Bears\n4. Giraffes")
            secondOption = input()
            output = ""
            if (secondOption=="1"):
                print(details['Lion'])
            elif(secondOption=="2"):
                print(details['Tiger'])
            elif(secondOption=="3"):
                print(details['Bear'])
            elif(secondOption=="4"):
                print(details['Giraffe'])
            else:
                print("Invalid entry.")
                continue
        elif(firstOption=="2"):
            details = habitatFile()
            print("\nPlease select an option to see details:")
            print("1. Penguin Habitat\n2. Bird House\n3. Aquarium")
            secondOption = input()
            output = ""
            if (secondOption=="1"):
                print(details['Penguin'])
            elif(secondOption=="2"):
                print(details['Bird House'])
            elif(secondOption=="3"):
                print(details['Aquarium'])
            else:
                print("Invalid entry.")
                continue
        else:
            print("Invalid entry.")
            continue



if __name__=="__main__":
    main()
