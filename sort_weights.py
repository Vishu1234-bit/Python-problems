def isPerfectSquare(num):
    if(num==1):
        return True
    half = num//2
    for i in range(2,half):
        if(i*i==num):
            return True
    return False
num=list(map(int,input().split(" ")))
def sortWeights(arr):
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            if(arr[i][1]>arr[j][1]):
                arr[i],arr[j]=arr[j],arr[i]
    return arr
setWeight = {}
for i in num:
    weight=0
    if(isPerfectSquare(i)):
        weight+=5
    if(i%4==0 and i%6==0):
        weight+=4
    if(i%2==0):
        weight+=3
    setWeight[i]=weight
setWeightArr =[]
for w in setWeight:
    setWeightArr.append([w,setWeight[w]])
setWeightArr = sortWeights(setWeightArr)
for i in setWeightArr:
    print("<",i[0],",",i[1],">")
