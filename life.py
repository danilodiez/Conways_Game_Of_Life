import os
import tkinter as tk



root = tk.Tk()

matrizTablero = [[0 for i in range(20)] for j in range(20)]
print(matrizTablero)

print(matrizTablero[0][0])
def pintarNegro(i,j):
    print('casilla',i,j)
    cuadro = tk.Button(root,bg="black", width=1,height=1,command=lambda: pintarBlanco(i,j)).grid(row=i, column = j)
    matrizTablero[i][j]=1
    print(matrizTablero)

def pintarBlanco(i,j):
    print('casilla',i,j)
    cuadro = tk.Button(root,bg="white", width=1,height=1,command=lambda: pintarNegro(i,j)).grid(row=i, column = j)
    matrizTablero[i][j]=0
    print(matrizTablero)

def pantallaInicial():
    for i in range(20):
        for j in range(20):
            cuadro = tk.Button(root,bg="white", width=1,height=1, command=lambda fila=i, col =j: pintarNegro(fila,col)).grid(row=i, column = j)
            

pantallaInicial()
root.mainloop()