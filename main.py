"""
- Programadores: Jose Pablo Esquetini Fallas - 2021035767 y Andrés Uriza Lazo - 2021466844
- Projecto II
- Taller de programacion - CE1102
- Fecha de creacion: 04/06/2021
- Ultima modificacion: 05/06/2021
"""

#---------------------------------------------------------------------------Libraries-----------------------------------------------------------------------------------

from tkinter import * 
import time
import random
import pickle

#-------------------------------------------------------------------------Global Variables------------------------------------------------------------------------------

seconds = 0

#---------------------------------------------------------------------------Window class---------------------------------------------------------------------------------

class Window():
    # Window creation
    def window_creator(self):
        window = Tk()
        window.title("Jungle Escape")
        window.geometry("1000x650")
        window.iconbitmap("images/sans.ico")
        window.resizable(False, False)
        main_menu = MainMenu(window)
        main_menu.main_menu()
#---------------------------------------------------------------------------Main menu class-----------------------------------------------------------------------------

class MainMenu():
    def __init__(self , place):
        self.window = place

    # Main menu creation
    def main_menu(self):
        main_menu = Canvas(self.window , width = 1000 , height = 650 , bg = "Black")
        main_menu.place(x = 0 , y = 0)

        bg_image = PhotoImage(file ="images/menu bg.png")
        bg_image_label = Label(main_menu , image = bg_image)
        bg_image_label.place(x = 0 , y = 0)

        name_entry = Entry(main_menu, width=40)
        name_entry.place(x=430, y=225)

        play_button = Button(main_menu, font="Arial", text="Start Game" , command = self.level1)
        play_button.place(x=450, y=300)

        level1_select = Button(main_menu, text="Level 1", font="Arial", command = self.level1)
        level1_select.place(x=365, y=400)

        level2_select = Button(main_menu, text="Level 2", font="Arial" , command = self.level2)
        level2_select.place(x=465, y=400)

        level3_select = Button(main_menu, text="Level 3", font="Arial" , command = self.level3)
        level3_select.place(x=560, y=400)

        about = Button(main_menu, font="Arial", text="About")
        about.place(x=470, y=500)

        hall_of_fame = Button(main_menu, font="Arial", text="Hall of Fame")
        hall_of_fame.place(x=445, y=560)

        # Setting window as the mainloop
        self.window.mainloop()
    
    # Level 1
    def level1(self):
        level1 = LevelCreation(1 , self.window) 
        level1.interface()

    # Level 2
    def level2(self):
        level2 = LevelCreation(2 , self.window) 
        level2.interface()
    
    # Level 3
    def level3(self):
        level3 = LevelCreation(3 , self.window) 
        level3.interface()

    #----------------------------------------------------------------------------Hall of fame-------------------------------------------------------------------------------

    def divide(self, list, i, j): # Funcion que genera particiones mayores y menores de una lista a partir de un pivot
        pivot = list[i]
        left = i + 1
        right = j

        while left <= right: # Mientras el puntero izquierdo este antes que el derecho
            if list[left] < pivot:
                left += 1
            else:
                if list[right] > pivot:
                    right -= 1
                else:
                    list[left], list[right] = list[right], list[left] # Se intercambian punteros
                    left += 1
                    right -= 1
        list[i], list[right] = list[right], list[i] # Se posiciona pivot
        return right # Retorna nueva posicion del pivot


    def quicksort(self, list, start, end): # Funcion que genera particiones de una lista hasta que quede ordenada
        if start < end: # Mientras puntero izquierdo este antes que el derecho (lista en total)
            partition = self.divide(list, start, end)
            self.quicksort(list, start, partition - 1)
            self.quicksort(list, partition + 1, end)


    def points(self, score): # Funcion que lee los puntos en binario de un archivo .txt, los ordena y reescribe si necesario
        file = open("puntajes.txt", "rb")
        top_10 = pickle.load(file)
        top_10.append(score)
        file.close()
        self.quicksort(top_10, 0, len(top_10) - 1)
        
        file = open("puntajes.txt", "wb")
        if len(top_10) > 10: # Si los puntajes se exceden de 10, se recorta el menor
            top_10 = top_10[1:]
        pickle.dump(top_10, file)
        file.close()

        file = open("puntajes.txt", "rb")
        top_10 = pickle.load(file)
        print(top_10)
        file.close()
        

# Level creation class

class LevelCreation():
    def __init__(self , level , place):
        self.window = place
        if level == 1:
            self.speed = 5
            self.projectile = 4
        elif level == 2:
            self.speed = 5
            self.projectile = 3
        elif level == 3:
            self.speed = 5
            self.projectile = 2

    def interface(self):
        level = Canvas(self.window , width = 1200 , height = 650 , bg = "Black")
        level.place(x = 0 , y = 0)

        bg_image = PhotoImage(file = "images/level image.png")
        image_label = Label(level , image = bg_image)
        image_label.place(x = 250 , y = 0)

        score = Label(level , text = "score" , font = ("Arial" , 16) , bg = "Black" , fg = "White")
        score.place(x = 30 , y = 100)

        main_menu_button = Button(self.window , text = "End Game" , font = ("Arial" , 16) , bg = "White" , fg = "Black" , command = self.go_back)
        main_menu_button.place(x = 30 , y = 200)

        def hello(self): # esto solo es para asegurarme que el canvas sigue funcionando, luego lo quito
            print("I'm still here")
            level.after(1000 , hello , self)
        
        hello(self)

        level.mainloop()

    def go_back(self):
        main_menu = MainMenu(self.window)
        main_menu.main_menu()

"""
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
"""

# Creating the window object
game = Window()
game.window_creator()


# https://stackabuse.com/quicksort-in-python    Para saber como implementar el algoritmo quicksort
# https://www.codegrepper.com/code-examples/python/read+a+text+file+in+python+and+dump+the+contents  Para saber como utilizar Pickle