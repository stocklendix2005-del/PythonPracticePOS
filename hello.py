import tkinter as tk

root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

def open_toplevel():
    top = tk.Toplevel(root)
    top.overrideredirect(True)          # remove native title bar
    top.geometry("400x250+100+100")

    def start_move(event):
        top.x = event.x
        top.y = event.y

    def do_move(event):
        x = top.winfo_x() + (event.x - top.x)
        y = top.winfo_y() + (event.y - top.y)
        top.geometry(f"+{x}+{y}")

    # Custom title bar
    title_bar = tk.Frame(top, bg="#2b2b2b", height=32)
    title_bar.pack(fill=tk.X)
    title_bar.bind("<Button-1>", start_move)
    title_bar.bind("<B1-Motion>", do_move)

    title_label = tk.Label(title_bar, text="Custom Toplevel", 
                           bg="#2b2b2b", fg="white", font=("Segoe UI", 10))
    title_label.pack(side=tk.LEFT, padx=12)
    title_label.bind("<Button-1>", start_move)
    title_label.bind("<B1-Motion>", do_move)

    close_btn = tk.Button(title_bar, text="✕", bg="#2b2b2b", fg="white",
                          bd=0, font=("Segoe UI", 12),
                          activebackground="#c42b1c", activeforeground="white",
                          command=top.destroy)
    close_btn.pack(side=tk.RIGHT, padx=8)

    # Content
    content = tk.Frame(top, bg="white")
    content.pack(fill=tk.BOTH, expand=True)
    tk.Label(content, text="This is a Toplevel with a custom title bar",
             bg="white").pack(pady=40)

btn = tk.Button(root, text="Open Toplevel with custom title bar",
                command=open_toplevel)
btn.pack(expand=True)

root.mainloop()