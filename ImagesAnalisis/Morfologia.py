from PIL import Image
import manageFile 
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
    def crearData (self, matriz):
        data = []
        for i in range (dataxy[1]):
            data = data + [ matriz[i][j] for j in range (dataxy[0])]
        return data

    def dilatar (self) :
        x = 0
        y = 0
        s = ""
        newdata = copy.deepcopy(self.matriz)
        for i in range ( self.dataxy[1]  ):
            #s = s + '\n'
            for j in range (self.dataxy[0] ):
            #   s = s+str(self.matriz[i][j])
                s = self.worddos(i,j, newdata, self.tiles[0])
                #self.andOp(i,j,newdata,self.tiles[0])
                print (s)  
                #       
        lista = self.crearData(newdata)
        return lista
    def erosion (self) :
        pass
    def union (self ):
        pass
    def worddos (self,y,x,newdata,tile):
        word = []
        waux = []
        limi = 0
        limf = 0
        auxx = 0 # 
        #print ("range "+str(x)+" "+str(range(y-self.n, y + self.s +1) ))
        ry = range(y-self.n, y + self.s +1 )
        for i in ry:
            waux = []
            # if (i < 0 or i > tiley ) :
            #      waux = [-1]*tilex 
            #    word.append(waux)
            if (not (tile[self.tilecy][self.tilecx] and self.matriz[y][x]) ):
                return 
            if (not (i < 0 or i > tiley )) :
                rx = range(x-self.w , x+self.e+1)
                #print(str(y)+" . "+str(x)+" : "+str(len(range(x-self.w , x+self.e+1))) )
                auxx = 0
                for j in rx :
                    print("     ")
                    print (" y,x "+str(y)+","+str(x))
                    print (" i,j: "+str(i)+","+str(j))
                    print (" ti,tj: "+str(i-ry[0])+","+str(auxx) )
                    if (j>0 and j< 3 ) :
                        print(tile[i-ry[0]][auxx])
                        if tile[i-ry[0]][auxx]==1:
                            newdata[i][j] =  self.matriz[i][j] or tile[i-ry[0]][auxx] 
                            print ("               "+str(i-ry[0])+","+str(j -rx[0]))
                        waux.append(self.matriz[i][j])
                    else:
                        waux.append(-1)
                    auxx = auxx + 1
                word.append(waux)
                '''
                if (x < self.w ):
                    waux = [-1]*(self.w-x) 
                    waux = waux+self.matriz[i][x : x+self.e+1]
                    word.append(waux)
                elif (self.tilex - x <self.e) :
                    waux = waux+[-1]*(self.e-(self.tilex - x))
                    word.append(waux)
                else :
                    waux= self.matriz[i][x-self.w : x+self.e+1]+[-1]*(self.e-self.tilex +x + 1)
                    word.append(waux)
                ''' 
                
        return word
    
    def word (self,y,x):
        word = []
        waux = []
        limi = 0
        limf = 0
        #print ("range "+str(x)+" "+str(range(y-self.n, y + self.s +1) ))
        for i in range(y-self.n, y + self.s +1 ):
            waux = []
            if (i < 0 or i > tiley ) :
                waux = [-1]*tilex 
                word.append(waux)
            else :
                rx = range(x-self.w , x+self.e+1)
                #print(str(y)+" . "+str(x)+" : "+str(len(range(x-self.w , x+self.e+1))) )
                for j in rx :
                    if (j>0 and j< self.dataxy[0]) :
                        waux.append(self.matriz[i][j])
                    else:
                        waux.append(-1)
                word.append(waux)
                '''
                if (x < self.w ):
                    waux = [-1]*(self.w-x) 
                    waux = waux+self.matriz[i][x : x+self.e+1]
                    word.append(waux)
                elif (self.tilex - x <self.e) :
                    waux = waux+[-1]*(self.e-(self.tilex - x))
                    word.append(waux)
                else :
                    waux= self.matriz[i][x-self.w : x+self.e+1]+[-1]*(self.e-self.tilex +x + 1)
                    word.append(waux)
                ''' 
                
        return word
    def ranX (self, i):
        return (i>=0 and i<self.dataxy[0] )
    def ranY (self, j) :
        return (j>=0 and j<self.dataxy[1])
    

    def andOp (self, y, x, newdata, tile):
        if (self.matriz[y][x]!= tile[self.tilecy][self.tilecx]):
            return
        rx = range(x-self.w , x+self.e+1)
        ry = range(y-self.n, y + self.s+1 )
        tt = self.word(x,y)
        print (tt)
        for i in ry :
            for j in rx:
                if ( self.ranX(j) and self.ranY(i) ) :
                    if tile[i-ry[0]][j-rx[0]]!=-1:
                        newdata[i][j] =  self.matriz[i][j] or tt[i-ry[0]][j-rx[0]] 
                #tt = tt+str(self.matriz[i][j])

                #   if (tile[i-ry[0]][j-rx[0]]!=-1):
                #       newdata[j][i] =  self.matriz[i][j] or tile[i-ry[0]][j-rx[0]] 
                    #if ( self.matriz[i][j] &  newdata[j][i] = 1;) :
        
        #print (tt+" "+str(rx)+"  : "+str(ry)) 
        '''
        for i in range(y-self.n, y + self.s +1 ):
            for j in range (self.tilex) :
                if ()
                if (word[i][j] != -1 and tile[i][j] != -1 ):
                    a = ord[i][j] and tile[i][j]

        '''


 hnbv)9o0a = [0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0]
data = [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0]
data = [0,0,0,0,0,1,0,1,0,1,0,0]
'''data = [1,1,1,1,1,1,1,1,
        1,1,0,0,1,1,1,1,
        1,0,0,0,0,1,0,1,
        1,0,0,0,0,0,0,1,
        1,1,0,0,0,0,0,1,
        1,1,0,0,0,0,0,1,
        1,1,1,1,0,1,0,1,
        1,1,1,1,1,1,1,1] 
'''
#data = [not data[i] for i in range (len(data))]
dataxy = [12,9]
dataxy = [3,4]
#dataxy = [8,8]
i = Image.new('1', dataxy)
i.putdata(data)
i.save("tile.png")


tiles = [ [[-1, 1, -1], [1, 1, -1], [-1, -1, -1]] ]

tilex = 3
tiley = 3
tilecx = 1
tilecy = 1
print(data)
m = Morfologia(tilex, tiley, tilecx, tilecy, tiles, data, dataxy)
manageFile.makeImageMorfologia(dataxy, m.dilatar(), "resultM.png")
