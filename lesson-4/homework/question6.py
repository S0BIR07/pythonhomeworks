for i in range(2,100):
    c=0
    for j in range(2,i):
        if(i%j==0): c+=1
    if(c<1): print(i)