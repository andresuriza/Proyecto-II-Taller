from tkinter import * 

"""
# Tarea programada 2: Operation Moonlight
# Curso: Taller de programacion
# Programadores: Andrés Uriza Lazo y Jose Pablo Esquetini Fallas
"""
#----------------------------------------------------------------------Nivel 1-------------------------------------------------------------------------------------------
def level_1():  # Inicia el nivel 1, con dificultad facil
    global avatar
    
    level1_window = Toplevel()
    level1_window.title("Nivel 1")
    level1_window.geometry("1200x600")
    level1_window.resizable(False, False)

    background = Canvas(level1_window, width=1210, height=610, borderwidth= -5, bg="black")
    background.grid()

    avatar_pic = background.create_image(600, 300, image=avatar)

    wip = Label(background, text="WORK IN PROGRESS", font="Arial 20", fg="white", bg="black")
    wip.place(x= 450, y=100)

    #class Avatar():
    #    def __init__(self):


    #class Missile():
    #    def __init__(self):   
#-------------------------------------------------------------------Menu principal---------------------------------------------------------------------------------------
menu_window = Tk()
menu_window.title("Juego") # Pendiente definir nombre
menu_window.geometry("1200x600")
menu_window.resizable(False, False)

avatar = PhotoImage(file="imagenes/soldado.png")

nombre_label = Label(menu_window, text="Nombre:", font="Arial")
nombre_label.place(x=400, y=400)

nombre_entry = Entry(menu_window, width=50)
nombre_entry.place(x=480, y=403)

play_button = Button(menu_window, font="Arial", text="Jugar", command=level_1)
play_button.place(x=590, y=440)

level_select__label = Label(menu_window, text="o bien, seleccione el nivel:", font="Arial")
level_select__label.place(x=520, y=480)

level1_select = Button(menu_window, text="Nivel 1", font="Arial", command=level_1)
level1_select.place(x=460, y=520)

level2_select = Button(menu_window, text="Nivel 2", font="Arial")
level2_select.place(x=580, y=520)

level3_select = Button(menu_window, text="Nivel 3", font="Arial")
level3_select.place(x=700, y=520)

about = Button(menu_window, font="Arial", text="About")
about.place(x=150, y=440)

puntajes = Button(menu_window, font="Arial", text="Puntajes")
puntajes.place(x=1000, y=440)

aviso_label = Label(menu_window, text="Por favor, recuerde ingresar un nombre antes de comenzar", font="Arial")
aviso_label.place(x=420, y=570)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
menu_window.mainloop()
