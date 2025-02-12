#Question1
a=float(input("Enter: "))
print(f"{a:.2f}")

#Question2
first_num=int(input("First number: "))
second_num=int(input("Second number: "))
third_num=int(input("Third number: "))
print("Largest:", max(first_num,second_num,third_num))
print("Smallest:", min(first_num,second_num,third_num))

#Question3
km=float(input("Kilometers: "))
m=km*1000
print(f"{int(m)} meters and {int((m-int(m))*100)} centimeters")

#Question4
a=int(input("Number 1: "))
b=int(input("Number 2: "))
print("Division:", a//b," \nRemainder:", a%b)

#Question5
t=float(input("Celsius: "))
f=t*9/5+32
print(f"Fahreinheit: {float(f)}")

#Question6
n=int(input("Number: "))
print(n%10)

#Question7
number=int(input("Number: "))
if(number%2==0):
    print(f"{int(number)} is even number")
else:
    print(f"{int(number)} is not even number")