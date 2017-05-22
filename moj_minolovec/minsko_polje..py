import tkinter as tk

#ob začetnem kliku se nam pokaže začetni ekran

zaslon = tk.Tk()

naslov = tk.Label(zaslon, text = 'MINOLOVEC')
naslov.pack()

gumb_za_izhod = tk.Button(zaslon, text = 'Izhod', command = ZAPRI IGRO)
gumb_za_izhod.pack()

# ko začnemo igro, se samodejno generira minsko polje...

gumb_za_zacetek_igre = tk.Button(zaslon, text = 'Nova igra', command = GENERIRAJ MINSKO POLJE)
gumb_za_zacetek_igre.pack()

        
