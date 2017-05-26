import tkinter as tk
import logika_minskega_polja

class Minolovec:


    def __init__(self, zaslon):

        self.stevec_min = tk.Label(zaslon, text = '10')
        
        self.gumbi = range(81)
        vrstice = []
        for vrstice in range(9):
            stolpci = []
            for stolpci in range(9):
                def klik_z_misko():
                    if 'Button-1' == True: #ne najdem primerne funkcije, ki bi
                                           # zaznala ko bi bil gumb kliknjen 
                                           # z levo tipko na miski

                        
                        
                    elif 'Button-2' == True: # isto za desno tipko
                        self.stevec_min.config(text= str( int()))
                self.gumbi = tk.Button(zaslon, height = 1, width = 1,
                                       text = '', command = klik_z_misko )
                self.gumbi.grid(row = vrstice, column = stolpci)
                        
       




        
    def primerjaj_pritisnjen_gumb_s_tem_kar_je_v_matriki(self):
        pass

    def posodobi_stevec(self):
        pass

    

zaslon = tk.Tk()
Minolovec(zaslon)
zaslon.mainloop()
