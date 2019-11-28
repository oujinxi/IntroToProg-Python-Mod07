### Jin Ou
### Nov. 27, 2019
### Python
### Assignment 7
## **Introduction:**
	To Created a Script that demonstrates how pickling and Structured Error Handling works.
## **Method:**
	The script will consist of two parts, one of structured error handling, and the other for pickling. 
#### Step1:
Create the base frame work to ask for user which part do they want to look at. 
```
print("What would you like to look at?")
print("1. Error Handling.")
print("2. Pickling.")
userchoice = input("Your Choice: ")
```
This is displayed as 
![alt text](https://github.com/oujinxi/IntroToProg-Python-Mod07/blob/master/img%20error%20handling%20choice.jpg "tooltip text")
 
#### Step 2:
Create individual methods for each part in order to have a clean I/O code. 
Starting with the Structured Error Handling part. 
The example I’m using is how to use custom error message to direct the user to give the correct input. First we will need to create a new error class for each custom error, for example:
```
class numberException(Exception):
    def __str__(self):
        return "Please enter an Upper Case Letter, not a Number."
```
The new class is based on the built-in Exception class with a slightly different error message. 
![alt text](https://github.com/oujinxi/IntroToProg-Python-Mod07/blob/master/number%20error.jpg "tooltip text")
Now we set the trigger for the error message. 
```
if Entry.isnumeric():
    raise numberException()
```
If the user input is a number, the error will be triggered in this case. 
 
#### Step 3
Moving on to the pickle tutor. Create a new method for this part, and import pickle file in order to use the corresponding commands. 
Options are provided for the user to store the file into different formats in order to compare the files stored in each of them with the same input. 
There was a big problem I encountered when I tried to read the pickle file. 
Since load only feeds one line at a time, I tried to use a while loop
```
while (True):
    print(objFileData)
    objFileData = pickle.load(objFile)
```
but it kept feeding me an error
 ![alt text](https://github.com/oujinxi/IntroToProg-Python-Mod07/blob/master/img%20error%20handling%20choice.jpg "tooltip text")
I couldn’t figure out how to fix the error, and then I saw some sample codes online bypassing the error with the structured error handling. Since I know the error code, I can simply break the loop when the error pops up.
```
while (True):
    try:
        print(objFileData)
        objFileData = pickle.load(objFile)
    except EOFError:
        break
```

Summary:
	The script was intended to explain structured error handling and pickling through demonstration and examples.

