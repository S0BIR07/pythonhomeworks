import random
from random import choice
person=0
computer=0
while(person<5 and computer<5):
    rand = random.randint(1,3)
    if rand==1: comp="r"
    if rand==2: comp="p"
    if rand==3: comp="s"
    pers = input("Rock, paper, scissors(r,p,s): ")
    pair = [comp,pers]
    if(comp==pers):
        print("Draw!")
        continue
    elif(pair==["r","s"] or pair==["s","p"] or pair==["p","r"]):
        computer+=1
        print("Point for computer!")
        print(f"You: {person}")
        print(f"Computer: {computer}")
        continue
    else:
        person+=1
        print("Point for you!")
        print(f"You: {person}")
        print(f"Computer{computer}")
        continue

if(person==5):
    print("You won!")
else:
    print("You lost!")