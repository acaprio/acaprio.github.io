# * Zookeeper Monitoring System
# *
# * @author acaprio


# Opens animal file containing list of animals and information about their care 
def animalFile():
    file = open("animals.txt","r")
    return file.read()

# Opens habitat file containing list of habitats and information on their status   
def habitatFile():  
    file = open("habitats.txt","r")
    return file.read()

def main():
    # set up of variables
    firstOption = ""
    secondOption = ""
    exit = False
    contents = ""

    # Initial welcome message and loop till exti is chosen
    print("Welcome to the zoo monitoring system.")
    while (not exit) :
        # will ask for menu until user exits
        # display first menu options
        print("Would you like to monitor an animal, habitat, or exit?")
        firstOption = input()
        # switch for first options chosen by user
        if (firstOption.lower()=="exit"):
            exit = True
            print("Goodbye!")
            break
        elif(firstOption.lower()=="animal"):
            contents = animalFile()
        elif(firstOption.lower()=="habitat"):
            contents = habitatFile()
        else:
            print("Invalid entry.")
            continue

        # takes data returned from file read methods and will split the
        # file contents. index 0 is the list of second options.
        file = contents.split("\n\n")
        print("\nPlease select an option:")
        print(file[0])
        secondOption = input()
        output = ""
        # switch includes both sigular and plural for each animal or
        # habitat name. will output the correct index of String output
        # based on the user choice
        if (secondOption.lower()=="lion" or secondOption.lower()=="lions"):
            output = file[1]
        elif(secondOption.lower()=="tiger" or secondOption.lower()=="tigers"):
            output = file[2]
        elif(secondOption.lower()=="bear" or secondOption.lower()=="bears"):
            output = file[3]
        elif(secondOption.lower()=="giraffe" or secondOption.lower()=="giraffes"):
            output = file[4]
        elif(secondOption.lower()=="penguin" or secondOption.lower()=="penguins"):
            output = file[1]
        elif(secondOption.lower()=="bird" or secondOption.lower()=="birds"):
            output = file[2]
        elif(secondOption.lower()=="aquarium"):
            output = file[3]
        else:
            print("Incorrect entry. Please try again.")
        # Alert message for any lines containing *'s. Will replace *
        # with ALERT!!!
        if ( "*" in output ) :
            output = output.replace("*****","ALERT!!! ")
        print("\n" + output + "\n")


if __name__=="__main__":
    main()

