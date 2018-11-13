from PIL import Image
import copy
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
        newdata = copy.deepcopy(self.matriz)
        for i in range ( self.dataxy[1]  ):
            for j in range (self.dataxy[0] ):
                #s = self.word(j,i)
                self.andOp(j,i,newdata,self.tiles[0])
                #print (s)        
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
        #print ("range "+str(x)+" "+str(range(y-self.n, y + self.s +1) ))
        for i in range(y-self.n, y + self.s +1 ):
            if (i < 0 or i > tiley ) :
                waux = [-1]*tilex 
                word.append(waux)
            else :
                if (x < self.w ):
                    waux = [-1]*(self.w-x) 
                    waux = waux+self.matriz[i][x : x+self.e+1]
                    word.append(waux)
                #elif (self.tilex - x <self.e) :
                 #   waux = waux+[-1]*(self.e-(self.tilex - x))
                #  word.append(waux)
                else :
                    waux= self.matriz[i][x-self.w : x+self.e+1]+[-1]*(self.e-self.tilex +x + 1)
                    word.append(waux) 
        return word
    def ranX (self, i):
        return (i>=0 & i<self.dataxy[0] )
    def ranY (self, j) :
        return (j>=0 & j<self.dataxy[1])

    def andOp (self, x, y, newdata, tile):
        rx = range(x-self.w , x+self.e+1)
        ry = range(y-self.n, y + self.s +1 )
        for i in ry :
            for j in rx:
                if ( self.ranX(i) & self.ranY(j) ) :
                    print (str(j-rx[0])+" ,  "+str(j))
                    if ( self.matriz[j][i] & tile[i-ry[0]][j-rx[0]]) :
                        newdata[j][i] = 1;

        print (str(x)+" "+str(rx)+"  : "+str(ry))
        print (" ****** ")
        '''
        for i in range(y-self.n, y + self.s +1 ):
            for j in range (self.tilex) :
                if ()
                if (word[i][j] != -1 and tile[i][j] != -1 ):
                    a = ord[i][j] and tile[i][j]

        '''
data = [0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0]
data = [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0]
data = [0,0,0,0,0,1,0,1,0,1,0,0]
dataxy = [12,9]
dataxy = [3,4]
i = Image.new('1', dataxy)
i.putdata(data)
i.save("tile.png")


tiles = [ [[0, 0, 0], [0, 0, 1], [0, 1, 0]] ]
tilex = 3
tiley = 3
tilecx = 1
tilecy = 1
print(data)
m = Morfologia(tilex, tiley, tilecx, tilecy, tiles, data, dataxy)
m.dilatar()
