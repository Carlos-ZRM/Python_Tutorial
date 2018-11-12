from PIL import Image
from CA import *
from os import listdir
from os.path import isfile, join


def openDirectory (directory) :
    list = [f for f in listdir(directory) if isfile(join(directory, f))]
    return list

def openFile( file ):
    with open( file , "r") as f:
        list_lines = f.readlines() 
    return list_lines

def makeImage( file, image ) :
    data = openFile (file)
    ca_obj = buildCA(data)
    dataxy = [ ca_obj.getRing(), ca_obj.getTimes() ]
    i = Image.new('1', dataxy)
    i.putdata( ca_obj.getData() )
    i.save(image)
    i.show()
    return 

def buildCA( line):
    data = []
    str = ""
    list = line[0].split(' ')
    object = CA( int(list[0]) , int(list[1]) , int(list[2]) )
    
    for i in range ( 1, object.getTimes() ):
        for j in range ( len (line[i]) -1) :
            data.append( not int(line[i][j]) )
    object.setData( data )        
    return object

def buildCADirectory(path, path2) :
    archivos = openDirectory(path)
    for i in range ( len(archivos) ) :
        if "Data" in archivos[i]  and  ".txt" in archivos[i] :
           makeImage(path+archivos[i], path2+archivos[i][0:-4]+".png")  
    return 
    
#makeImage( "test.txt" , "testca.png" )
openDirectory("64/")
buildCADirectory("64/data", "64/espacio")