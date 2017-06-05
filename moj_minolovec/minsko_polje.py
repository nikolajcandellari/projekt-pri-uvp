import tkinter as tk
import logika_minskega_polja

class Minolovec:


    def __init__(self, zaslon):

        self.stevec_min = tk.Label(zaslon, text = '10')
        self.stevec_min.grid(row =0, column = 0)
        
        self.polja = []
        for _ in range(9):
            vrstica = []
            for _ in range(9):
                vrstica.append(None)
            self.polja.append(vrstica)

        self.nalepke = []
        for _ in range(9):
            vrstica = []
            for _ in range(9):
                vrstica.append(None)
            self.nalepke.append(vrstica)
        
        for i in range(9):
            for j in range(9):
                p = tk.Frame( highlightbackground="green", highlightcolor="green",
                              highlightthickness=1, width=50, height=50, bd= 0)
                p.grid(row = i + 1, column = j)
                def levi_klik(event, v=i, s=j):
                    self.primerjaj(v, s)
                def desni_klik(event, v=i,s=j):
                    self.oznaci(v, s)
                p.bind("<Button-1>", levi_klik)
                p.bind("<Button-3>", desni_klik)
                self.polja[i][j] = p


    def oznaci(self, i, j):
        if self.nalepke[i][j] != None:
            l.destroy()
            self.nalepke[i][j] = None
        else:
            l = tk.Label(self.polja[i][j], text='X')
            self.nalepke[i][j] = l
            l.pack()
        # posodobi stevec

        
    def primerjaj(self, x, y):
        pass

    def posodobi_stevec(self):
        pass

    

zaslon = tk.Tk()
Minolovec(zaslon)
zaslon.mainloop()
