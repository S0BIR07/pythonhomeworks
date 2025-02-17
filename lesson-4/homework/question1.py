a = input("Enter elements of list 1: ").split()
b = input("Enter elements of list 2: ").split()
a = [int(x) for x in a]
b = [int(x) for x in b]
ua = [x for x in a if x not in b]
ub = [x for x in b if x not in a]
result = ua + ub
print("Uncommon elements:", result)