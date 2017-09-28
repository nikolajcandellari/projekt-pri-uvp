import random

#za graf. umesnik 

matrika_okolic = []
for _ in range(9):
    vrstica = []
    for _ in range(9):
        vrstica.append(None)
    matrika_okolic.append(vrstica)

    
def okolica(i, j):
    i_j_okolica = []
                
    i_okolica = [i - 1, i, i + 1]
    for e in i_okolica:
        if e < 0 or 8 < e:
            i_okolica.remove(e)

    j_okolica = [j - 1, j, j + 1]
    for e in j_okolica:
        if e < 0 or 8 < e:
            j_okolica.remove(e)
                    
    for i in i_okolica:
        for j in j_okolica:
            if matrika_okolic[i][j] == None:
                i_j_okolica.append([i, j])
                matrika_okolic[i][j] = 'odkrita'
            
    return i_j_okolica

#osnovno minsko polje

class Minsko_polje:

    def __init__(self):
        
        self.matrika = []
        for _ in range(9):
            vrstica = []
            for _ in range(9):
                vrstica.append(0)
            self.matrika.append(vrstica)
            
        self.stevec = '10'

    def dodaj_mino(self, x, y):
        self.matrika[x][y] = 10

    def povecaj_polje(self, x, y):
        self.matrika[x][y] += 1

    def inicializiraj_polja(self):
        polozaji_min = []

        # nakljucno doloceni polozaji 10 min
        
        while len(polozaji_min) < 10:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if (x, y) not in polozaji_min:
                self.dodaj_mino(x, y)
                polozaji_min.append((x, y))

        # povecanje stevil v poljih glede na število sosednjih min

        for a in polozaji_min:
            
            x_okolica = [a[0] - 1, a[0], a[0] + 1]
            for e in x_okolica:
                if e < 0 or 8 < e:
                    x_okolica.remove(e)
                    
            y_okolica = [a[1] - 1, a[1], a[1] + 1]
            for e in y_okolica:
                    if e < 0 or 8 < e:
                        y_okolica.remove(e)
            
            for x in x_okolica:
                for y in y_okolica:
                    if (x, y) not in polozaji_min:
                        if x != a[0] or y != a[1] :
                            self.povecaj_polje(x, y)
#
#samo za minsko_polje_popravljeno
#                           
            
    def primerjaj(self, i, j, k=[0]):
        k[0]+=1
        
        if self.matrika[i][j] == 10:   #uničiš prvotni zaslon in ustavariš končnega
            return False
            
        elif k[0] == 71:     # če je stevilo odkrit polj=71 potem si zmagal saj
            return True                 # so neodkrita ostala le polja z bombami  

        else:
            a = self.matrika[i][j]
            return a
        
             
    def posodobi_stevec1(self):
        sm = self.stevec
        smt = int(sm)
        smt1 = smt - 1
        
        sm = str(smt1)


    def posodobi_stevec2(self):
        sm = self.stevec
        smt = int(sm)
        smt2 = smt + 1
        
        sm = str(smt2)

        
m = Minsko_polje()
m.inicializiraj_polja()
matrika = m.matrika
print(matrika)
