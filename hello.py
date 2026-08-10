import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sortable Treeview")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview.Heading",
    font=("Segoe UI", 11, "bold"),
    foreground="white",
    background="#2c3e50",
    relief="flat",
)
style.map("Treeview.Heading", background=[("active", "#34495e")])

# ---------- Treeview ----------
columns = ("name", "age", "score")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

# Column headings (we will update the text later to show ↑ / ↓)
tree.heading("name", text="Name", command=lambda: sort_column("name"))
tree.heading("age", text="Age", command=lambda: sort_column("age"))
tree.heading("score", text="Score", command=lambda: sort_column("score"))

tree.column("name", width=140, anchor="w")
tree.column("age", width=80, anchor="e")
tree.column("score", width=80, anchor="e")

# Sample data
data = [
    ("Alice", 28, 92),
    ("Bob", 34, 78),
    ("Charlie", 22, 95),
    ("Diana", 31, 88),
    ("Eve", 25, 81),
    ("Frank", 29, 70),
]

for item in data:
    tree.insert("", "end", values=item)

tree.pack(fill="both", expand=True, padx=10, pady=10)

# ---------- Sorting logic ----------
sort_states = {}  # keeps track of current sort direction per column
# True = ascending, False = descending


def sort_column(col):
    # Get all items
    items = [(tree.set(k, col), k) for k in tree.get_children("")]

    # Decide direction
    ascending = sort_states.get(col, True)

    # Try to sort numerically if possible, otherwise alphabetically
    try:
        items.sort(key=lambda t: float(t[0]), reverse=not ascending)
    except ValueError:
        items.sort(key=lambda t: t[0].lower(), reverse=not ascending)

    # Re-order the items in the tree
    for index, (val, k) in enumerate(items):
        tree.move(k, "", index)

    # Toggle direction for next click
    sort_states[col] = not ascending

    # Update all headings (clear arrows, then set the active one)
    for c in columns:
        text = c.capitalize()
        if c == col:
            text += " ↑" if ascending else " ↓"
        tree.heading(c, text=text)


root.mainloop()
