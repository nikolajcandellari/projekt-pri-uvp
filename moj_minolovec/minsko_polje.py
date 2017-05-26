import tkinter as tk
import logika_minskega_polja

class Minolovec:

    def __init__(self, zaslon):
        self.polje = tk.Toplevel()
        self.polje.pack()
        
        vrstica = []
        for _ in range(9):
            vrstica.append(0)
        stolpec = []
        for_ in range(9):
            stolpec.append(0)
        self.gumbi = tk.Button(row = , column = x)
        self.gumbi.pack()
        








   
zaslon = tk.Tk()
self.gumbi.pack()
zaslon.mainloop()







'''naslov = tk.Label(zaslon, text ='MINOLOVEC')
naslov.pack()

def zapri():
    zaslon.quit()
    
gumb_za_izhod = tk.Button(zaslon, text = 'Izhod' , command = zapri)
gumb_za_izhod.pack()

gumb_za_zacetek_igre = tk.Button(zaslon, text = 'Nova igra'
                                 , command = self.matrika)
gumb_za_zacetek_igre.pack()'''
