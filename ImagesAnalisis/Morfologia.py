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
        '''
            N
        W -----E
            S
        '''
        self.w = tilecx
        self.e = tilex-tilecx-1
        self.s = tiley-tilecy-1
        self.n = tilecy
        print (str(self.n)+" "+str(self.w)+" "+str(self.e)+" "+str(self.s)  )
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
        return
    def erosion (self) :
        pass
    def union (self ):
        pass
    def word (self,x,y):
        word = []
        waux = []
        limi = 0
        limf = 0
        print ("range "+str(x)+" "+str(range(y-self.n, y + self.s +1) ))
        for i in range(y-self.n, y + self.s +1 ):
            if (i < 0 or i > tiley ) :
                waux = [-1]*tilex 
                word.append(waux)
            else :
                if (x < self.w ):
                    waux = [-1]*(self.w-x) 
                    waux = waux+self.matriz[i][x : x+self.e+1]
                    word.append(waux)
                elif (self.tilex - x <=self.e) :
                    waux = waux+[-1]*(self.e-(self.tilex - x))
                    word.append(waux)
                else :
                    waux= self.matriz[i][x-self.w : x+self.e+1]
                    word.append(waux)

        '''
        for i in range (y, y+self.tiley) : 
            if (i < dataxy[1]) :
                saux= [-1]*1
                saux= []
                if (x-1<0) :
                    saux=[-1]*1
                    saux = saux+self.matriz[i][x : self.tilecx-x+1]
                elif x+2 > self.tilex :
                    saux = self.matriz[i][x-1 : x]
                    saux = saux +[-1]*1
                else :
                    saux = saux+self.matriz[i][x-1 : x+2]
                #saux.insert(self.matriz[i][x : self.tilex])
                s.append(saux)
            else :
                s.append( [-1]*tilex )
        
            '''
        #for i in range (self.tilex*self.tiley):
        #    s+="*"
        '''
        for i in range (y, y+self.tiley):
            limi = i*self.tiley + x
            limf = i*self.tiley + x +self.tilex

            print(str(limi)+","+str(limf))
            s.append(self.data[limi:limf]  )
        '''
        return word


data = [0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0]
data = [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0]
data = [0,0,0,0,0,1,0,1,0,1,0,0]
dataxy = [12,9]
dataxy = [3,4]
i = Image.new('1', dataxy)
i.putdata(data)


tiles = [0,0,0,0,1,0,1,1,1]
tilex = 3
tiley = 3
tilecx = 1
tilecy = 1
print(data)
m = Morfologia(tilex, tiley, tilecx, tilecy, tiles, data, dataxy)
m.dilatar()
