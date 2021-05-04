'''1)	“Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation” (Wikipedia).
2)	Variables are containers for storing data values. They are case-sensitive and can change type after they have been set.
3)	“A namespace is a system that has a unique name for each and every object in Python. An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary” (GeeksforGeeks).
4)	Lists use square brackets, are changeable, is ordered and allows duplicate members. A tuple is also a collection of data types but is ordered, unchangeable, allows duplicate members and uses round brackets. The main difference between a list and a tuple is that a tuple is unchangeable where a list is changeable.
5)	You convert a number to a string by using the built-in str() function.
6)	A local variable is declared inside the function’s body or in the local scope and can only be used inside the function.
A global variable can be referenced all throughout the program. A global variable is created in the main body of the code.
7)	Import the built-in module called random then define a range value.
8)	Dictionaries are used to store data values called keys. A dictionary is a collection that is ordered, changeable, does not allow duplicate members and uses curly brackets.
9)	“The self-parameter is a reference to the current instance of the class and is used to access variables that belongs to the class” (W3 Schools).
The self-parameter has to be the first parameter of any function in a class.
10)	 The break keyword is used to break out of a for loop and or a while loop.
The continue keyword is used to end the current iteration in a for loop and or a while loop and continues to the next iteration. The pass statement is used as a placeholder for future code.
11)	List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is ordered and changeable. No duplicate members.
A list can be used as a grocery list because it is changeable.
A tuple can be a list of requirements because it cannot be changed.
A set can be used as a full list of names because it cannot be unindexed.
A dictionary can be used as a reference sheet because a key can be called on.
12)	“When an error occurs, or exception as we call it, Python will normally stop and generate an error message” (W3 Schools). The try block lets you test a block of code for errors.
The except block lets you handle the error. The finally block lets you execute code, regardless of the result of the try and except blocks.
13)	The “#” symbol is a single line comment
14)	Def getList(dict):
Return dict.keys()
	print(getList(dict))
	
15)	“The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number” (W3 Schools). 
Example:  x = range (3, 6)
	for n in x 
	print(n)
16)	The floor division operator gets the floor division of two integers.
17)	A data type is the type of value being typed into code. Different types can do different things such as string, int, float, bool.
18)	The basic types supported areIntegers, floating numbers, complex, strings, bool, built in functions like math and classes, conclusion.
19)	To check if two data types are pointing to the same object then the “is” keyword is used.
20)	“The else keyword in a for loop specifies a block of code to be executed when the loop is finished” (W3 Schools). “With the while else statement
we can run a block of code once when the condition no longer is true” (W3 Schools).
21)	Immutable means you can not modify the value after you create the object and assign a value.
22)	Lists are used to store many items in a single variable, use square brackets, ordered, changeable and allow duplicates.
23)	A tuple is a built-in data type used to store collections of data, is ordered, unchangeable, and allows duplicates.
24)	You choose a list over a tuple when you want the data to be able to be updated or changed.
25)	You get the last value in a list by using a zero-based index. ex [5]
26)	The out-of-range error means that the index you are trying to access does not exist.
27)	So, the descriptor can clean up the file that was open. You also close a file because the object close() flushes any unwritten information and closes
the file after which no more writing can be done.
'''

# 28
def main():
    agian = True
    while agian == True:
        names = ["Dale"]
        user = input("What name are you looking for: ")
        if(user in names):
            print("Hello Dale")
        else:
            print("No Dale")
        redo = input("Do you want to look up another name: (y/n)")
        if(redo != "y"):
            agian = False
main()


# 29
def main():
    agian = True
    while agian == True:
        file = input("what file would you like to open: ")
        open_file = open(file, "r")

        str=open_file.read()

        txt=str.replace('\n', ' ') #remove spaces

        word=txt.split(' ')

        for words in word: # Count spaces

           word_space=' '

           for w in range(len(words)):  #for loop adding the word count

               if(words[w].isalpha()):  # if loop

                   word_space += words[w].lower()

           word[word.index(words)]=word_space

        while(' ' in word):  #set while loop

           word.remove(' ')  #remove spaces

        set_function=set(word)

        print("There are ", len(set_function)," words in this document and the words are:")
             

        for words in set_function:  #set for loop
            print(word)
           
        open_file.close()  #close file

        redo = input("Do you want to open another file:(y/n) ")
        if(redo != "y"):
            agian = False
main()

# 30
import string

def main():
    agian = True
    while agian == True:
        file_path = input("What file would you like to open: ")
        file = None
        words_dict = {}
        try:
            file = open(file_path, "r")

            line = file.readline()
            while(line):
                line = line.strip("\n")
                clean_line = line.translate(str.maketrans('', '', string.punctuation))
                words = clean_line.split(" ")

                for word in words:
                    if (word in words_dict):
                        count = words_dict[word]
                        words_dict[word] = count + 1
                    else:
                        words_dict[word] = 1
                
                line = file.readline()
            
            print(words_dict)
        except Exception as err:
            print("An error occurred:", err)
        finally:
            if (file != None):
                file.close()

        #Do another file?
        redo = input("Do you want to open another file? (y/n): ")
        if (redo != "y"):
            agian= False
main()
