from PIL import Image

class Morfologia :
    def __init__(self, tilex, tiley, tilecx, tilecy, tiles, data, dataxy) :
        self.tilex = tilex
        self.tiley = tiley
        self.tilecx = tilecx
        self.tilecy = tilecy
        self.tiles = tiles
        self.dataxy = dataxy
        self.matriz = self.crearMat(data)
        print (self.matriz)
        self.data = data
  
    def crearMat(self,data):
        matriz = []
        c = 0
        for i in range (self.dataxy[1]) :
            aux = []
            for j in range ( self.dataxy[0] ) :
                aux.append(data[c])
                c+=1
            matriz.append(aux)
           
        return matriz
    def dilatar (self) :
        x = 0
        y = 0
        s = ""
        for i in range ( self.dataxy[1]  ):
            for j in range (self.dataxy[0] ):
                s = self.word(j,i)
                print (s)
        pass
        
        return
    def erosion (self) :
        pass
    def union (self ):
        pass
    def word (self,x,y):
        s = []
        limi = 0
        limf = 0
        for i in range (y, y+self.tiley) :
            if (i < dataxy[1]):
                saux=[-1]*1
                saux= []
                if (x-1<0) :
                    saux=[-1]*1
                    saux = saux+self.matriz[i][x : self.tilecx-x+1]
                elif x+2>self.tilex :
                    saux = self.matriz[i][x-1 : x]
                    saux = saux +[-1]*1
                else :
                    saux = saux+self.matriz[i][x-1 : x+2]
                #saux.insert(self.matriz[i][x : self.tilex])
                s.append(saux)
            else :
                s.append( [-1]*tilex)
        #for i in range (self.tilex*self.tiley):
        #    s+="*"
        '''
        for i in range (y, y+self.tiley):
            limi = i*self.tiley + x
            limf = i*self.tiley + x +self.tilex

            print(str(limi)+","+str(limf))
            s.append(self.data[limi:limf]  )
        '''
        return s

data = [0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0]
data = [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0]
data = [0,0,0,0,0,1,0,1,0,1,0,0]
dataxy = [12,9]
dataxy = [3,4]
i = Image.new('1', dataxy)
i.putdata(data)

i.show()

tiles = [0,0,0,0,1,0,1,1,1]
tilex = 4
tiley = 5
tilecx = 1
tilecy = 1
print(data)
m = Morfologia(tilex, tiley, tilecx, tilecy, tiles, data, dataxy)
m.dilatar()
