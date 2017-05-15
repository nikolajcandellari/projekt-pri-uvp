import tkinter as tk

#ob začetnem kliku se nam pokaže začetni ekran

zaslon = tk.Tk()

naslov = tk.Label(zaslon, text = 'MINOLOVEC')
naslov.pack()

gumb_za_izhod = tk.Button(zaslon, text = 'Izhod', command = ZAPRI IGRO)
gumb_za_izhod.pack()

gumb_za_zacetek_igre = tk.Button(zaslon, text = 'Nova igra', command = GENERIRAJ MINSKO POLJE)
gumb_za_zacetek_igre.pack()




# ko začnemo igro, se samodejno generira minsko polje...
        
matrika = []
for _ in range(9):
    vrstica = []
    for _ in range(9):
        vrstica.append(0)
    matrika.append(vrstica)

koordinate_min = []
for _ in range(9):
    x = (random.randint(1, 9), random.randint(1, 9))
    

            
class minsko_polje:

    def __init__(self):
        self.polje = matrika
        self.polozaj_min =  
