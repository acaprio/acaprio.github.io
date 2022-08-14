# * Zookeeper Monitoring System
# * Will ask for input and display cooresponding information
# * from the specified file
# * @author acaprio

import json


# Opens file to be read (animal or habitat....passed by user via menu options)
# containing list of animals and information about their care 
def fileRead(fileName):
    file = open(fileName,"r")
    data = json.loads(file.read())
    n = 1 # counter variable to iterating through keys
    print("\nPlease select an option to see details:")
    for key in data.keys():
        print(n, key)
        n+=1
    secondOption = int(input())
    # keyIndex for comparing to secondOption
    # for loop will itterate through the keys to see if keyIndex matches
    # Then will print the values for the desired key
    keyIndex = 1
    for key in data.keys():
       if (keyIndex == secondOption):
           print(data[key])
           break
       else: 
           keyIndex+=1

    file.close()
    return

def fileCreate(fileName):
    file = open(fileName,"r")
    data = json.loads(file.read())
    # get new info to be added depending on animal or habitat
    if (fileName == 'animals.json'):
        newKey = input("Enter species of animal to add:\n")
        newName = input("Enter the name:\n")
        newAge = input("Enter the age:\n")
        newHealth = input("Enter health concerns:\n")
        newFeeding = input("Enter feeding schedule:\n")
        data[newKey] = {'name': newName, 'age': newAge, 'health': newHealth, 'feeding': newFeeding}
    else:
        newKey = input("Enter type of habitat to add:\n")
        newTemperature = input("Enter habitat temperature:\n")
        newFoodSource = input("Enter food source status:\n")
        newCleanliness = input("Enter cleanliness level:\n")
        data[newKey] = {'Temperature': newTemperature, 'Food Source': newFoodSource, 'Cleanliness': newCleanliness}
    # save data back to file. 
    with open(fileName, "w") as f:
        f.write(json.dumps(data, indent=4))
    print("\n",newKey, "has been added")
    print(data[newKey])
    file.close()
    return 

def fileUpdate(fileName):
    file = open(fileName, "r")
    data = json.loads(file.read())
    n = 1 # counter variable to iterating through keys
    print("\nPlease select an option to update:")
    for key in data.keys():
        print(n, key)
        n+=1
    secondOption = int(input())
    # keyIndex for comparing to secondOption
    # for loop will itterate through the keys to see if keyIndex matches
    # will then update the data associated with key per user input
    keyIndex = 1
    for key in data.keys():
       if (keyIndex == secondOption):
           if(fileName == 'animals.json'):
               print(data[key])
               print("\nWhich parameter will be updated?")
               print("1 Name\n2 Age\n3 Health\n4 Feeding")
               updateOption = int(input())
               if(updateOption == 1):
                   newParameter = 'name'
               elif(updateOption == 2):
                   newParameter = 'age'
               elif(updateOption == 3):
                   newParameter = 'health'
               elif(updateOption == 4):
                   newParameter = 'feeding'
           else:
               print(data[key])
               print("\nWhich parameter will be updated?")
               print("Temperature\nFood Sourse\nCleanliness")
               updateParameter = int(input())
               if(updateOption == 1):
                   newParameter = 'Temperature'
               elif(updateOption == 2):
                   newParameter = 'Food Source'
               elif(updateOption == 3):
                   newParameter = 'Cleanliness'

           updateValue = input("\nEnter the new value?\n")
           data[key][newParameter] = updateValue
           # save data back to file. 
           with open(fileName, "w") as f:
               f.write(json.dumps(data, indent=4))
           print("\n",key, "has been updated")
           print(data[key])
           break
       else: 
           keyIndex+=1

    file.close()
    return

def fileDelete(fileName):
    file = open(fileName,"r")
    data = json.loads(file.read())
    n = 1 # counter variable to iterating through keys
    print("\nPlease select an option to delete:")
    for key in data.keys():
        print(n, key)
        n+=1
    secondOption = int(input())
    # keyIndex for comparing to secondOption
    # for loop will itterate through the keys to see if keyIndex matches
    # will then delete the data associated with key
    keyIndex = 1
    for key in data.keys():
       if (keyIndex == secondOption):
           del data[key]
           # save data back to file. 
           with open(fileName, "w") as f:
               f.write(json.dumps(data, indent=4))
           print(key, "has been deleted\n")
           break
       else: 
           keyIndex+=1

    file.close()
    return

def main():
    # set up of variables
    firstOption = ""    #first menu option - string
    secondOption = ""   #second menu option - string
    exit = False        #exit - boolean
    contents = ""       #file contents - string

    # Initial welcome message and loop till exit is true (chosen by user)
    print("Welcome to the ABC Zoo monitoring system.")
    while (not exit) :
        # will ask for menu until user exits
        # display first menu options
        print("\nPlease select an option:\nTo Monitor\t\tOther Options")
        firstOption = input("1 Animal\t\t8 Modify Data\n2 Habitat\t\t9 Exit\n")
        # switch for first options chosen by user
        if (firstOption=="9"):
            exit = True
            print("\nGoodbye!\n")
            break
        elif (firstOption=="1"):
            fileRead('animals.json')
        elif (firstOption=="2"):
            fileRead('habitats.json')
        elif (firstOption=="8"):
            print("\nPlease select an option\n")
            print("1 Create Animal Record\n2 Update Animal Record\n3 Delete Animal Record\n")
            print("4 Create Habitat Record\n5 Update Habitat Record\n6 Delete Habitat Record\n")
            modifyOption = input()
            if (modifyOption=="1"):
                fileCreate('animals.json')
            elif (modifyOption=="2"):
                fileUpdate('animals.json')
            elif (modifyOption=="3"):
                fileDelete('animals.json')
            elif (modifyOption=="4"):
                fileCreate('habitats.json')
            elif (modifyOption=="5"):
                fileUpdate('habitats.json')
            elif (modifyOption=="6"):
                fileDelete('habitats.json')
            else:
                print("Invalid Entry")
        else:
            print("Invalid entry.")
            continue



if __name__=="__main__":
    main()

