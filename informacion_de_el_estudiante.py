#---------------------------------
# Desktop informacion estudiantil
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox
# abrir toplevel centigrados
def abrir_toplevel_infstu():
    global toplevel_infstu
    toplevel_infstu = Toplevel()
    toplevel_infstu.title("infstu")
    toplevel_infstu.resizable(False, False)
    toplevel_infstu.geometry("600x300")
    toplevel_infstu.config(bg="white")
    
    # etiqueta para valor en centigrados
    lb_inf = Label(toplevel_infstu, text = "Nombre = ")
    lb_inf.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_inf.place(x=150, y=60)

    # caja de texto para valor en centigrados
    entry_inf = Entry(toplevel_infstu, textvariable=c)
    entry_inf.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_inf.focus_set()
    entry_inf.place(x=210,y=60)

   # boton para convertir
    bt_aceptar = Button(toplevel_infstu,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=150, width=100, height=30)

# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    toplevel_infstu.destroy()






# abrir toplevel centigrados
def abrir_toplevel_notas():
    global toplevel_notas
    toplevel_notas = Toplevel()
    toplevel_notas.title("notas")
    toplevel_notas.resizable(False, False)
    toplevel_notas.geometry("600x400")
    toplevel_notas.config(bg="white")

        # etiqueta para valor en centigrados
    lb_notas = Label(toplevel_notas, text = "notas =")
    lb_notas.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_notas.place(x=150, y=60)

    # caja de texto para valor en centigrados
    entry_notas = Entry(toplevel_notas, textvariable=c)
    entry_notas.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_notas.focus_set()
    entry_notas.place(x=210,y=60)

   # boton para convertir
    bt_aceptar = Button(toplevel_notas,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=150, width=100, height=30)

# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    toplevel_notas.destroy()









# abrir toplevel centigrados
def abrir_toplevel_imc():
    global toplevel_imc
    toplevel_imc = Toplevel()
    toplevel_imc.title("imc")
    toplevel_imc.resizable(False, False)
    toplevel_imc.geometry("400x300")
    toplevel_imc.config(bg="white")

    # logo de la app
    lb_logo2 = Label(toplevel_infstu, image=logo, bg="white")
    lb_logo2.place(x=10,y=10)

    # logo de la app
    lb_logo2 = Label(toplevel_notas, image=logo, bg="white")
    lb_logo2.place(x=10,y=10)

    # logo de la app
    lb_logo2 = Label(toplevel_imc, image=logo, bg="white")
    lb_logo2.place(x=10,y=10)

    # etiqueta para valor en centigrados
    lb_infstu = Label(toplevel_infstu, text = "nombre= ")
    lb_infstu.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_infstu.place(x=100, y=15)

    # sumar
def convertir():
    messagebox.showinfo("Temperatura 1.0", "Conversión realizada")
    cent = int(c.get())
    if kf.get()=="kelvin":
        k = cent + 273.15
        t_resultados.insert(INSERT, f"\n{int(c.get())} °C equivalen a {k} °K")
    elif kf.get() == "fahrenheit":
        f = cent*9/5 + 32
        t_resultados.insert(INSERT, f"\n{int(c.get())} °C equivalen a {f} °F")
    else:
        t_resultados.insert(INSERT, "Debe seleccionar una opción")
    
# borrar
def borrar():
    messagebox.showinfo("Temperatura 1.0", "Los datos serán borrados")
    c.set("")
    t_resultados.delete("1.0","end")

# salir
def salir():
    messagebox.showinfo("Temperatura 1.0", "La app se va a cerrar")
    ventana_principal.destroy()


# etiqueta para valor en centigrados
    lb_c = Label(toplevel_infstu, text = "nombre(s) = ")
    lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_c.place(x=150, y=60)

    # etiqueta para valor en centigrados
    lb_c = Label(toplevel_imc, text = "°C = ")
    lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_c.place(x=150, y=60)

# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    toplevel_infstu.destroy()
    
# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    toplevel_notas.destroy()

# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    toplevel_imc.destroy()


# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("informacion estudiante")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="blue")



#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=480)
frame_entrada.place(x=10, y=10)
# logo de la app
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=200,y=40)


# titulo de la app
titulo = Label(frame_entrada, text="informacion de estudiante")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=100,y=10)


#--------------------------------
# barra menu
#--------------------------------
barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

menu_convertir = Menu(tearoff=0)
menu_convertir.add_command(label="Convertir", command=convertir)
menu_convertir.add_separator()
menu_convertir.add_command(label="Borrar", command=borrar)

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Convertir", menu=menu_convertir)
barra_menu.add_cascade(label="Salir", menu=menu_salir)



# boton para abrir Toplevel para ingresar inf personal
bt_estudiante = Button(frame_entrada, text="inf personal", command=abrir_toplevel_infstu)
bt_estudiante.config(bg="red", width=10, height=0)
bt_estudiante.place(x=50, y=200)

# boton para abrir Toplevel para ingresar notas
bt_notas = Button(frame_entrada, text="notas", command=abrir_toplevel_notas)
bt_notas.config(bg="red", width=10, height=0)
bt_notas.place(x=200, y=200)

# boton para abrir Toplevel para ingresar indice masa corporal 
bt_imc = Button(frame_entrada, text="imc", command=abrir_toplevel_imc)
bt_imc.config(bg="red", width=10, height=0)
bt_imc.place(x=350, y=200)




ventana_principal.mainloop()