password=input("Enter a password: ")
while(len(password)<8 or password==password.lower()):
    if(len(password)<8):
        password = input("Password is too short. ")
    if(password==password.lower()):
        password = input("Password must contain an uppercase letter. ")
print("Password is strong.")