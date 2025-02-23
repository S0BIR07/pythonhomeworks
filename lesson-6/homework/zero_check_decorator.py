def check(func):
    def wrapper(a, b):
        if b==0:
            return "Denominator cannot be zero"
        return func(a, b)
    return wrapper
@check
def div(a, b):
    return a / b
a = int(input("Input the first number: "))
b = int(input("Input the second number: "))
print(div(a, b))