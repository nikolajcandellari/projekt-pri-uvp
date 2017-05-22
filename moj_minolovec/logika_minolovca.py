import random 

class Minsko_polje:

    def __init__(self):
        self.matrika = []
        for _ in range(9):
            vrstica = []
            for _ in range(9):
                vrstica.append(0)
            self.matrika.append(vrstica)

    def dodaj_mino(self, x, y):
        self.matrika[x][y] = 10

    def povecaj_polje(self, x, y):
        self.matrika[x][y] += 1

    def inicializiraj_polja(self):
        polozaji_min = []
        
        while len(polozaji_min) < 10:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if (x, y) not in polozaji_min:
                self.dodaj_mino(x, y)
                polozaji_min.append((x, y))

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
                        if x != a[0] or y != a[1]:
                            self.povecaj_polje(x, y)
                


        
    '''def ostevilci_polja(self):
        polja = []
        for i in range(9):'''
            
            

m = Minsko_polje()
m.inicializiraj_polja()
print(m.matrika)


    

            
'''class minsko_polje:

    def __init__(self):
        self.polje = matrika
        self.polozaj_min =  '''
