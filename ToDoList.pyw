import tkinter
from tkinter import *
from tkinter import messagebox
import pickle

wn = Tk()
wn.title("Lista de Tareas")
wn.iconbitmap('./iconoListaTareas.ico')
menu_Bar = Menu(wn)
wn.configure(menu=menu_Bar,bg="white")


#FUNCIONES
def añadirTarea():
	tarea = entrada.get()
	if tarea.strip() != "":
		lista_tareas.insert(END,tarea)
		entrada.delete(0,END)
	else:	
		messagebox.showerror("Error","Inserta la tarea")
def borrarTarea():
	try:
		tarea_index = lista_tareas.curselection()[0]
		lista_tareas.delete(tarea_index)
	except:
		messagebox.showerror("Error","Selecciona una tarea")
def guardarTarea():
	guardarTarea = lista_tareas.get(0, lista_tareas.size())
	pickle.dump(guardarTarea,open("tasks.dat","wb"))
	messagebox.showinfo("Información","Tareas guardadas exitosamente")
def cargarTarea():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        lista_tareas.delete(0, END)
        for task in tasks:
            lista_tareas.insert(END, task)
        messagebox.showinfo("Información","Tareas Cargadas exitosamente")
    except:
        messagebox.showerror(title="Error!", message="No se encuentra el archivo tasks.dat.")
def tareaCompletada():
	pregunta = messagebox.askyesno("Información","Desea Añadir a la lista de Tareas Completas")
	pregunta2 = messagebox.askyesno("Información","Desea ver la lista de tareas Completas")
	if pregunta == True:
		datosCompletos = lista_tareas.curselection()
		datos = lista_tareas.get(datosCompletos)
		lista_TareasCompleta.insert(END,datos)
		if pregunta2 == True:
			messagebox.showinfo("Información","Mira la segunda ventana")
	else:
		messagebox.showerror("Error","Ninguna Opcion seleccionada")
def guardarTareaCompleta():
	guardarTarea = lista_tareas.get(0, lista_TareasCompleta.size())
	pickle.dump(guardarTarea,open("tasksComplete.dat","wb"))
	messagebox.showinfo("Información","Tareas guardadas exitosamente")
def cargarTareaCompletas():
    try:
        tasks = pickle.load(open("tasksComplete.dat", "rb"))
        lista_TareasCompleta.delete(0, END)
        for task in tasks:
            lista_TareasCompleta.insert(END, task)
        messagebox.showinfo("Información","Tareas Cargadas exitosamente")
    except:
        messagebox.showerror(title="Error!", message="No se encuentra el archivo tasksComplete.dat")


#MENU BAR

menuArchivo = Menu(menu_Bar,tearoff=0)
menu_Bar.add_cascade(label="Archivo",menu=menuArchivo)
menuArchivo.add_command(label="Añadir Tarea",command=añadirTarea)
menuArchivo.add_command(label="Borrar Tarea",command=borrarTarea)
menuArchivo.add_command(label="Guardar Tareas",command=guardarTarea)
menuArchivo.add_command(label="Cargar Tareas",command=cargarTarea)
menuArchivo.add_command(label='Tarea Completada',command=tareaCompletada)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir",command=wn.quit)


#GUI

complete = Tk()
complete.title('Lista de Tareas --COMPLETAS')
complete.iconbitmap('./iconoListaTareas.ico')
complete.configure(bg='white')

lista_TareasCompleta = Listbox(complete,height = 10, width= 75,font=("Arial",12))
lista_TareasCompleta.grid(sticky=W+E, row = 1 ,column=0)

scrollbar_list = Scrollbar(complete, orient=VERTICAL, command=lista_TareasCompleta.yview)
scrollbar_list.grid(row=0, column=1, sticky=N+S)	
lista_TareasCompleta.configure(yscrollcommand=scrollbar_list.set)

btnSave = Button(complete, text='Guardar tareas',relief=FLAT,command=guardarTarea,font=("Arial",12))
btnSave.grid(sticky=W+E, row = 2 ,column=0 )

btnLoad = Button(complete, text='Cargar Tareas',relief=FLAT,command=cargarTarea,font=("Arial",12))
btnLoad.grid(sticky=W+E, row = 3 ,column=0 )

complete.mainloop




contenedor = Frame(wn).grid(row=0,column=0)	

lista_tareas = Listbox(contenedor,height = 10, width= 75,font=("Arial",12))
lista_tareas.grid(sticky=W+E, row = 1 ,column=0)

vsbar = Scrollbar(contenedor, orient=VERTICAL, command=lista_tareas.yview)
vsbar.grid(row=0, column=1, sticky=N+S)
lista_tareas.configure(yscrollcommand=vsbar.set)

entrada = Entry(wn,width = 60,font=("Arial",12))
entrada.focus()
entrada.grid(sticky=W+E, row = 3 ,column=0 )

btnAdd = Button(wn, text='Añadir tarea', command=añadirTarea,relief=FLAT,font=("Arial",12))
btnAdd.grid(sticky=W+E, row = 4 ,column=0 )

btnDelete = Button(wn, text='Borrar tarea',relief=FLAT,command=borrarTarea,bg="red",fg="white",font=("Arial",12))
btnDelete.grid(sticky=W+E, row =5 ,column=0 )

btnSave = Button(wn, text='Guardar tareas',relief=FLAT,command=guardarTarea,font=("Arial",12))
btnSave.grid(sticky=W+E, row = 6 ,column=0 )

btnLoad = Button(wn, text='Cargar Tareas',relief=FLAT,command=cargarTarea,font=("Arial",12))
btnLoad.grid(sticky=W+E, row = 7 ,column=0 )

btnComplete = Button(wn, text='Tarea Completada',relief=FLAT,bg="green", command=tareaCompletada,fg="white",font=("Arial",12))
btnComplete.grid(sticky=W+E, row = 8 ,column=0 )

separator = Label(wn,text=" ",bg="white").grid(sticky=W+E,row=9,column=0)

labelAuthor = Label(wn,text='Creado Por Teo mas Información en la Barra de Menu',bg="white")
labelAuthor.grid(sticky=W+E, row=10,column=0)
#POSICIONAR VENTANA
wn.mainloop()