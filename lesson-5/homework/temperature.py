def convert_cel_to_far(Celsius):
    Fahrenheit=Celsius*9/5+32
    Fahrenheit=round (Fahrenheit,2)
    return Fahrenheit
def convert_far_to_cel(Fahrenheit):
    Celsius=(Fahrenheit-32)*5/9
    Celsius=round(Celsius,2)
    return Celsius
Far=float(input("Enter a temperature in degrees F: "))
print(f"{Far} degrees F = {convert_far_to_cel(Far)} degrees C")
Cel=float(input("\nEnter a temperature in degrees C: "))
print(f"{Cel} degrees F = {convert_cel_to_far(Cel)} degrees F")