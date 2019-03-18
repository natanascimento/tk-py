from tkinter import *

class api (object):
    #Padrão para criação de GUI
    def __init__(self,window):
        self.window=window
        self.initGUI()
    #Inicializando a GUI
    def initGUI(self):
        self.window.title("tk-py")
        self.create_area()
        self.create_menu_bar()

    #Inciando o menu superior
    def create_menu_bar(self):
        #Cria a barra de menu superior alocando para que funcione em "window"
        menubar = Menu(self.window)
        
        #Cria a opção File na barra de menu associando ao nome EXIT ao passar em cima
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.finaliza_software)
        
        #Cria o formato cascata ao passar na aba
        menubar.add_cascade(label="File", menu=filemenu)

        #Da o show de todo o menu
        self.window.config(menu=menubar)

    #Inicializador de comandos
    def finaliza_software(self):
        self.window.quit()
    
    #Deixar a GUI com uma área em branco
    def create_area(self):
        pass
    
def main():
    root = Tk()
    root.geometry("500x300+50+50") #LxA+E+T
    api(root)
    root.mainloop()

if __name__ == '__main__':
    main()