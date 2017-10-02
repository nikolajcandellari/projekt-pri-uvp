import tkinter as tk
import logika

class Minolovec:

    def __init__(self, zaslon):


        #stevec min

        self.stevec_min = tk.Label(zaslon, text = '10')
        self.stevec_min.grid(row = 0, column = 0)


        #matrika kliknjenih polj
        
        self.enojno_kliknjena = []
        self.kliknjena = logika.matrika_okolic


        #minsko polje
        
        self.polja = []
        for _ in range(9):
            vrstica = []
            for _ in range(9):
                vrstica.append(None)
            self.polja.append(vrstica)

        #ustvarjanje prikaza polj
  
        for i in range(9):
            for j in range(9):
                p = tk.Frame( highlightbackground="green", 
                              highlightcolor="green",
                              highlightthickness=1, width=50, height=50)             
                p.grid(row=i + 1, column=j)
                
                def levi_klik(event, v=i, s=j):
                    self.primerjaj(v, s)
                    
                def desni_klik(event, v=i, s=j):
                    self.oznaci(v, s)
                    self.posodobi_stevec1()
                    
                p.bind("<Button-1>", levi_klik)
                p.bind("<Button-3>", desni_klik)
                self.polja[i][j] = p


    def oznaci(self, i, j):       
        l = tk.Button(self.polja[i][j], width=5, height=3, text='X')
        
        def oznaci_in_unici():
            self.posodobi_stevec2()
            l.destroy()
            
        l['command'] = oznaci_in_unici
        l.pack()

            
    def primerjaj(self, i, j):
        from logika import matrika


        #uničiš prvotni zaslon in ustavariš končnega
        
        if matrika[i][j] == 10:
            
             zaslon.destroy()
             
             zaslon2 = tk.Tk()
             koncno_okno = tk.Frame(zaslon2, width=10, height=10)
             koncni_napis = tk.Label(koncno_okno, width=10, height=10,
                                     text='IZGUBIL SI')
             
             koncno_okno.pack()
             koncni_napis.pack()
             zaslon2.mainloop()
    

        else:
            
            a = matrika[i][j]

            if a != 0:
                
                vrednost_matrike = tk.Label(self.polja[i][j], width=5,
                                            height=3, text= a)
                vrednost_matrike.pack()
                
                self.enojno_kliknjena.append([i, j])
                self.kliknjena[i][j] = 'odkrita'
                self.zmaga()
                
                
            else:
                
                okolica_nicle = logika.okolica(i, j)
                for e in okolica_nicle:
                    if e not in self.enojno_kliknjena:
                        x = e[0]
                        y = e[1]
                        b = matrika[x][y]
                        
                        vrednost_matrike = tk.Label(self.polja[x][y], width=5,
                                                height=3, text=b)
                        vrednost_matrike.pack()
                        self.zmaga()

                        #v primeru da je sosednje polje enako 0
                        if b == 0 and (x != i or y != j ):   
                            self.primerjaj(i=x, j=y)         


    def zmaga(self):
        if logika.prestej_polja_matrike(self.kliknjena) == 71:
            zaslon.destroy()
            
            zaslon3 = tk.Tk()
            zmagovalno_okno = tk.Frame(zaslon3, width=10, height=10)
            zmagovalni_napis = tk.Button(zmagovalno_okno, width=10, height=10,
                                         text='ZMAGAL SI')    
            zmagovalno_okno.pack()
            zmagovalni_napis.pack()
            zaslon3.mainloop()

    #funkciji za posodabljanje stevca

    def posodobi_stevec1(self):
        sm = self.stevec_min
        smt = int(sm['text'])
        smt1 = smt - 1 
        sm.config(text = str(smt1))


    def posodobi_stevec2(self):
        sm = self.stevec_min
        smt = int(sm['text'])
        smt2 = smt + 1  
        sm.config(text = str(smt2))

        
zaslon = tk.Tk()
m = Minolovec(zaslon)
zaslon.mainloop()
