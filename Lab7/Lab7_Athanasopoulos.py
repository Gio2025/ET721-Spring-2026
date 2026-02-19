"""
George Athanasopoulos
Feb 19, 2026
Lab 7, working with data in Python
"""

print("\n----- Example 1: Read file ----- ")
with open("phrases.txt", "r") as file1:
    filecontent = file1.read(30)
    print(filecontent)
    filecontent = file1.read(5)
    print(filecontent)

# Check if the file is closed.
print(f"Is the file closed? {file1.closed}")


print("\n----- Example 2: Readline file ----- ")
with open("phrases.txt", "r") as file1:
    filecontent = file1.readline(30)
    print(filecontent)
    filecontent = file1.readline(5)
    print(filecontent)


print("\n----- Example 3: Readlines file ----- ")
# Readlines makes a list of all the lines in the text file. Each line is an item in the list.
with open("phrases.txt", "r") as file1:
    filecontent = file1.readlines()
    print(filecontent)
    filecontent = file1.readlines(5)
    print(filecontent)


print("\n----- Example 4: Loop through each line in a file ----- ")
# Readlines makes a list of all the lines in the text file. Each line is an item in the list.
with open("phrases.txt", "r") as file1:
    filecontent = file1.readlines()
    for eachline in filecontent:
        print(eachline.strip())     # strip() method removes \n in each line.


print("\n----- Example 5: Create file ----- ")
# "W" mode creates a file if the file doesn't exist. On the other hand, if the file exists, "W" mode will overwrite the data in the file.
with open("Athanasopoulos.txt", "w") as file:
    file.write("Python basics for data science\n")
    file.write("Athanasopoulos")
    

print("\n----- Example 6: Append data to an existing file ----- ")
# Append the date and time into "Athanasopoulos.txt" file
from datetime import datetime
with open("Athanasopoulos.txt", "a") as file:
    file.write(f"\nLast update: {datetime.now()}")


print("\n----- Example 7: Copy a file ----- ")
# Copy file "Athanasopoulos.txt" into a new file
with open("Athanasopoulos.txt", "r") as readfile:
    with open("newfile.txt", "w") as writefile:
        for eachline in readfile:
            writefile.write(eachline)


print("\n----- Example 8: Pandas a file ----- ")
import pandas as pd

data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age'  : [25, 30, 35] 
}
df = pd.DataFrame(data)
print(df)


print("\n----- Example 9: Creating df with pandas from an excel file ----- ")
df = pd.read_excel("classdata.xlsx")
print(df)
print(df.head())



print("\n----- EXERCISE ----- ")
def email_read(filename):
    gmail_count = 0
    yahoo_count = 0
    hotmail_count = 0
    
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "gmail" in line:
                    gmail_count += 1
                elif "yahoo" in line:
                    yahoo_count += 1
                elif "hotmail" in line:
                    hotmail_count += 1

        
        with open("reportemail.txt", "w") as email:
            email.write(f"gmail  : {gmail_count}")
            email.write(f"yahoo  : {yahoo_count}")
            email.write(f"hotmail: {hotmail_count}")

            print(f"gmail   = {gmail_count}")
            print(f"yahoo   = {yahoo_count}")
            print(f"hotmail = {hotmail_count}")

        return gmail_count, yahoo_count, hotmail_count
    
    except FileNotFoundError:
        print("Error: The file was not found")

email_read("user_email.txt")
