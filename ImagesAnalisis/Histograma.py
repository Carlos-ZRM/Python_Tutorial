from PIL import Image

import matplotlib.pyplot as plt

def asimetria(l1,l2,l3,m1,m2,m3):
    res = [0,0,0]
    for i in range (len(l1)):
        res[0]=res[0]+(l1[i]-m1)**3
        res[1]=res[1]+(l2[i]-m2)**3
        res[2]=res[2]+(l3[i]-m3)**3
    return res

def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)

def getGreen(greenVal):
    return '#%02x%02x%02x' % (0, greenVal, 0)
   
def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)


image = Image.open("./snakes.jpg")

image.show()

histogram = image.histogram()

l1 = histogram[0:256]
l2 = histogram[256:512]
l3 = histogram[512:768]
ml1 = 0.0
ml2 = 0.0
ml3 = 0.0

plt.figure(0)


for i in range(0, 256):
    ml1 = ml1 + l1[i]
    plt.bar(i, l1[i], color = getRed(i), edgecolor=getRed(i), alpha=0.3)
ml1 = ml1/256
 

# G histogram

plt.figure(1)

for i in range(0, 256):
    ml2 = ml2 + l2[i]
    plt.bar(i, l2[i], color = getGreen(i), edgecolor=getGreen(i),alpha=0.3)
ml2 = ml2/256


# B histogram

plt.figure(2)

for i in range(0, 256):
    ml3 = ml3 + l3[i]
    plt.bar(i, l3[i], color = getBlue(i), edgecolor=getBlue(i),alpha=0.3)
ml3 = ml3/256

asim = asimetria(l1,l2,l3,ml1,ml2,ml3)
print("Histograma canal R ")
print("     Media "+str(ml1))
print("     Asimetria "+str(asim[0]))
print("Histograma canal G ")
print("     Media "+str(ml2))
print("     Asimetria "+str(asim[1]))
print("Histograma canal B ")
print("     Media "+str(ml3))
print("     Asimetria "+str(asim[2]))

plt.show()