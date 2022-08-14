# Self Assessment

You can use the [editor on GitHub](https://github.com/acaprio/acaprio.github.io/edit/main/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

# Code Review

ADD LINK TO VIDEO HERE
[Link](url)

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

# Enhancement One

### Artifact Selection
The artifact used in this enhancement was originally written in August 2018 for the course IT-145 Foundations in Application Development. It is a program written in Java that allows zookeepers to monitor animals and habitats. It takes user input to display information saved on a text file. 

### Justification
I chose to include this artifact to showcase innovative techniques and skills by transferring the program from Java to Python. This will also showcase my understanding of the language and its best coding practices. Being capable of successfully transferring code from one language to another is an important skill. It not only showcases the writer’s skill and education across multiple languages, but can be beneficial professionally. Companies often have various pieces of software to maintain that could be written in different languages. Having a solid understanding of how one language relates to another can aid in bringing a more cohesive understanding of how different applications can communicate with each other. 

### Reflection
Transferring from Java to Python was a bit of a challenge. The original program was written using NetBeans IDE, which I didn’t have set up for Python. I did some internet searching and found that while Python plugins are available, it isn’t supported directly by Oracle. I ended up using Visual Studio to rewrite the code in Python, as it was already set up from previous classes. I haven’t had a coding class in a while, so it took some time remembering how to set things up. Once I had the IDE situated, the actual writing into Python wasn’t overly difficult. I ended up commenting out most of the rewrite and then tested in order of execution until I was confident the entire program would work. I did not update any formatting of the outputted menus, or fix any inefficiencies, as that will be covered in my Milestone 3 enhancement plan. Doing this part of the enhancement first allowed me to see the program again and pick out any parts I want to update later. It worked as a great way to do a more in-depth review of the code. 

### Code:
[Enhancement One Artifact](https://github.com/acaprio/acaprio.github.io/tree/main/Enhancement%20One)

# Enhancement Two

### Artifact Selection
The artifact used in this enhancement was originally written in August 2018 for the course IT-145 Foundations in Application Development. It is a program that allows zookeepers to monitor animals and habitats. It takes user input to display information saved on a text file. It was originally written using Java, but was transferred to Python during Enhancement One

### Justification
I chose to include this artifact to showcase my ability of improving efficiency and best coding practices. This code originally had a very confusing menu selection structure. It did not tell the user how to select menu items and expected input as a word, which can be mistyped easily. I changed the structure of the first menu by placing the options in a numbered list that was then outputted. The user is now able to enter a number corresponding to the menu item. The first menu selection then dictates which file is to be read by the system. These second list of options to choose from are then read from that file. The user then inputs the number corresponding to the desired menu option. Another major flaw in the program was how the data was saved. Using a text file does not allow for data manipulation. Changing the text file to a JSON file allows for better a data structure by assigning values to keys.

### Reflection
	The changes were relatively simple, but eliminated the need for guessing when selecting an option. They are also crucial to the program if another developer wanted to ever add to the list of options. Having to guess what words would be input by users as a trigger to select items was confusing and not very efficient use of the coding. This enhancement demonstrates an ability to solve algorithm and data structure inefficiencies while maintaining efficient design. 

### Code:
[Enhancement Two Artifact](https://github.com/acaprio/acaprio.github.io/tree/main/Enhancement%20Two)

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
