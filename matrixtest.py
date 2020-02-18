def matrixMult(a,b):
    for i in range(len(b)):
        temp = []
        for j in range(len(a)):
            sum = 0
            for k in range(len(a[0])):
                sum+=a[k][j]*b[i][k]
            temp.append(sum)
        b[i] = temp


def matrixPrint(a):
    for i in range(len(a[0])):
        stri = ""
        for j in range(len(a)):
            stri+=str(a[j][i])+" "
        print(stri)
    print("")
m1 = [[2,3,7,5],[6,1,9,2],[3,8,1,2],[3,5,2,1]]
m2 = [[2,0,4,9],[1,3,6,5],[1,7,5,8],[2,5,8,7],[6,9,4,8]]
matrixPrint(m1)
matrixPrint(m2)
matrixMult(m1,m2)
matrixPrint(m2)