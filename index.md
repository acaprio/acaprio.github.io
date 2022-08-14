# Self Assessment

### Education Overview
Throughout the coursework of this program, I was able to showcase my abilities in a variety of ways. Everything I have learned has better prepared myself for employment in the computer science field. I first learned about collaboration within a team in CS 310 Collaboration and Team Projects. It was also my first-time utilizing git to collaborate with others. I learned the importance of documenting everything and the practical benefits of commenting code. Another course I remember was CS 250 Software Development Lifecycle, which taught me how to communicate the development of software to others in the team, including stakeholders. 
Additionally, CS 260 Data Structures and Algorithms taught me about differing data structures and how to best build and implement them. We created searches and sorting algorithms using C++. The last course I would like to mention is IT 315 Object Oriented Analysis and Design. I learned the importance of design and planning. We explored how to best develop software based on system requirements. It also taught me the importance of use cases, sequence diagrams, and communication diagrams. 

### Portfolio Summary
My portfolio brings together artifacts showing enhancements in three separate categories, Software Engineering and Design, Data Structures and Algorithms, and Databases. I used the same project for each of these categories. The code came from a project written for the course IT 145 Foundations in Application Development and was originally written in 2018 in Java. The purpose of the program is to allow zookeepers a way to manage animals and habitats. The original program saved the relevant information in a text file and would display the appropriate information based on the users’ selections. 
I chose to use the same base code for all three artifacts to demonstrate my mastery of each category in a cohesive way. Each enhancement was built upon the previously enhanced code. This allowed me to tie each enhancement together in a way that demonstrates my ability to further adapt a program while mitigating design flaws at each step. 
My first enhancement demonstrates my ability to use innovative techniques and skill by transferring the original Java code to Python. This also showcases my knowledge of both languages. In order to transfer from one language to another you need to have an understanding of the current language, so you know how best to translate into another. It also demonstrated my ability to deliver a technically sound product while using Python best coding practices. 
The second enhancement took the transferred code and improved the efficiency and data structure. I restructured the menus within the main code to better align with best coding practices. I also reconstructed the data to a JSON object demonstrating my knowledge of object-oriented coding. This artifact also showcases my ability to enhance data structures while managing trade-offs in the design. 
The third enhancement demonstrates my knowledge of databases and data manipulation by adding CRUD functionality. The read portion of CRUD already existed, but I added methods for create, update, and delete. I also further enhanced the efficiency of the code by consolidating code that was redundant. This artifact demonstrates my ability to use innovative techniques and skills. 

# Code Review

ADD LINK TO VIDEO HERE
[Link](url)

# Enhancement One

### Artifact Selection
The artifact used in this enhancement was originally written in August 2018 for the course IT-145 Foundations in Application Development. It is a program written in Java that allows zookeepers to monitor animals and habitats. It takes user input to display information saved on a text file. 

### Justification
I chose to include this artifact to showcase innovative techniques and skills by transferring the program from Java to Python. This will also showcase my understanding of the language and its best coding practices. Being capable of successfully transferring code from one language to another is an important skill. It not only showcases the writer’s skill and education across multiple languages, but can be beneficial professionally. Companies often have various pieces of software to maintain that could be written in different languages. Having a solid understanding of how one language relates to another can aid in bringing a more cohesive understanding of how different applications can communicate with each other. 

### Reflection
Transferring from Java to Python was a bit of a challenge. The original program was written using NetBeans IDE, which I didn’t have set up for Python. I did some internet searching and found that while Python plugins are available, it isn’t supported directly by Oracle. I ended up using Visual Studio to rewrite the code in Python, as it was already set up from previous classes. I haven’t had a coding class in a while, so it took some time remembering how to set things up. Once I had the IDE situated, the actual writing into Python wasn’t overly difficult. I ended up commenting out most of the rewrite and then tested in order of execution until I was confident the entire program would work. Doing this part of the enhancement first allowed me to see the program again and it worked as a great way to do a more in-depth review of the code. 

### Code
[Enhancement One Artifact](https://github.com/acaprio/acaprio.github.io/tree/main/Enhancement%20One)

# Enhancement Two

### Artifact Selection
The artifact used in this enhancement was originally written in August 2018 for the course IT-145 Foundations in Application Development. It is a program that allows zookeepers to monitor animals and habitats. It takes user input to display information saved on a text file. It was originally written using Java, but was transferred to Python during Enhancement One.

### Justification
I chose to include this artifact to showcase my ability of improving efficiency and best coding practices. This code originally had a very confusing menu selection structure. It did not tell the user how to select menu items and expected input as a word, which can be mistyped easily. I changed the structure of the first menu by placing the options in a numbered list that was then outputted. The user is now able to enter a number corresponding to the menu item. The first menu selection then dictates which file is to be read by the system. These second list of options to choose from are then read from that file. The user then inputs the number corresponding to the desired menu option. Another major flaw in the program was how the data was saved. Using a text file does not allow for data manipulation. Changing the text file to a JSON file allows for better a data structure by assigning values to keys.

### Reflection
The changes were relatively simple, but eliminated the need for guessing when selecting an option. They are also crucial to the program if another developer wanted to ever add to the list of options. Having to guess what words would be input by users as a trigger to select items was confusing and not very efficient use of the coding. This enhancement demonstrates an ability to solve algorithm and data structure inefficiencies while maintaining efficient design. 

### Code
[Enhancement Two Artifact](https://github.com/acaprio/acaprio.github.io/tree/main/Enhancement%20Two)

# Enhancement Three

### Artifact Selection
The artifact used in this enhancement was originally written in August 2018 for the course IT-145 Foundations in Application Development. It is a program that allows zookeepers to monitor animals and habitats. It takes user input to display information saved on a text file. It was originally written using Java, but was transferred to Python during Enhancement One.

### Justification
I chose to include this artifact to showcase innovative techniques and skills by adding create, update, and delete functionality. The code originally only had read capabilities. The methods added to accomplish these changes demonstrate my skills in implementing computing solutions that deliver value for my target audience of zookeepers. I also further enhanced the code to allow for the added CRUD capabilites by creating menu options that pull from the JSON file instead of being coded directly. 

### Reflection
Enhancing this artifact did provide some challenges. I didn’t want to hard code the menu options because that wouldn’t allow for additions to be done when adding records. It took a while to figure out how to do the updating and creating without explicitly calling out the key the values should be saved to. I was working with 2 independent files and didn’t want to repeat the code too much. I tried to make the code as generic as possible so anyone could hopefully expand what is built currently. 

### Code
[Enhancement Two Artifact](https://github.com/acaprio/acaprio.github.io/tree/main/Enhancement%20Three)
