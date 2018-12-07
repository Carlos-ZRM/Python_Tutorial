from PIL import Image
import Operaciones
import matplotlib.pyplot as plt


def escala ( imgage ):

    img = image.convert('L')
    datos = list(img.getdata())
    aux =[]
    sum = 0
    escala = 0
    for i in range (len(datos)):
        aux= datos[i]
        sum = 000
        for j in range (len(aux)):
            sum+=aux[j]
        sum=sum/len(aux)
        escala = int (sum*.33 + sum*.5 + sum*.15)
        datos[i]= (escala,escala,escala)        
    img.putdata(datos)
    img.save("hist-escala.jpg")
    img.show()
    return result
def asimetria(l1,l2,l3,m1,m2,m3):
    res = [0,0,0]
    for i in range (len(l1)):
        res[0]=res[0]+(l1[i]-m1)**3
        res[1]=res[1]+(l2[i]-m2)**3
        res[2]=res[2]+(l3[i]-m3)**3
    return res
def asimetriaInt(l1,m1):
    res = 0
    for i in range (len(l1)):
        res=res+(l1[i]-m1)**3
    return res
def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)

def getGreen(greenVal):
    return '#%02x%02x%02x' % (0, greenVal, 0)
   
def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)

def histogramaRGB(image):
    image.show()
    i_size = image.size[0]*image.size[1]
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
    

    # G histogram

    plt.figure(1)

    for i in range(0, 256):
        ml2 = ml2 + l2[i] 
        plt.bar(i, l2[i], color = getGreen(i), edgecolor=getGreen(i),alpha=0.3)


    # B histogram

    plt.figure(2)

    for i in range(0, 256):
        ml3 = ml3 + l3[i]
        plt.bar(i, l3[i], color = getBlue(i), edgecolor=getBlue(i),alpha=0.3)


    asim = asimetria(l1,l2,l3,ml1,ml2,ml3)
    print("Histograma canal R ")
    print("     Media "+str(ml1/256))
    print("     Asimetria "+str(asim[0]))
    print("Histograma canal G ")
    print("     Media "+str(ml2/256))
    print("     Asimetria "+str(asim[1]))
    print("Histograma canal B ")
    print("     Media "+str(ml3/256))
    print("     Asimetria "+str(asim[2]))
    plt.show()

def histogramaG(img):
    image = img.convert('L')
    image.show()
    i_size = image.size[0]*image.size[1]
    l1 =  image.histogram()
    ml1=0
    plt.figure(3)
    for i in range(len(l1)):
        ml1 = ml1 + l1[i]
        plt.bar(i, l1[i], color = getRed(i), edgecolor=getRed(i), alpha=0.3)
    plt.savefig("histograma-gs.png")
    asim = asimetriaInt(l1,ml1)
    print("Histograma GrayScale ")
    print("     Media "+str(ml1/256))
    print("     Asimetria "+str(asim))
    plt.show()


def desplazamiento(image,cte):
    img = image.convert('L')
    datos = img.getdata()
    datosn = Operaciones.restaCte(datos, cte)
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datosn)
    imgg.save("hist-escala-desplazamiento.jpg")
    histogramaG(imgg)

def contraccion(image, cmaximo,cminimo):
    img = image.convert('L')
    datos = img.getdata()
    maximo=max(datos)
    minimo=min(datos)
    k = (cmaximo-cminimo)/(maximo-minimo)
    print(str(maximo)+","+str(minimo)+","+str(k))
    datosn = Operaciones.contraccion(datos, k, minimo, cminimo )
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datosn)
    imgg.save("hist-escala-desplazamiento.jpg")
    histogramaG(imgg)

def expansion(image, cmaximo,cminimo):
    img = image.convert('L')
    datos = img.getdata()
    maximo=max(datos)
    minimo=min(datos)
    k = (cmaximo-cminimo)/(maximo-minimo)
    print(str(maximo)+","+str(minimo)+","+str(k))
    datosn = Operaciones.contraccion(datos, k, minimo, cminimo )
    imgg  = Image.new( 'L',img.size )
    imgg.putdata(datosn)
    imgg.save("hist-escala-desplazamiento.jpg")
    histogramaG(imgg)


image = Image.open("snakes.jpg")

#histogramaRGB("snakes.jpg")
histogramaG(image)
#desplazamiento(image,-30)
contraccion(image,150, 160)
contraccion(image,0, 255)

