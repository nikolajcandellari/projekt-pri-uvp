import random

#za graf. umesnik

def prestej_polja_matrike(matrika):
    stevilo_nepraznih_polj = 0
    for vrstica in matrika:
        for polje in vrstica:
            if polje != None:
                stevilo_nepraznih_polj += 1
    return stevilo_nepraznih_polj

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
            
        self.zacetno_polje = []

    def dodaj_mino(self, x, y):
        self.matrika[x][y] = 10

    def povecaj_polje(self, x, y):
        self.matrika[x][y] += 1

    def inicializiraj_polja(self):

        pra_x = int(input("zacetna vrstica med 0 in 8"))
        self.zacetno_polje.append(pra_x)
        
        pra_y = int(input("zacetni stolpec med 0 in 8"))
        self.zacetno_polje.append(pra_y)

        zacetek = []
        polozaji_min = []
                
        x_okolica = [pra_x - 1, pra_x, pra_x + 1]
        for e in x_okolica:
            if e < 0 or 8 < e:
                x_okolica.remove(e)

        y_okolica = [pra_y - 1, pra_y, pra_y + 1]
        for e in y_okolica:
            if e < 0 or 8 < e:
                y_okolica.remove(e)
                    
        for x in x_okolica:
            for y in y_okolica:
                zacetek.append([x, y])          

        # nakljucno doloceni polozaji 10 min
        
        while len(polozaji_min) < 10:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if (x, y) not in polozaji_min:
                if [x, y] not in zacetek:
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

m = Minsko_polje()
m.inicializiraj_polja()
matrika = m.matrika
print(matrika)
