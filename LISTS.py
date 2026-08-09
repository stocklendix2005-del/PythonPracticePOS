import tkinter as tk
    
root = tk.Tk()
root.geometry("600x400")
root.title("Animate Frame on Button Click")

# Main content
main_frame = tk.Frame(root, bg="#2c3e50")
main_frame.pack(fill="both", expand=True)

# The frame we will animate (starts hidden to the left)
slide_frame = tk.Frame(root, bg="#3498db", width=250)
slide_frame.place(x=-250, y=0, relheight=1)   # off-screen

# Content inside the sliding frame
tk.Label(slide_frame, text="Side Panel", font=("Arial", 18, "bold"),
         bg="#3498db", fg="white").pack(pady=30)
tk.Button(slide_frame, text="Close", command=lambda: slide_out()).pack(pady=10)

# Animation state
is_open = False

def slide_in(x=-250):
    global is_open
    if x < 0:
        slide_frame.place(x=x, y=0, relheight=1)
        root.after(8, slide_in, x + 10)   # speed = 10 pixels
    else:
        slide_frame.place(x=0, y=0, relheight=1)
        is_open = True

def slide_out(x=0):
    global is_open
    if x > -250:
        slide_frame.place(x=x, y=0, relheight=1)
        root.after(8, slide_out, x - 10)
    else:
        slide_frame.place(x=-250, y=0, relheight=1)
        is_open = False

def toggle():
    if is_open:
        slide_out()
    else:
        slide_in()

# Button that triggers the animation
tk.Button(main_frame, text="Open / Close Menu", font=("Arial", 14),
          command=toggle, bg="#e74c3c", fg="white", padx=20, pady=10).pack(pady=50)

root.mainloop()