from tkinter import * 
import time
import random

"""
# Tarea programada 2: Operation Moonlight
# Curso: Taller de programacion
# Programadores: Andrés Uriza Lazo y Jose Pablo Esquetini Fallas
"""
seconds = 0
#----------------------------------------------------------------------Nivel 1-------------------------------------------------------------------------------------------
def level_1():  # Inicia el nivel 1, con dificultad facil
    global avatar
    
    level1_window = Toplevel()
    level1_window.title("Nivel 1")
    level1_window.geometry("1200x600")
    level1_window.resizable(False, False)

    background = Canvas(level1_window, width=1210, height=610, borderwidth= -5, bg="gray")
    background.grid()

    informacion = Canvas(background, width=350, height=1000, borderwidth= -25, bg="black")
    informacion.place(x=0, y=0)

    def counter():
        global seconds
        seconds += 1
        return seconds

    class Avatar():
        def __init__(self):
            self.avatar_pic = background.create_image(600, 300, image=avatar)

        def left(self, key): # Mueve al avatar a la izquierda
           if background.coords(self.avatar_pic)[0] > 380:
                background.move(self.avatar_pic, -30, 0)

        def right(self, key): # Mueve al avatar a la derecha
           if background.coords(self.avatar_pic)[0] < 1130:
                background.move(self.avatar_pic, 30, 0)

        def up(self, key): # Mueve al avatar hacia arriba
           if background.coords(self.avatar_pic)[1] > 70:
                background.move(self.avatar_pic, 0, -30)

        def down(self, key): # Mueve al avatar hacia abajo
           if background.coords(self.avatar_pic)[1] < 520:
                background.move(self.avatar_pic, 0, 30)

    class Obstacle():
        def __init__(self, x_pos, y_pos, x_speed, y_speed):
            self.counter = 0
            self.obstacle_pic = background.create_image(x_pos, y_pos, image=obstacle)
            self.x_speed = x_speed
            self.y_speed = y_speed

        def animate(self): # Mueve a los proyectiles
            x = background.coords(self.obstacle_pic)[0]
            y = background.coords(self.obstacle_pic)[1]

            if self.counter == 2:
                self.obstacle_pic.destroy()
            else:
                if x >= 1180 or x <= 300:
                    self.counter += 1
                    self.x_speed = -self.x_speed
                if y >= 540 or y <= 50:
                    self.counter += 1
                    self.y_speed = -self.y_speed
            background.move(self.obstacle_pic, self.x_speed, self.y_speed)
            background.after(10, self.animate)

    player = Avatar()

    level1_window.bind("<Up>", player.up)
    level1_window.bind("<Down>", player.down)
    level1_window.bind("<Left>", player.left)
    level1_window.bind("<Right>", player.right)        
    
    def create():
        if counter() % 2 == 0:
            proyectile = Obstacle(random.randint(300, 1180), random.randint(50, 540), random.randint(-5, 5), random.randint(-5, 5))
            proyectile.animate()
        background.after(1000, create)

    create()    
#-------------------------------------------------------------------Menu principal---------------------------------------------------------------------------------------
menu_window = Tk()
menu_window.title("Juego") # Pendiente definir nombre
menu_window.geometry("1200x600")
menu_window.resizable(False, False)

avatar = PhotoImage(file="imagenes/soldado.png")
obstacle = PhotoImage(file="imagenes/proyectil.png")

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
