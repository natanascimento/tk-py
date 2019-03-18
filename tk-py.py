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

    def create_area(self):
        pass

def main():
    root = Tk()
    root.geometry("500x300+50+50") #LxA+E+T
    api(root)
    root.mainloop()

if __name__ == '__main__':
    main()