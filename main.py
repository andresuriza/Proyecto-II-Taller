"""
- Programadores: Jose Pablo Esquetini Fallas - 2021035767 y Andrés Uriza Lazo - 2021466844
- Projecto II
- Taller de programacion - CE1102
- Fecha de creacion: 04/06/2021
- Ultima modificacion: 22/06/2021
"""

# ---------------------------------------------------------------------------Libraries-----------------------------------------------------------------------------------

import pickle
import random
from tkinter import *

import pygame
from pygame import mixer

pygame.init()

# -------------------------------------------------------------------------Global Variables------------------------------------------------------------------------------

player_coords = [0, 0]
lives = 3
energy = 20

# ---------------------------------------------------------------------------Window class---------------------------------------------------------------------------------

class Window:
    # Window creation
    def window_creator(self):
        window = Tk()
        window.title("Jungle Escape")
        window.geometry("1000x650")
        window.iconbitmap("images/sans.ico")
        window.resizable(False, False)
        main_menu = MainMenu(window)
        main_menu.main_menu()


# ---------------------------------------------------------------------------Main menu class-----------------------------------------------------------------------------

class MainMenu:
    def __init__(self, place):
        self.window = place
        self.username = ""

    mixer.music.load("menu_song.wav")
    mixer.music.play(-1)  # loop

    # Main menu creation
    def main_menu(self):
        main_menu = Canvas(self.window, width=1000, height=650, bg="Black")
        main_menu.place(x=0, y=0)

        bg_image = PhotoImage(file="images/menu bg.png")
        bg_image_label = Label(main_menu, image=bg_image)
        bg_image_label.place(x=0, y=0)

        name_entry = Entry(main_menu, width=40)
        name_entry.place(x=430, y=225)

        # Username setting function
        def set_name():
            self.username = name_entry.get()
            self.window.after(1000 , set_name)
        
        set_name()

        play_button = Button(main_menu, font="Arial", text="Start Game", command=self.level1)
        play_button.place(x=450, y=300)

        level1_select = Button(main_menu, text="Level 1", font="Arial", command=self.level1)
        level1_select.place(x=365, y=400)

        level2_select = Button(main_menu, text="Level 2", font="Arial", command=self.level2)
        level2_select.place(x=465, y=400)

        level3_select = Button(main_menu, text="Level 3", font="Arial", command=self.level3)
        level3_select.place(x=560, y=400)

        about_button = Button(main_menu, text="About", font="Arial", command=self.about)
        about_button.place(x=470, y=500)

        hall_of_fame = Button(main_menu, font="Arial", text="Hall of Fame", command=self.hall_of_fame)
        hall_of_fame.place(x=445, y=560)

        # Setting window as the mainloop
        self.window.mainloop()

    # Level 1
    def level1(self):
        level1 = LevelCreation(1, self.window , self.username)
        level1.interface()

    # Level 2
    def level2(self):
        level2 = LevelCreation(2, self.window , self.username)
        level2.interface()

    # Level 3
    def level3(self):
        level3 = LevelCreation(3, self.window , self.username)
        level3.interface()

    # About
    def about(self):
        about = Canvas(self.window, width=1000, height=650, bg="Black")
        about.place(x=0, y=0)

        label1 = Label(about, text="About Jungle Escape", font=("Arial", 24), fg="White", bg="Black")
        label1.place(x=350, y=30)

        label2 = Label(about, text="Pais de Produccion: Costa Rica", font=("Arial", 16), fg="White", bg="Black")
        label2.place(x=30, y=100)

        label3 = Label(about, text="Ingenieria en Computadores - Instituto Tecnologico de Costa Rica",
                       font=("Arial", 16), fg="White", bg="Black")
        label3.place(x=30, y=150)

        label4 = Label(about, text="Taller de Programacion CE-1102", font=("Arial", 16), fg="White", bg="Black")
        label4.place(x=30, y=200)

        label5 = Label(about, text="Primer Semestre, 2021", font=("Arial", 16), fg="White", bg="Black")
        label5.place(x=30, y=250)

        label6 = Label(about, text="Jeff Schmidt Peralta, Grupo 01", font=("Arial", 16), fg="White", bg="Black")
        label6.place(x=30, y=300)

        label7 = Label(about, text="Python, Version: 3.9", font=("Arial", 16), fg="White", bg="Black")
        label7.place(x=30, y=350)

        label8 = Label(about, text="Autores: Andres Uriza Lazo y Jose Pablo Esquetini Fallas", font=("Arial", 16), fg="White",
                       bg="Black")
        label8.place(x=30, y=400)

        label9 = Label(about,
                       text="Modulos utilizados: Pygame, por: Lenard Lindstrom, René Dudfield, Pete Shinners, Nicholas Dudfield",
                       font=("Arial", 16), fg="White", bg="Black")
        label9.place(x=30, y=450)

        label9b = Label(about, text="y Thomas Kluyver.", font=("Arial", 16), fg="White", bg="Black")
        label9b.place(x=30, y=480)

        label10 = Label(about,
                        text="Jungle Escape es un juego de movimiento, este se realiza con las 4 flechas del teclado",
                        font=("Arial", 16), fg="White", bg="Black")
        label10.place(x=30, y=530)

        go_back = Button(about, text="Main Menu", font="Arial", command=self.main_menu)
        go_back.place(x=30, y=580)

    # ----------------------------------------------------------------------------Hall of fame-------------------------------------------------------------------------------

    def divide(self, list, i, j):  # Funcion que genera particiones mayores y menores de una lista a partir de un pivot
        pivot = list[i]
        left = i + 1
        right = j

        while left <= right:  # Mientras el puntero izquierdo este antes que el derecho
            if list[left] < pivot:
                left += 1
            else:
                if list[right] > pivot:
                    right -= 1
                else:
                    list[left], list[right] = list[right], list[left]  # Se intercambian punteros
                    left += 1
                    right -= 1
        list[i], list[right] = list[right], list[i]  # Se posiciona pivot
        return right  # Retorna nueva posicion del pivot

    def quicksort(self, list, start, end):  # Funcion que genera particiones de una lista hasta que quede ordenada
        if start < end:  # Mientras puntero izquierdo este antes que el derecho (lista en total)
            partition = self.divide(list, start, end)
            self.quicksort(list, start, partition - 1)
            self.quicksort(list, partition + 1, end)

    def points(self, score):  # Funcion que lee los puntos en binario de un archivo .txt, los ordena y reescribe si necesario

        file = open("puntajes.txt", "rb")
        top_10 = pickle.load(file)
        top_10.append(score)
        file.close()
        self.quicksort(top_10, 0, len(top_10) - 1)

        file = open("puntajes.txt", "wb")
        if len(top_10) > 10:  # Si los puntajes se exceden de 10, se recorta el menor
            top_10 = top_10[1:]
        pickle.dump(top_10, file)
        print(top_10)
        file.close()

        self.hall_of_fame()

    
    def hall_of_fame(self):
        points = Canvas(self.window , width=1000, height=650, bg="Black")
        points.place(x=0, y=0)
        
        """
        # Para reestablecer puntajes
        file = open("puntajes.txt", "wb")
        pickle.dump([0,0,0,0,0,0,0,0,0,0], file)
        file.close()
        """

        file = open("puntajes.txt", "rb")
        top_10 = pickle.load(file)
        file.close()

        label1 = Label(points , text = "Hall of Fame" , font = ("Arial" , 24) , bg = "Black" , fg = "White")
        label1.place(x = 400 , y = 30)

        no_1 = Label(points, text="1) " + str(top_10[9]), font = ("Arial" , 16) , bg="Black", fg="White")
        no_1.place(x=30, y=100)

        no_2 = Label(points, text="2) " + str(top_10[8]), font = ("Arial" , 16) , bg="Black", fg="White")
        no_2.place(x=30, y=150)

        no_3 = Label(points, text="3) " + str(top_10[7]), font = ("Arial" , 16) , bg="Black", fg="White")
        no_3.place(x=30, y=200)

        no_4 = Label(points, text="4) " + str(top_10[6]), font = ("Arial" , 16) , bg="Black", fg="White")
        no_4.place(x=30, y=250)

        no_5 = Label(points, text="5) " + str(top_10[5]), font = ("Arial" , 16) , bg="Black", fg="White")
        no_5.place(x=30, y=300)

        no_6 = Label(points, text="6) " + str(top_10[4]), font = ("Arial" , 16) , bg="Black", fg="White")
        no_6.place(x=30, y=350)

        no_7 = Label(points, text="7) " + str(top_10[3]), font = ("Arial" , 16) , bg="Black", fg="White")
        no_7.place(x=30, y=400)

        no_8 = Label(points, text="8) " + str(top_10[2]), font = ("Arial" , 16) , bg="Black", fg="White")
        no_8.place(x=30, y=450)

        no_9 = Label(points, text="9) " + str(top_10[1]), font = ("Arial" , 16) , bg="Black", fg="White")
        no_9.place(x=30, y=500)

        no_10 = Label(points, text="10) " + str(top_10[0]), font = ("Arial" , 16) , bg="Black", fg="White")
        no_10.place(x=30, y=550)

        go_back = Button(points , text="Main Menu", font="Arial", command=self.main_menu)
        go_back.place(x=500, y=550)


class Avatar:
    def __init__(self, window, avatar_pic, level):
        self.avatar_pic = avatar_pic
        self.level = level
        self.window = window
        self.window.bind("<Up>", self.up)
        self.window.bind("<Down>", self.down)
        self.window.bind("<Left>", self.left)
        self.window.bind("<Right>", self.right)
        self.get_coords()

    def get_coords(self): # Indicates the player's current location
        global player_coords
        position = self.level.coords(self.avatar_pic)
        player_coords = position
        self.level.after(10, self.get_coords)

    def left(self, key):  # Mueve al avatar a la izquierda
        if self.level.coords(self.avatar_pic)[0] > 260:
            self.level.move(self.avatar_pic, -20, 0)

    def right(self, key):  # Mueve al avatar a la derecha
        if self.level.coords(self.avatar_pic)[0] < 890:
            self.level.move(self.avatar_pic, 20, 0)

    def up(self, key):  # Mueve al avatar hacia arriba
        if self.level.coords(self.avatar_pic)[1] > 10:
            self.level.move(self.avatar_pic, 0, -20)

    def down(self, key):  # Mueve al avatar hacia abajo
        if self.level.coords(self.avatar_pic)[1] < 490:
            self.level.move(self.avatar_pic, 0, 20)


class Obstacle:
    def __init__(self, window, level, speed):
        self.window = window
        self.level = level
        self.x_speed = speed
        self.y_speed = speed
        self.counter = 0
        self.proyectile_image = PhotoImage(file="images/shuriken.png")
        self.options = [[260, random.randint(10, 575)], [925, random.randint(10, 575)],
                        [random.randint(260, 925), 10], [random.randint(260, 925), 575]]
        self.coords = random.choice(self.options)
        self.proyectile = self.level.create_image(self.coords[0], self.coords[1], image=self.proyectile_image , anchor = NW)
        self.bouncer()
        self.animate()
        self.collision()

    # Function that makes sure that all the projectiles move inside the map
    def bouncer (self):
        if self.coords[0] == 260 and self.x_speed < 0:
            self.x_speed *= -1
        if self.coords[0] == 925 and self.x_speed > 0:
            self.x_speed *= -1
        if self.coords[1] == 10 and self.y_speed < 0:
            self.y_speed *= -1
        if self.coords[1] == 575 and self.y_speed > 0:
            self.y_speed *= -1

    # Collision checker function
    def collision(self):
        global player_coords
        position = self.level.coords(self.proyectile)
        player_hitbox = [player_coords[0], player_coords[1], 85, 130]
        proyectile_hitbox = [position[0], position[1], 75, 75]
        hurt = mixer.Sound("hurt.wav")

        if player_hitbox[0] < proyectile_hitbox[0] + proyectile_hitbox[2] and player_hitbox[0] + player_hitbox[2] > \
                proyectile_hitbox[0] and player_hitbox[1] < proyectile_hitbox[1] + proyectile_hitbox[3] and \
                player_hitbox[1] + player_hitbox[3] > proyectile_hitbox[1]:
            global energy
            hurt.play()
            energy -= 1
            self.level.delete(self.proyectile)
        self.level.after(100, self.collision)

    def animate(self):  # Mueve a los proyectiles
        shuriken = mixer.Sound("shuriken.wav")

        if self.counter != 2:
            position = self.level.coords(self.proyectile)
            x = position[0]
            y = position[1]
            if x >= 930 or x <= 250:
                self.counter += 1
                self.x_speed = -self.x_speed
                shuriken.play()
            if y >= 580 or y <= 5:
                self.counter += 1
                self.y_speed = -self.y_speed
                shuriken.play()
            self.level.move(self.proyectile, self.x_speed, self.y_speed)
            self.window.after(10, self.animate)
        else:
            self.level.delete(self.proyectile)



# Level creation class


class LevelCreation:
    def __init__(self, level, place , name):
        global lives, energy
        lives = 3
        energy = 20
        self.level = level
        self.window = place
        self.seconds = 60
        self.points = 0
        self.lives = lives
        self.energy = energy
        self.name = name

        if level == 1:
            self.speed_options = [-5 , -4 , -3, 3 , 4 , 5]
            self.projectile = 3
            self.reward = 1
        if level == 2:
            self.speed_options = [-6 , -5 , -4 , -3, 3 , 4 , 5 , 6]
            self.projectile = 2
            self.reward = 3
        if level == 3:
            self.speed_options = [-7 , -6 , -5 , -4 , -3, 3 , 4 , 5 , 6 , 7]
            self.projectile = 1
            self.reward = 5

    def go_back_points(self): # Retorna al menu principal, y procesa el puntaje obtenido
        main_menu = MainMenu(self.window)
        main_menu.points(self.points)
        main_menu.main_menu()
        
       
    def interface(self):  # Define los elementos del nivel
        level_canvas = Canvas(self.window, width=1000, height=650)
        level_canvas.place(x=0, y=0)

        bg_image = PhotoImage(file="images/level image.png")
        level_canvas.create_image(250, 0, image=bg_image, anchor=NW)

        score_canvas = Canvas(self.window, width=250, height=650, bg="Black")
        score_canvas.place(x=0, y=0)

        ninja = PhotoImage(file="images/ninja.png")
        ninja_pic = level_canvas.create_image(610, 300, image=ninja , anchor = NW)
        player = Avatar(self.window, ninja_pic, level_canvas)

        def UI():
            if self.seconds == 0 or self.lives == 0:
                self.go_back_points()

            timer = Label(score_canvas, text=f"Time: {self.seconds}", font=("Arial", 16), bg="Black", fg="White", borderwidth=11)
            timer.place(x=23, y=125)

            score = Label(score_canvas, text=f"Score: {self.points}", font=("Arial", 16), bg="Black", fg="White")
            score.place(x=30, y=200)

            lives = Label(score_canvas , text= f"Player's Lives: {self.lives}" , font = ("Arial" , 16) , fg = "White" , bg = "Black")
            lives.place(x = 30 , y = 350)

            energy = Label(score_canvas , text = f"Energy left: {self.energy}   " , font = ("Arial" , 16) , fg = "White" , bg = "Black")
            energy.place(x = 30 , y = 425)

            self.window.after(100, UI)

        UI()

        # UI elements that do not change
        if self.level == 1:
            level_name = Label(score_canvas, text="Level 1", font=("Arial", 24), bg="Black", fg="White")
        if self.level == 2:
            level_name = Label(score_canvas, text="Level 2", font=("Arial", 24), bg="Black", fg="White")
        if self.level == 3:
            level_name = Label(score_canvas, text="Level 3", font=("Arial", 24), bg="Black", fg="White")

        level_name.place(x=30, y=50)

        username = Label(score_canvas , text = f"Username: {self.name}" , font = ("Arial" , 16) , fg = "White" , bg = "Black")
        username.place(x = 30 , y = 275)

        main_menu_button = Button(self.window, text="Go back", font=("Arial", 16), bg="White", fg="Black", command=self.go_back_points)
        main_menu_button.place(x=30, y=500)

        # Seconds Counter
        def counter():  
            self.seconds -= 1
            self.points += self.reward
            self.window.after(1000, counter)

        counter()

        # Projectile creator
        def creator():
            self.speed = random.choice(self.speed_options)
            proyectile = Obstacle(self.window, level_canvas, self.speed)
            self.window.after(300 * self.projectile , creator)
        
        creator()

        # Lives and energy updates
        def update():
            global lives, energy
            self.lives = lives
            self.energy = energy
            if energy == 0:
                lives -= 1
                energy = 20
            self.window.after(100 , update)
        
        update()

        level_canvas.mainloop()

    """
    Logica para sonido de herido

    

    Logica para sonido de shuriken rebotando con un borde

    
    """


# Creating the window object
game = Window()
game.window_creator()
