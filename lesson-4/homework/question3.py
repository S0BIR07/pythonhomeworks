ends = []
vowels = ['a','o','u','i','e']
txt = input("Input the txt: ")
new_txt = txt[:3]
index=2
while(index<len(txt)-1):
    if(txt[index] in vowels or txt[index] in ends):
        new_txt+=txt[index+1]
        index+=1
    else:
        new_txt=new_txt+"_"+txt[index+1:index+4]
        ends.append(txt[index])
        index+=3
print(new_txt)