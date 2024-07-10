word=input()
first=0
last = len(word)-1
while(first<len(word) and last>=0):
    for index in range(0,len(word)):
        if(index==first or index==last):
            print(word[index],end="")
        else:
            print(" ",end="")
    first+=1
    last-=1
    print("\n")
