import tkinter
x = 0

y_bomb = 530
x_bomb = 400

v = 10
press = False
move_ship = True

def animation():
    global x, v, y_bomb, press, move_ship
    if move_ship == True:
        x = x + v
    if x > 800:
        v = -v
    if x < -100:
        v = -v    
    draw.coords(draw_ship, x, 50)
    if press == True:
        y_bomb = y_bomb - 20
        if y_bomb < 150:
            if x_bomb > x and x_bomb < x + 100:
                draw.coords(draw_boom, x-30, 50-30)
                move_ship = False
            y_bomb = 530
            press = False
        draw.coords(draw_bomb, x_bomb, y_bomb)
    draw.after(20, animation)

def move_up(event):
    global press
    press = True
    
def new_game(event):
    global move_ship, x, v
    draw.coords(draw_boom, -400, -400)
    move_ship = True
    x = 0
    v = 10

def move_right(event):
    global x_bomb
    x_bomb = x_bomb + 10
    draw.coords(draw_bomb, x_bomb, y_bomb)
    
def move_left(event):
    global x_bomb
    x_bomb = x_bomb - 10
    draw.coords(draw_bomb, x_bomb, y_bomb)   

win = tkinter.Tk()
draw = tkinter.Canvas(win, bg="#1C71C6", width=800, height=600)
draw.pack()

# загрузить картинки
img_sea = tkinter.PhotoImage(file='sea.png')
draw.create_image(0, 150, image=img_sea, anchor=tkinter.NW)

img_bomb = tkinter.PhotoImage(file='bomb.png')
draw_bomb = draw.create_image(400, 530, image=img_bomb, anchor=tkinter.NW)

img_ship = tkinter.PhotoImage(file='ship.png')
draw_ship = draw.create_image(0, 50, image=img_ship, anchor=tkinter.NW)

img_boom = tkinter.PhotoImage(file='boom.png')
draw_boom = draw.create_image(-200, -200, image=img_boom, anchor=tkinter.NW)


#управление бомбой
win.bind('<Right>', move_right)
win.bind('<Left>', move_left)

# управление бомбой
win.bind('<Up>', move_up)

# играть сначала
win.bind('<space>', new_game)

animation()
win.mainloop()