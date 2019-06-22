import tkinter
from tkinter import*
import ast
from ast import*

def primo(numero):
    if numero <= 1:
        return False
    elif numero == 2 or numero == 3:
        return True
    elif numero % 2 == 0:
        return False
    i = 3
    while i * i <= numero:
        if (numero % i == 0):
            return False
        else:
            pass
        i = i + 1
    return True

def validarEntrada():
    try:
        numero = ast.literal_eval(entrada.get())
        tipo = type(numero)
        if tipo != int:
            messagebox.showerror(None,"Debe ingresar numeros enteros")
            entrada.delete(0,END)
            return
        else:
            if primo(numero):
                messagebox.showinfo(None,"El numero si es primo")
                return
            else:
                messagebox.showinfo(None,"El numero no es primo")
                return
    except ValueError:
        messagebox.showerror(None,"Debe ingresar un numero")
        entrada.delete(0,END)
        return

def clear():
    entrada.delete(0,END)
    
        
app = tkinter.Tk()
app.geometry('600x600')

l1 = Label(app,font=("Times New Roman",20),text="Ingrese un numero").grid(row=0,column=1)
entrada = Entry(app)
entrada.grid(row=1,column=1)
btnPrimo = Button(app,command=validarEntrada,font=("Times New Roman",16),text="Determinar si es primo")
btnPrimo.grid(row=2,column=0)

btnReset = Button(app,command=clear,font=("Times New Roman",16),text="Borrar entrada")
btnReset.grid(row=2,column=2)


app.mainloop()
