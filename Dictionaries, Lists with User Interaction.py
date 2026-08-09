import tkinter as tk

root = tk.Tk()
root.title("Tkinter Canvas Tutorial")
root.geometry("800x600")

# Create Canvas
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack(fill="both", expand=True)

# Draw shapes
canvas.create_rectangle(50, 50, 250, 200, fill="#3498db", outline="black", width=3)
canvas.create_oval(300, 50, 500, 250, fill="#e74c3c")
canvas.create_line(50, 300, 600, 300, fill="black", width=5)

# Text
canvas.create_text(400, 350, text="Hello Canvas!", font=("Arial", 24, "bold"), fill="blue")

root.mainloop()