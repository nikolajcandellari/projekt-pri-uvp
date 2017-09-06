import tkinter as tk
import logika_minskega_polja as logika

class Minolovec:


    def __init__(self, zaslon):

        #stevec min
        
        self.stevec_min = tk.Label(zaslon, text = '10')
        self.stevec_min.grid(row =0, column = 0)

        #minsko polje
        
        self.polja = []
        for _ in range(9):
            vrstica = []
            for _ in range(9):
                vrstica.append(None)
            self.polja.append(vrstica)

        
        for i in range(9):
            for j in range(9):
                p = tk.Frame( highlightbackground="green", highlightcolor="green",
                              highlightthickness=1, width=50, height=50)
                p.grid(row = i + 1, column = j)
                def levi_klik(event, v=i, s=j):
                    self.primerjaj(v, s)
                def desni_klik(event, v=i, s=j):
                    self.oznaci(v, s)
                p.bind("<Button-1>", levi_klik)
                p.bind("<Button-3>", desni_klik)
                self.polja[i][j] = p


    def oznaci(self, i, j):
            l = tk.Button(self.polja[i][j], width=5, height=3, text='X')
            l['command'] = l.destroy             
            l.pack()
        # posodobi stevec

        
    def primerjaj(self, i, j):
        from logika_minskega_polja import matrika
        if matrika[i][j] == 10:
            #naredi label cez vecino zaslona in nato zakljuci program
             zaslon.destroy()
            
        else:
            a = matrika[i][j] # ohranjaj enako velikost polj
            vrednost_matrike = tk.Label(self.polja[i][j], width=5, height=3, text= a)
            vrednost_matrike.pack()

    def posodobi_stevec(self):
        pass

    

zaslon = tk.Tk()
Minolovec(zaslon)
zaslon.mainloop()
