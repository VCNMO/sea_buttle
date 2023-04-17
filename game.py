import tkinter as tk
v = 10
x = 0
y = 3 
y_boom = 300
boom = False

def animation():
    global x, v
    x += v
    if boom:
        y_boom -= 5
        draw_game.coords(image_boom, 300, y_boom)    
    if x > 600:
        v = -v
    if x < -100:
        v = -v
    draw_game.coords(image_ship, x, y)
    draw_game.after(20, animation)
    
def move_ship_right(even):
    global x
    x += v
    draw_game.coords(image_ship, x, y)
    
def move_ship_left(even):
    global x
    x -= v
    draw_game.coords(image_ship, x, y)    

def move_ship_up(even):
    global boom
    boom = not boom
    print(boom)

win = tk.Tk()
draw_game = tk.Canvas(win, width=600, height=400, bg="#40B3E0")
draw_game.pack()
pic_sea = tk.PhotoImage(file="sea.png")
pic_ship = tk.PhotoImage(file="ship_100.png")
pic_boom = tk.PhotoImage(file="boom2.png")


image_sea = draw_game.create_image(0, 100, anchor=tk.NW, image=pic_sea) 
image_ship = draw_game.create_image(x, y, anchor=tk.NW, image=pic_ship)
image_boom = draw_game.create_image(300, 300, anchor=tk.NW, image=pic_boom)
#win.bind('<Right>', move_ship_right)
#win.bind('<Left>', move_ship_left)
#win.bind('<Up>', move_ship_up)
animation()

win.mainloop()
