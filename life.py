import os
import tkinter as tk



root = tk.Tk()



def pintarGrilla(i,j, color):
    print('hola',i,j)
    cuadro = tk.Button(root,bg=color, width=1,height=1,command=lambda: pintarGrilla(i,j,"white")).grid(row=i, column = j)

def crearBoton():
    for i in range(20):
        for j in range(20):
            cuadro = tk.Button(root,bg="white", width=1,height=1, command=lambda fila=i, col =j: pintarGrilla(fila,col,"black")).grid(row=i, column = j)
        
        


crearBoton()
root.mainloop()