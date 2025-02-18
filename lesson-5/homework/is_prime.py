def is_prime(n):
    if n>0:
        for i in range(2,n):
            if n%i!=0:
                return True
            else:
                return False
    elif n==1:
        return False
    else:
        print("Your number should be positive!")
num=int(input("Enter a number: "))
print(is_prime(num))