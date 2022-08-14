/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package monitoringsystem;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 *
 * @author acapr
 */
public class MonitoringSystem {
    
    public static String animalFile() throws FileNotFoundException {
        FileInputStream file = new FileInputStream("animals.txt");
        Scanner inputFile = new Scanner(file);
        String contents = "";
        
        // read the file and append to string contents to be returned
        while(inputFile.hasNext())
        {
            contents = contents + inputFile.nextLine() + "\n";
        }
        return contents;
    }
    
    public static String habitatFile() throws FileNotFoundException {
        FileInputStream file = new FileInputStream("habitats.txt");
        Scanner inputFile = new Scanner(file);
        String contents = "";
        
        // read the file and append to string contents to be returned
        while(inputFile.hasNext())
        {
            contents = contents + inputFile.nextLine() + "\n";
        }
        return contents;
    }

    /**
     * @param args the command line arguments
     * @throws java.io.FileNotFoundException
     */
    public static void main(String[] args) throws FileNotFoundException {
        // set up of scnr and variables
        Scanner scnr = new Scanner(System.in);
        String firstOption = "";
        String secondOption = "";
        boolean exit = false;
        String contents = "";
        
        System.out.println("Welcome to the zoo monitoring system.");
        
        while(!exit){   // will ask for menu until user exits
            
            // display first menu options
            System.out.println("Would you like to monitor an animal, habitat, or exit?");
            firstOption = scnr.nextLine();
            
            // switch for first options chosen by user
            switch (firstOption.toLowerCase()) {
                case "exit":
                    exit = true;
                    System.out.println("Goodbye!");
                    System.exit(0);
                    break;
                case "animal":
                    contents = animalFile();
                    break;
                case "habitat":
                    contents = habitatFile();
                    break;
                default:
                    System.out.println("Invalid entry.");
                    continue;
            }
            
            // takes data returned from file read methods and will split the 
            // file contents. index 0 is the list of seconf options.
            String[] file = contents.split("\n\n");
            System.out.println("\nPlease select an option:");
            System.out.println(file[0]);
            secondOption = scnr.nextLine();
            String output = "";
            
            // switch includes both sigular and plural for each animal or 
            // habitat name. will output te correct index of String output
            // based on the user choice
            switch (secondOption.toLowerCase()){
                case "lion":
                case "lions":
                    output = file[1];
                    break;
                case "tiger":
                case "tigers":
                    output = file[2];
                    break;
                case "bear":
                case "bears":
                    output = file[3];
                    break;
                case "giraffe":
                case "giraffes":
                    output = file[4];
                    break;
                    
                case "penguin":
                case "penguins":
                    output = file[1];
                    break;
                case "bird":
                case "birds":
                    output = file[2];
                    break;
                case "aquarium":
                    output = file[3];
                    break;
                    
                default:
                    System.out.println("Incorrect entry. Please try again.");
                    
            }
            
            // Alert message for any lines containing *'s. Will replace * 
            // with ALERT!!!
            if (output.contains("*")){
                output = output.replace("*****", "ALERT!!! ");
            }
            
            System.out.println("\n" + output + "\n");
            }
        
        
    }
    
}
