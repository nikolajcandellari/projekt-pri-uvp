import tkinter as tk
import logika_minskega_polja as logika

class Minolovec:


    def __init__(self, zaslon):

        #minsko polje
        
        self.polja = []
        for _ in range(9):
            vrstica = []
            for _ in range(9):
                vrstica.append(None)
            self.polja.append(vrstica)
  
        for i in range(9):
            for j in range(9):
                p = tk.Frame( highlightbackground="green", 
                              highlightcolor="green",
                              highlightthickness=1, width=50, height=50)             
                p.grid(row=i + 1, column=j)
                
                def levi_klik(event, v=i, s=j, i=[0]):
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
            
    def primerjaj(self, i, j, k=[0]):
        k[0]+=1
        from logika_minskega_polja import matrika
        
        if matrika[i][j] == 10:   #uničiš prvotni zaslon in ustavariš končnega
            
             zaslon.destroy()
             
             zaslon2 = tk.Tk()
             koncno_okno = tk.Frame(zaslon2, width=10, height=10)
             koncni_napis = tk.Label(koncno_okno, width=10, height=10,
                                     text='IZGUBIL SI')
             
             koncno_okno.pack()
             koncni_napis.pack()
             zaslon2.mainloop()
            
        elif k[0] == 71:     # če je stevilo odkrit polj=71 potem si zmagal saj
                             # so neodkrita ostala le polja z bombami  
            zaslon.destroy()
            
            zaslon3 = tk.Tk()
            zmagovalno_okno = tk.Frame(zaslon3, width=10, height=10)
            zmagovalni_napis = tk.Button(zmagovalno_okno, width=10, height=10,
                                         text='ZMAGAL SI')    
            zmagovalno_okno.pack()
            zmagovalni_napis.pack()
            zaslon3.mainloop()

        else:
            a = matrika[i][j]
            vrednost_matrike = tk.Label(self.polja[i][j], width=5, height=3,
                                        text= a)
            vrednost_matrike.pack()


zaslon = tk.Tk()
Minolovec(zaslon)
zaslon.mainloop()
