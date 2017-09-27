import tkinter as tk
import logika_minskega_polja as logika

class Minolovec:


    def __init__(self, zaslon):

        #stevec min
        
        stevec = logika.stevec 
        self.stevec_min = tk.Label(zaslon, text = stevec )
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
                p = tk.Frame( highlightbackground="green", 
                              highlightcolor="green",
                              highlightthickness=1, width=50, height=50)             
                p.grid(row=i + 1, column=j)
                
                def levi_klik(event, v=i, s=j, i=[0]):
                    
                    primerjaj = logika.Minsko_polje.primerjaj
                    if primerjaj(v=i, s=j) == True:
                            
                        zaslon.destroy()
            
                        zaslon3 = tk.Tk()
                        zmagovalno_okno = tk.Frame(zaslon3, width=10, height=10)
                        zmagovalni_napis = tk.Button(zmagovalno_okno, width=10,
                                                     height=10, text='ZMAGAL SI')    
                        zmagovalno_okno.pack()
                        zmagovalni_napis.pack()
                        zaslon3.mainloop()
                        
                    elif primerjaj(v=i, s=j) == False:
                        
                        zaslon.destroy()
             
                        zaslon2 = tk.Tk()
                        koncno_okno = tk.Frame(zaslon2, width=10, height=10)
                        koncni_napis = tk.Label(koncno_okno, width=10,
                                                height=10, text='IZGUBIL SI')
             
                        koncno_okno.pack()
                        koncni_napis.pack()
                        zaslon2.mainloop()
                         
                    else:
                        a = primerjaj(v=i, s=j)
                        vrednost_matrike = tk.Label(self.polja[i][j], width=5,
                                                    height=3, text='a')
                        vrednost_matrike.pack()
                        
                def desni_klik(event, v=i, s=j):
                    self.oznaci(v, s)
                    posodobi_stevec1 = logika.Minsko_polje.posodobi_stevec1
                    posodobi_stevec1()
                    
                p.bind("<Button-1>", levi_klik)
                p.bind("<Button-3>", desni_klik)
                self.polja[i][j] = p

    def oznaci(self, i, j):
        l = tk.Button(self.polja[i][j], width=5, height=3, text='X')
        def oznaci_in_unici():
            posodobi_stevec2 = logika.Minsko_polje.posodobi_stevec2
            posodobi_stevec2()
            l.destroy()
        l['command'] = oznaci_in_unici
        l.pack()

zaslon = tk.Tk()
Minolovec(zaslon)
zaslon.mainloop()
