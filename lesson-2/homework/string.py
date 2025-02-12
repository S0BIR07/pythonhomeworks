#Question1
name=input("Enter your name: ")
age=int(input("Enter your year of birth: "))
print(f"Your name is {name} and you are {int(2025-age)} years old")

#Question2
txt='LMaasleitbtui'
print("Car 1:", txt[::2], "\nCar 2:", txt[1::2])

#Question3
str=input("String input: ")
print(len(str))
print(str.upper())
print(str.lower())

#Question4
palindrome=input("Enter word: ")
if(palindrome==palindrome[::-1]):
    print(palindrome, "is a palindrome")
else:
    print(palindrome, "is not a palindrome")

#Question5