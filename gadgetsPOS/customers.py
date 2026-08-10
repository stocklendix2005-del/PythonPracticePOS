from tkinter import *
from tkinter import ttk
from CustomTitleBar import CustomToplevel
from database import get_customers


def open_customers(root):
    win = CustomToplevel(
        parent=root,
        title="CUSTOMERS",
        width=1750,
        height=780,
        x=140,
        y=200,
        bg="#0C131A",
    )

    header_frame = Frame(win.content_area, bg="#0C131A")
    header_frame.pack(fill="x", side="top")

    header_frame.rowconfigure(0, weight=1)
    header_frame.rowconfigure(1, weight=1)
    header_frame.columnconfigure(0, weight=0)
    header_frame.columnconfigure(1, weight=1)
    header_frame.columnconfigure(2, weight=0)

    header_lab = Label(
        header_frame,
        text="C u s t o m e r s",
        font=("arial", 15, "bold"),
        fg="white",
        bg="#0C131A",
    )
    header_lab.grid(row=0, column=1, columnspan=2)

    search_frame = Frame(
        header_frame,
        bg="#0C131A",
    )
    search_frame.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    search_entry = Entry(search_frame, width=15, font=("arial", 13))
    search_entry.pack(side="left", padx=10)

    cancel_searchButton = Button(
        search_frame,
        text="X",
        bd=0,
        bg="#0C131A",
        activebackground="#0C131A",
        command=search_entry.delete(0, END),
        fg="white",
    )  # one
    cancel_searchButton.pack(side="left")

    search_button = Button(
        search_frame,
        text="🔎",
        font=("arial", 14),
        bd=0,
        fg="white",
        activebackground="#0C131A",
        bg="#0C131A",
    )
    search_button.pack(side="left")

    body_frame = Frame(win.content_area, bg="#06203A")
    body_frame.pack(fill=BOTH, expand=True)

    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "customer.Treeview",
        font=("Segoe UI", 13),
        foreground="#ffffff",
        background="#2c3e50",
        rowheight=30,
        relief="flat",
    )
    style.map("Treeview.Heading", background=[("active", "#34495e")])

    style.configure(
        "Treeview.Heading", font=("Segoe UI", 15, "bold"), foreground="#2c3e50"
    )

    scrollbar = Scrollbar(body_frame, orient="vertical")
    columns = (
        "CUSTOMER CODE",
        "CUSTOMER NAME",
        "CUSTOMER I.D",
        "CUSTOMER LOCATION",
        "CUSTOMER STATUS",
        "CUSTOMER CONTACTS",
    )
    tree = ttk.Treeview(
        body_frame,
        columns=columns,
        show="headings",
        style="customer.Treeview",
        yscrollcommand=scrollbar.set,
    )
    scrollbar.configure(command=tree.yview)

    tree.column("CUSTOMER CODE", width=100)
    tree.column("CUSTOMER NAME", width=100)
    tree.column("CUSTOMER I.D", width=100)
    tree.column("CUSTOMER LOCATION", width=100)
    tree.column("CUSTOMER STATUS", width=100)
    tree.column("CUSTOMER CONTACTS", width=100)

    tree.heading(
        "CUSTOMER CODE",
        text="CUSTOMER CODE",
        anchor="w",
        command=lambda: sort_column("CUSTOMER CODE"),
    )
    tree.heading(
        "CUSTOMER NAME",
        text="CUSTOMER NAME",
        anchor="w",
        command=lambda: sort_column("CUSTOMER NAME"),
    )
    tree.heading(
        "CUSTOMER I.D",
        text="CUSTOMER I.D",
        anchor="w",
        command=lambda: sort_column("CUSTOMER I.D"),
    )
    tree.heading(
        "CUSTOMER LOCATION",
        text="CUSTOMER LOCATION",
        anchor="w",
        command=lambda: sort_column("CUSTOMER LOCATION"),
    )
    tree.heading(
        "CUSTOMER STATUS",
        text="CUSTOMER STATUS",
        anchor="w",
        command=lambda: sort_column("CUSTOMER STATUS"),
    )
    tree.heading(
        "CUSTOMER CONTACTS",
        text="CUSTOMER CONTACTS",
        anchor="w",
        command=lambda: sort_column("CUSTOMER CONTACTS"),
    )

    sort_states = {}  # keeps track of current sort direction per column
    # True = ascending, False = descending

    customers = get_customers()

    def load_data(data):
        for row in tree.get_children():
            tree.delete(row)
        for phone in data:
            tree.insert(
                "",
                END,
                values=(phone[1], phone[3], phone[2], phone[4], phone[6], phone[5]),
            )

    load_data(customers)

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

        scrollbar.pack(side="right")
        tree.pack(fill="both")
