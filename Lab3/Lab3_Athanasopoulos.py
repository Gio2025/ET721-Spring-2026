"""
George Athanasopoulos
Feb 3, 2026
Lab 3, conditional statement and loop in python
"""

print("\n ----- Example 1: Set-up of conditional statement -----")
# conditional statement states the flow of the program
age = 11
if(age >= 21 and age <=100):
    print("You are an adult!")
elif(age < 21 and age >=12):
    print("You are a teen!")
elif(age < 12 and age >0):
    print("You are a kid!")


print("\n ----- Example 2: For loop -----")
# for loop as a counter from 9 to 1, step of 1
for n in range(9, 0, -1):
    print(n)


print("\n ----- Example 3: For loop in a list -----")
#for loop in a list
count_negative = 0
numbers = [3, 6, 1, -8, 9, -5]
for m in numbers:
    if m < 0:
        count_negative += 1
else:
    print(f"There is/are {count_negative} negative numbers")
# for-else, the else statement will run only after the completion of all iterations in the for loop
print('\nEND OF PROGRAM')


print("\n ----- Example 4: While loop as a counter -----")
# while loop to print from -3 to 5, inclusive, step of 2.    output --> -3 -1 1 3 5
x = -3
while x <=5:
    print(x)
    x += 2


print("\n ----- Example 5: While loop to validate an input -----")
# program collects a number from the user and print if the number is even or odd
# after it, the program will ask the user if another number will be tested
# if the user types 'y' or 'Y', then the program will run again
# if the user types any other character that is not 'y' or 'Y', the program will stop
decision_user = 'y'
user_number = 0
while True:
    user_number = int(input("Enter a number: "))
    if user_number % 2 == 0 and user_number != 0:
        print(f"{user_number} is EVEN")
    elif user_number == 0:
        print(f"{user_number} is ZERO")
    else:
        print(f"{user_number} is ODD")
    decision_user = input("Do you want another run? y or Y for yes: ")
    if decision_user != 'y' and decision_user != 'Y':
        break


print("\n ----- EXERCISE A -----")
# use while loop to validate that the 'user_number' is between 1 and 9
while True:
    user_number = int(input("Enter a number between 1 and 9: "))
    if user_number >= 1 and user_number <= 9:
        print(f"Number inputted: {user_number}")
        break
    else:
        print("Inputted number is not between 1 and 9. ")


print("\n ----- EXERCISE B -----")
# use loop to allow the user to guess the number three times. If the user guesses the number before the third attempt, 
# the program should end (break).
attempts_left = 3
number = 8
while attempts_left > 0:
    guess = int(input(f"Guess the number between 1 and 10 ({attempts_left} attempts left): \n"))

    if guess < 1 or guess > 10:
        print("Number not within range!")
        attempts_left -= 1
    elif guess == number:
        attempts_left -= 1
        print(f"Correct, the number was {number}!")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print("Incorrect guess. Try again!")

if attempts_left == 0 and guess != number:
    print(f"Out of attempts! The number was {number}.")
