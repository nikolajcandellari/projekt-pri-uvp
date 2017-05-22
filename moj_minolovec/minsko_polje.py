import tkinter as tk

#ob začetnem kliku se nam pokaže začetni ekran

zaslon = tk.Tk()
naslov = tk.Label(zaslon, text ='MINOLOVEC')
naslov.pack()

def zapri():
    zaslon.quit()
    
gumb_za_izhod = tk.Button(zaslon, text = 'Izhod' , command = zapri)
gumb_za_izhod.pack()

with open('logika_minskega_polja.py') as logika:
    def ustvari_minsko_polje():
        class Minsko_polje
gumb_za_zacetek_igre = tk.Button(zaslon, text = 'Nova igra'
                                 , command = ustvari_minsko_polje)
gumb_za_zacetek_igre.pack()



   

zaslon.mainloop()

