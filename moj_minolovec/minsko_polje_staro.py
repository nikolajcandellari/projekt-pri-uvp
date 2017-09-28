import tkinter as tk
import logika_minskega_polja as logika

class Minolovec:


    def __init__(self, zaslon):


        #stevec_min

        self.stevec_min = tk.Label(zaslon, text = '10')
        self.stevec_min.grid(row = 0, column = 0)


        #polja kliknjena in niso enaka 0
            
        self.oznacbe = []


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
            
    def primerjaj(self, i, j, k=[0]):
        
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

            if a != 0:
                
                k[0]+=1
                vrednost_matrike = tk.Label(self.polja[i][j], width=5,
                                            height=3, text= a)
                vrednost_matrike.pack()
                
                oznacbe = self.oznacbe
                oznacbe.append([i, j])
                
            else:
                
                okolica_nicle = logika.okolica(i, j)
                for e in okolica_nicle:
                    if e not in self.oznacbe:

                        k[0]+=1
                    
                        x = e[0]
                        y = e[1]
                        b = matrika[x][y]
                        vrednost_matrike = tk.Label(self.polja[x][y], width=5,
                                                height=3, text=b)
                        vrednost_matrike.pack()

                        if b == 0 and (x != i or y != j ):   #v primeru da je
                            self.primerjaj(i=x, j=y, k=[0])  #soseda enaka 0


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
        
        
    def zmagovalni_pogoji(self):
        print(self.polja.count('None'))
        
        

zaslon = tk.Tk()
Minolovec(zaslon)
zaslon.mainloop()
