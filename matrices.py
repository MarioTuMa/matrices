import math
fout = open("pic.ppm","w")
size = 500
fout.write("P3\n"+str(size)+" "+str(size)+"\n255\n")


pixels = []
for i in range(size):
    pixels.append([])
    for j in range(size):
        pixels[i].append([255,255,255])

def line(x1,y1,x2,y2,r,g,b):
    x1 = round(x1)
    x2 = round(x2)
    y1 = round(y1)
    y2 = round(y2)
    if(x1==x2):
        for i in range(min(y1,y2),max(y1,y2)+1):
            pixels[x1][i]=[r,g,b]
        return
    if(y1==y2):
        for i in range(min(x1,x2),max(x1,x2)+1):
            pixels[i][y1]=[r,g,b]
        return
    m = (y1-y2)/(x1-x2)
    #print(m)
    if(abs(m)<1):
        if(x1>x2):
            line(x2,y2,x1,y1,r,g,b)
            return
        extra = 0
        shift = 0

        for i in range(x1,x2+1):
            pixels[i][y1+shift]=[r,g,b]
            extra += m
            shift=round(extra)
    if(abs(m)>1):
        m = 1/m
        if(y1>y2):
            line(x2,y2,x1,y1,r,g,b)
            return
        extra = 0
        shift = 0

        for i in range(y1,y2+1):
            pixels[x1+shift][i]=[r,g,b]
            extra += m
            shift=round(extra)

def matrixMult(a,b):
    for i in range(len(b)):
        temp = []
        for j in range(len(a)):
            sum = 0
            for k in range(len(a[0])):
                sum+=a[k][j]*b[i][k]
            temp.append(sum)
        b[i] = temp
    return b

def matrixPrint(a):
    for i in range(len(a[0])):
        stri = ""
        for j in range(len(a)):
            stri+=str(a[j][i])+" "
        print(stri)
    print("")

def altitude(p1x,p1y,p2x,p2y,p3x,p3y,r,g,b):
    m23 = (p3y-p2y)/(p3x-p2x)

    Dx = (p2y-p1y-m23*p2x-p1x/m23)/(-m23-1/m23)
    Dy = p2y+m23*(Dx-p2x)
    Dx = int(Dx)
    Dy = int(Dy)
    lineMatrix.append([p1x,p1y,0,1])
    lineMatrix.append([Dx,Dy,0,1])
    crosshair(Dx,Dy,5,255,0,0)



def crosshair(x1,y1,radius,r,g,b):
    lineMatrix.append([x1-radius,y1,0,1])
    lineMatrix.append([x1+radius,y1,0,1])
    lineMatrix.append([x1,y1-radius,0,1])
    lineMatrix.append([x1,y1+radius,0,1])


def median(p1x,p1y,p2x,p2y,p3x,p3y,r,g,b):
    lineMatrix.append([p1x,p1y,0,1])
    lineMatrix.append([int((p2x+p3x)/2),int((p2y+p3y)/2),0,1])
    crosshair(int((p2x+p3x)/2),int((p2y+p3y)/2),5,255,0,0)

def matrixDraw():
    for i in range(len(lineMatrix)):
        if(i%2==0):
            line(lineMatrix[i][0],lineMatrix[i][1],lineMatrix[i+1][0],lineMatrix[i+1][1],0,0,0)

lineMatrix = []

def matrixClear():

    lineMatrix=[]
    return lineMatrix
p1x = 80
p1y = 230
p2x = 380
p2y = 19
p3x = 439
p3y = 490

lineMatrix.append([p1x,p1y,0,1])
lineMatrix.append([p2x,p2y,0,1])
lineMatrix.append([p2x,p2y,0,1])
lineMatrix.append([p3x,p3y,0,1])
lineMatrix.append([p3x,p3y,0,1])
lineMatrix.append([p1x,p1y,0,1])

Hx = int(((p2x*(p1x-p3x)+p2y*(p1y-p3y))*(p3y-p2y)-(p3y-p1y)*(p1x*(p2x-p3x)+p1y*(p2y-p3y)))/((p3x-p2x)*(p3y-p1y)-(p3y-p2y)*(p3x-p1x)))
Hy = int(((p2x*(p1x-p3x)+p2y*(p1y-p3y))*(p3x-p2x)-(p3x-p1x)*(p1x*(p2x-p3x)+p1y*(p2y-p3y)))/((p3y-p2y)*(p3x-p1x)-(p3x-p2x)*(p3y-p1y)))

altitude(p1x,p1y,p2x,p2y,p3x,p3y,128,128,128)
altitude(p2x,p2y,p1x,p1y,p3x,p3y,128,128,128)
altitude(p3x,p3y,p2x,p2y,p1x,p1y,128,128,128)

median(p1x,p1y,p2x,p2y,p3x,p3y,128,128,128)
median(p2x,p2y,p1x,p1y,p3x,p3y,128,128,128)
median(p3x,p3y,p2x,p2y,p1x,p1y,128,128,128)

crosshair(int((Hx+p1x)/2),int((Hy+p1y)/2),5,255,0,0)
crosshair(int((Hx+p2x)/2),int((Hy+p2y)/2),5,255,0,0)
crosshair(int((Hx+p3x)/2),int((Hy+p3y)/2),5,255,0,0)


print("Big Line Matrix")
matrixPrint(lineMatrix)
rotAngle = math.pi/720


matrixDraw()
lineMatrix = matrixClear()

centerx = (Hx+p1x+p2x+p3x)/4
centery = (Hy+p1y+p2y+p3y)/4

rotMatrix = [
[math.cos(rotAngle),math.sin(rotAngle),0,0],
[-math.sin(rotAngle),math.cos(rotAngle),0,0],
[0,0,1,0],
[-centerx*math.cos(rotAngle)+centery*math.sin(rotAngle)+centerx,-centerx*math.sin(rotAngle)-centery*math.cos(rotAngle)+centery,0,1]]
lineMatrix.append([int((p2x+p3x)/2),int((p2y+p3y)/2),0,1])
lineMatrix.append([int((p2x+p3x)/2),int((p2y+p3y)/2),0,1])

print("Rotation Matrix")
matrixPrint(rotMatrix)
print("Line matrix that is actually a dot")
matrixPrint(lineMatrix)
for i in range(1440):
    matrixDraw()
    matrixMult(rotMatrix,lineMatrix)
    if(i%360==0):
        print("Multiplied line matrix that is actually a dot by rot matrix "+str(i)+" times")
        matrixPrint(lineMatrix)

matrixDraw()

for i in range(size):
    for j in range(size):
        fout.write(str(pixels[i][j][0])+" "+str(pixels[i][j][1])+" "+str(pixels[i][j][2])+" ")

    fout.write("\n")
print("The image file is pic.ppm")