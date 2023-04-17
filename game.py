import tkinter as tk

def move_ship_right(even):
    draw_game.coords(image_ship, 100, 0)
def move_ship_left(even):
    draw_game.coords(image_ship, 0, 100)    

win = tk.Tk()
draw_game = tk.Canvas(win, width=600, height=400, bg="#40B3E0")
draw_game.pack()
pic_sea = tk.PhotoImage(file="sea.png")
pic_ship = tk.PhotoImage(file="ship_100.png")


image_sea = draw_game.create_image(0, 100, anchor=tk.NW, image=pic_sea) 
image_ship = draw_game.create_image(0, 3, anchor=tk.NW, image=pic_ship)
win.bind('<Right>', move_ship_right)
win.bind('<Left>', move_ship_left)

win.mainloop()
