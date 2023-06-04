from tkinter import *
from tkinter import ttk

class Calculadora():
    
    def __init__(self, master = None):
        
        
        self.font = ("Verdana", "12")
        self.font_tela = ("Verdana", "15", "bold")
        #espaço inicial
        self.espaco = Frame(master, height=10)
        self.espaco.place(y=300)
        self.espaco.pack()
        
        #tela das contas
        
         
        self.valor_resultado = StringVar()
        self.resultado_variable = StringVar()
        self.valores = ' '
        self.resultado = ' '
        
        def display_valores(event):
            
            
            last_digit = self.valores[-1]
            
            # if event in ["÷", "+", "-", "*", "√"] and last_digit in ["÷", "+", "-", "*", "√"] and event != last_digit:
            if self.valores == ' ' or self.valores == "error":
                
                self.valores = event 
                self.valor_resultado.set(self.valores)
                
            elif event in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "π"]:
            
            
                self.valores = self.valores + str(event)
                
                self.valor_resultado.set(self.valores)
                
            elif last_digit not in ["+", "-", "*", "÷"] and (event != "="):
                
                self.valores = self.valores + str(event)
                
                self.valor_resultado.set(self.valores)
                
            elif last_digit in ["+", "-", "*", "÷", "^", "√"]:
                
                index_last_digit = self.valores.rfind(last_digit)
                self.valores = f"{self.valores[:index_last_digit]}{event}"
                
                self.valor_resultado.set(self.valores)
                
        def event_igual(event):
            
            last_digit = self.valores[-1]
            
            while "√" in self.valores and "+" not in self.valores and "-" not in self.valores and "*" not in self.valores and "/" not in self.valores:
                 #Quando o usuario quer somente fazer a raiz basica de alguma coisa

                new_raiz = "**(1/2)"

                new_string = f"{self.valores[1:]}{new_raiz}"
                
                self.valores = f"{self.valores[1:]}{new_raiz}"
                
            
            if last_digit not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "π"]:
                
                self.valores = "error"
                self.valor_resultado.set(self.valores)   
                
            elif "√" not in self.valores:        
            
                self.valores = self.valores.replace("π", "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912")
                self.valores = self.valores.replace("÷", "/")
                self.valores = self.valores.replace("^", "**")
                self.valores = str(round(eval(self.valores), 9))
                self.valor_resultado.set(self.valores)
                
                    
                
                self.valores = str(round(eval(self.valores), 9))
                self.valor_resultado.set(self.valores)
                    
                    
                    
        
        def evento_ac(event):
            
            
            self.valores = ' '
            
            self.valor_resultado.set(self.valores)
            


            
        
            
        
         
        self.tela_conta = Label(master,textvariable = self.valor_resultado, width=15, height=2,relief=FLAT, anchor = "e",
                                font = self.font_tela,bg = "#1B5F6B", justify=RIGHT, padx = 6)
        
        # self.tela_conta.place(bordermode=OUTSIDE, height=100, width=100)
        self.tela_conta.place(x = 15  ,y =5 )
    
         #espaço entre teclado e
        self.espaco = Frame(master, height=10)
        self.espaco.place(y=300)
        self.espaco.pack()


        #Frame Teclado - 1
        

        self.botao_raiz = Button(master, font = self.font,command = lambda: display_valores("√"), text = "√", borderwidth= 5, relief=RAISED, overrelief=RIDGE )
        self.botao_raiz["padx"] = 4
        self.botao_raiz["pady"] = 4
        self.botao_raiz.place(x = 15, y = 70)
        
        self.botao_pi = Button(master, font= self.font,command = lambda: display_valores("π"), text = "π", borderwidth= 5, relief=RAISED, overrelief=RIDGE )
        self.botao_pi["padx"] = 4
        self.botao_pi["pady"] = 4
        self.botao_pi.place(x = 58, y = 70)
        
        self.botao_eleva = Button(master,command= lambda: display_valores("^"),  font= self.font, text = "^", borderwidth= 5 , relief=RAISED, overrelief=RIDGE)
        self.botao_eleva["padx"] = 4
        self.botao_eleva["pady"] = 4
        self.botao_eleva.place(x = 98, y = 70)
        
        self.botao_igual = Button(master, font = self.font, text = "=",command = lambda: event_igual("="), borderwidth= 5 , relief=RAISED, overrelief=RIDGE)
        self.botao_igual["padx"] = 5
        self.botao_igual["pady"] = 4
        self.botao_igual.place(x = 142, y = 70)
        
        self.botao_ac = Button(master, font = self.font, text = "AC",command=lambda: evento_ac("AC"), borderwidth= 5, relief=RAISED, overrelief=RIDGE, bg ="#A83027")
        self.botao_ac["padx"] = 3
        self.botao_ac["pady"] = 4
        self.botao_ac.place(x = 190, y = 70)
        
        self.botao_div = Button(master, font = self.font, text = "÷",command = lambda: display_valores("÷"), borderwidth= 5 , relief=RAISED, overrelief=RIDGE)
        self.botao_div["padx"] = 31
        self.botao_div["pady"] = 8
        self.botao_div.place(x = 142, y = 120)
        
        self.botao_multi = Button(master, font = self.font, text = "*",command = lambda: display_valores("*"), borderwidth= 5 , relief=RAISED, overrelief=RIDGE)
        self.botao_multi["padx"] = 33
        self.botao_multi["pady"] = 8
        self.botao_multi.place(x = 142, y = 175)
        
        self.botao_soma = Button(master, font = self.font, text = "+",command = lambda: display_valores("+"), borderwidth= 5 , relief=RAISED, overrelief=RIDGE)
        self.botao_soma["padx"] = 31
        self.botao_soma["pady"] = 8
        self.botao_soma.place(x = 142, y = 230)
        
        self.botao_sub = Button(master, font = self.font, text = "-",command = lambda: display_valores("-"), borderwidth= 5 , relief=RAISED, overrelief=RIDGE)
        self.botao_sub["padx"] = 33.5
        self.botao_sub["pady"] = 8
        self.botao_sub.place(x = 142, y = 285)
        
        
        #numerais - 1
        
        self.numero_sete = Button(master, font= self.font, text= "7",command = lambda: display_valores("7"), borderwidth= 5  , relief=RAISED, overrelief=RIDGE)
        self.numero_sete["padx"] = 5
        self.numero_sete["pady"] = 8
        self.numero_sete.place(x = 15, y = 120)
        
        self.numero_oito = Button(master, font= self.font, text= "8",command = lambda: display_valores("8"), borderwidth= 5  , relief=RAISED, overrelief=RIDGE)
        self.numero_oito["padx"] = 5
        self.numero_oito["pady"] = 8
        self.numero_oito.place(x = 58, y = 120)
        
        self.numero_nove = Button(master, font= self.font, text= "9",command = lambda: display_valores("9"), borderwidth= 5  , relief=RAISED, overrelief=RIDGE)
        self.numero_nove["padx"] = 5
        self.numero_nove["pady"] = 8
        self.numero_nove.place(x = 98, y = 120)
        
        #numerais - 2
        
        self.numero_quatro = Button(master, font= self.font, text= "4",command = lambda: display_valores("4"), borderwidth= 5  , relief=RAISED, overrelief=RIDGE)
        self.numero_quatro["padx"] = 5
        self.numero_quatro["pady"] = 8
        self.numero_quatro.place(x = 15, y = 175)
        
        self.numero_cinco = Button(master, font= self.font, text= "5",command = lambda: display_valores("5"), borderwidth= 5  , relief=RAISED, overrelief=RIDGE)
        self.numero_cinco["padx"] = 5
        self.numero_cinco["pady"] = 8
        self.numero_cinco.place(x = 58, y = 175)
        
        self.numero_cinco = Button(master, font= self.font, text= "6",command = lambda: display_valores("6"), borderwidth= 5  , relief=RAISED, overrelief=RIDGE)
        self.numero_cinco["padx"] = 5
        self.numero_cinco["pady"] = 8
        self.numero_cinco.place(x = 98, y = 175)
        
        #numerais - 3
        
        self.numero_um = Button(master, font= self.font, text= "1",command = lambda: display_valores("1"), borderwidth= 5  , relief=RAISED, overrelief=RIDGE)
        self.numero_um["padx"] = 5
        self.numero_um["pady"] = 8
        self.numero_um.place(x = 15, y = 230)
        
        self.numero_dois = Button(master, font= self.font, text= "2",command = lambda: display_valores("2"), borderwidth= 5  , relief=RAISED, overrelief=RIDGE)
        self.numero_dois["padx"] = 5
        self.numero_dois["pady"] = 8
        self.numero_dois.place(x = 58, y = 230)
        
        self.numero_tres = Button(master, font= self.font, text= "3",command = lambda: display_valores("3"), borderwidth= 5  , relief=RAISED, overrelief=RIDGE)
        self.numero_tres["padx"] = 5
        self.numero_tres["pady"] = 8
        self.numero_tres.place(x = 98, y = 230)
        
        #numerais - 4
        
        self.numero_zero = Button(master, font = self.font, text = "0",command = lambda: display_valores("0"), borderwidth = 5, relief=RAISED, overrelief=RIDGE)
        self.numero_zero["padx"] = 26
        self.numero_zero["pady"] = 8
        self.numero_zero.place(x = 15, y = 285)
        
        
        
        self.virgula = Button(master, font = self.font, text = ",",command = lambda: display_valores(","), borderwidth = 5, relief=RAISED, overrelief=RIDGE)
        
        self.virgula["padx"] = 7
        self.virgula["pady"] = 8
        self.virgula.place(x = 98, y = 285)
        

        
        
        
        
        
        
        
        
        
        
        
        
        # self.botao_apaga = Button(master, font= self.font, text = "⌫", borderwidth= 5 )
        # self.botao_apaga["padx"] = 2
        # self.botao_apaga["pady"] = 2
        # self.botao_apaga.place(x = 87, y = 65)
        
    
        
if __name__ == "__main__":
    
    janela = Tk()
    janela.title("Calculadora")
    janela.geometry(newGeometry="250x350+750+250")
    janela.configure(background="#5799AD")
    janela.resizable(0, 0)
    Calculadora(janela)
    janela.mainloop()