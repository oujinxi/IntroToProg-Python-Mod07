# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description:Create a script that demonstrates how Pickling and Structured Error Handling work.
# ChangeLog (Who,When,What):
# Jin,11.27.2019,Created started script

# ------------------------------------------------------------------------ #
class numberException(Exception):
    def __str__(self):
        return "Please enter an Upper Case Letter, not a Number."
class lowerException(Exception):
    def __str__(self):
        return "Please enter an Upper Case Letter, not a Lower Case Letter."
class CustomError(Exception):
    def __str__(self):
        return "There's a custom Error in your Entry, Please try again."
class TooManyLetterException(Exception):
    def __str__(self):
        return "You entered too many letters. Please enter an Upper Case Letter only."

row = []
rows = []
def ErrorHandling ():
    print("Structured Error Handling turns the error condition into structured error messages."
          "\nIt allows the creation of custom error conditions."
          "\nAs I'm demonstrating below, I'm creating a condition for the user Entry."
          "\nIt will keep showing error Messages until the condition is met. \n")
    try:
        Entry = input("Enter a Upper Case Letter: ")
        if len(Entry) == 1:
            if Entry.isnumeric():
                raise numberException()
            elif Entry.islower():
                raise lowerException()
            elif Entry.isupper():
                pass
            else:
                raise CustomError()
        elif len(Entry) > 1:
            raise TooManyLetterException()
        else:
            raise CustomError()

        print("You Entered: " + Entry)
        print("Thank You.")
    except numberException as e:
        print(e)
    except lowerException as e:
        print(e)
    except CustomError as e:
        print(e)
    except TooManyLetterException as e:
        print(e)

def PickleTutor ():
    import pickle

    '''pickling demo'''
    DataOne = input("Write Something Random: ")
    DataTwo = input("Write Something Else Random.")
    DataEntry = [DataOne, DataTwo]
    print("The python pickle module is used to convert the python object into a stream of characters."
          "\nWhile the character stream contains all neccessary information to reconstruct the original object, it doesn't resemble the original."
          "\nOne of the advantage of pickle is that, same object is only serialize once. Meaning it can condense the code for recurring objects.")
    print("Press Enter to continue.")
    input()
    print()
    while (True):
        print("What would you like to do with the entry?")
        print("1. Store into a file in pickle format.")
        print("2. Store into a file in normal txt file.")
        print("3. Load and Read the pickle file.")
        print("4. Load and Read the Txt file.")
        print("5. Do nothing and quit.")

        userchoice = input("Your choice: ")
        if (userchoice.strip() == '1'):
            objFile = open("EntryLog.dat", "ab")
            pickle.dump(DataEntry, objFile)
            objFile.close()
            print("Entry Stored in pickle format.\n")
            continue
        elif (userchoice.strip() == "2"):
            objFile = open("EntryLog.txt", 'a')
            objFile.write(DataEntry[0]+','+DataEntry[1]+'\n')
            objFile.close()
            print("Entry Stored in txt file.\n")
            continue
        elif (userchoice.strip() == "3"):
            objFile = open("EntryLog.dat", "rb")
            objFileData = pickle.load(objFile)
            while (True):
                try:
                    print(objFileData)
                    objFileData = pickle.load(objFile)
                except EOFError:
                    break
        elif (userchoice.strip() == "4"):
            objFile = open("EntryLog.txt", "r")
            for line in objFile:
                data = line.split(",")
                row = {"One":data[0].strip(),"Two":data[1].strip()}
                rows.append(row)
            objFile.close()
            print(rows)
        elif (userchoice.strip() == "5"):
            print("Nothing was stored.")
            break
        else:
            print("Please enter 1, 2, or 3.")
            continue
        print()
    print("You can compare the txt file and dat file created from the data entry.")

'''Processing'''
print("What would you like to look at?")
print("1. Error Handling.")
print("2. Pickling.")
userchoice = input("Your Choice: ")
if (userchoice.strip() == '1'):
    ErrorHandling()
elif (userchoice.strip() == '2'):
    PickleTutor()