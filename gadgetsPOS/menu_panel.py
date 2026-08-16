from tkinter import *


def sliding_menu(root):

    menu_height = 195

    slide_frame = Frame(root, bg="#3498db", height=menu_height)

    # Start above the top of the window
    slide_frame.place(x=0, y=-menu_height, relwidth=1)

    canvas = Canvas(slide_frame, bg="#0C131A", height=menu_height)
    canvas.pack(fill=BOTH, expand=True)

    button_menu = []

    menu_frame = Frame(canvas, bg="#FFFFFF")
    canvas_window = canvas.create_window((0, 0), window=menu_frame, anchor="nw")

    menu_frame.grid_columnconfigure(0, weight=1)
    menu_frame.grid_columnconfigure(1, weight=1)
    menu_frame.grid_columnconfigure(2, weight=1)
    menu_frame.grid_columnconfigure(3, weight=1)
    menu_frame.grid_columnconfigure(4, weight=1)

    is_open = False

    def slide_in(y=-menu_height):
        nonlocal is_open

        if y < 0:
            slide_frame.place(x=0, y=y, relwidth=1)

            root.after(8, slide_in, y + 10)

        else:
            slide_frame.place(x=0, y=0, relwidth=1)
            is_open = True

    def slide_out(y=0):
        nonlocal is_open

        if y > -menu_height:
            slide_frame.place(x=0, y=y, relwidth=1)

            root.after(8, slide_out, y - 10)

        else:
            slide_frame.place(x=0, y=-menu_height, relwidth=1)
            is_open = False

    def toggle():
        if is_open:
            slide_out()
        else:
            slide_in()

    return slide_frame, toggle
