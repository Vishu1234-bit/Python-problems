def sqrt(n):
    half = n//2
    for i in range(2,half):
        if(i*i>=n):
            return i
string = input()
length = len(string)
n = sqrt(length)
matrix=[]
index=0
for i in range(0,n):
    row=[]
    for j in range(0,n):
        if(index==len(string)):
            row.append('')
        else:
            row.append(string[index])
        index+=1
    matrix.append(row)
for i in range(0,n):
    for j in range(0,n):
        print(matrix[i][j],end=" ")
    print('\n')
stringToFind = input()
start,end=[0,0],[0,0]
for i in range(0,n):
    for j in range(0,n):
        if(matrix[i][j]==stringToFind[0]):
            k=j
            c=0
            while(matrix[i][k]==stringToFind[c] and c!=len(stringToFind)):
                k+=1
                c+=1
                if(k==n or c==len(stringToFind)):
                    break
            if(c==len(stringToFind)):
                start = [i,j]
                end = [i,k-1]
                break
for i in range(0,n):
    for j in range(0,n):
        print(matrix[j][i])
        if(matrix[j][i]==stringToFind[0]):
            k=j
            c=0
            while(matrix[k][i]==stringToFind[c] and c!=len(stringToFind)):
                k+=1
                c+=1
                if(k==n or c==len(stringToFind)):
                    break
            if(c==len(stringToFind)):
                start = [j,i]
                end = [k-1,i]
                break
print(start,end)
