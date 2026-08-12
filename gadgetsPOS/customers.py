from tkinter import *
from tkinter import ttk
from CustomTitleBar import CustomToplevel
from database import get_searchCustomer
from database import get_customers


def open_customers(root):
    win = CustomToplevel(
        parent=root,
        title="CUSTOMERS",
        width=1750,
        height=780,
        x=120,
        y=220,
        bg="#0C131A",
    )

    win.configure(bd=2, highlightthickness=2, highlightcolor="#2c3e50")

    header_frame = Frame(win.content_area, bg="#0C131A")
    header_frame.pack(fill="x", side="top")

    header_frame.rowconfigure(0, weight=1)
    header_frame.columnconfigure(0, weight=0)
    header_frame.columnconfigure(1, weight=1)
    header_frame.columnconfigure(2, weight=0)

    search_frame = Frame(
        header_frame,
        bg="#0C131A",
    )
    search_frame.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    tools_frame = Frame(
        header_frame,
        bg="#0C131A",
    )
    tools_frame.grid(row=0, column=1, sticky="w", pady=10)

    def tools_bt(parent, text, command):
        return Button(
            parent,
            text=text,
            bg="#2c3e50",
            fg="white",
            width=4,
            font=("arial", 15),
            bd=0,
            command=command,
        )

    customerInfoButton = tools_bt(tools_frame, "ℹ", None)
    customerInfoButton.pack(side="left", padx=5)

    deleteCustomerBt = tools_bt(tools_frame, "    🗑️", None)
    deleteCustomerBt.pack(side="left", padx=5)

    updateCustomerBt = tools_bt(tools_frame, "    🔄️", update_customers)
    updateCustomerBt.pack(side="left", padx=5)

    addCustomerFrame = Frame(header_frame, bg="#0C131A")
    addCustomerFrame.grid(row=0, column=2, pady=10)

    search_entry = Entry(search_frame, width=15, font=("arial", 13))
    search_entry.pack(side="left", padx=10)

    cancel_searchButton = Button(
        search_frame,
        text="X",
        bd=0,
        bg="#0C131A",
        activebackground="#0C131A",
        command=lambda: clear_search_and_refresh(search_entry, customers),
        fg="white",
    )  # one
    cancel_searchButton.pack(side="left")

    def search():
        term = search_entry.get()
        get = get_searchCustomer(term)
        return load_data(get)

    search_button = Button(
        search_frame,
        text="🔎",
        font=("arial", 14),
        bd=0,
        fg="white",
        activebackground="#0C131A",
        bg="#0C131A",
        command=lambda: search(),
    )

    search_button.pack(side="left")

    body_frame = Frame(win.content_area, bg="#06203A")
    body_frame.pack(fill=BOTH, expand=True)

    style = ttk.Style()
    style.theme_use("clam")

    # Body style
    style.configure(
        "customer.Treeview",
        font=("Segoe UI", 13),
        foreground="#ffffff",
        background="#2c3e50",
        fieldbackground="#2c3e50",  # important for the actual rows
        rowheight=30,
        relief="flat",
    )

    # Heading style  ← note the "customer." prefix
    style.configure(
        "customer.Treeview.Heading",
        font=("Segoe UI", 15, "bold"),
        foreground="#2c3e50",
        background="#ecf0f1",  # or whatever colour you want
        relief="flat",
    )

    style.map(
        "customer.Treeview.Heading",
        background=[("active", "#34495e")],
        foreground=[("active", "white")],
    )

    # ---------- Scrollbar + Treeview ----------
    scrollbar = ttk.Scrollbar(body_frame, orient="vertical")

    columns = (
        "ID",
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

    tree["displaycolumns"] = (
        "CUSTOMER CODE",
        "CUSTOMER NAME",
        "CUSTOMER I.D",
        "CUSTOMER LOCATION",
        "CUSTOMER STATUS",
        "CUSTOMER CONTACTS",
    )

    scrollbar.configure(command=tree.yview)

    # Column widths
    for col in columns:
        tree.column(col, width=120, anchor="w")

    # Headings with sort command
    for col in columns:
        tree.heading(
            col,
            text=col,
            anchor="w",
            command=lambda c=col: sort_column(c),  # important: capture col correctly
        )

    # Pack once only
    scrollbar.pack(side="right", fill="y")
    tree.pack(side="left", fill="both", expand=True)

    # ---------- Data + Sorting ----------
    sort_states = {}  # col → True (asc) / False (desc)

    customers = get_customers()

    def load_data(data):
        tree.delete(*tree.get_children())

        if data:
            for phone in data:
                tree.insert(
                    "",
                    "end",
                    values=(
                        phone[0],
                        phone[1],
                        phone[3],
                        phone[2],
                        phone[4],
                        phone[6],
                        phone[5],
                    ),
                )

    load_data(customers)

    def clear_search_and_refresh(search_entry, data):
        search_entry.delete(0, END)
        load_data(data)

    def update_customers():
        pass

    def sort_column(col):
        items = [(tree.set(k, col), k) for k in tree.get_children("")]

        ascending = sort_states.get(col, True)

        try:
            items.sort(key=lambda t: float(t[0]), reverse=not ascending)
        except ValueError:
            items.sort(key=lambda t: str(t[0]).lower(), reverse=not ascending)

        for index, (_, k) in enumerate(items):
            tree.move(k, "", index)

        # Toggle direction
        sort_states[col] = not ascending

        # Update headings – keep original text + arrow
        for c in columns:
            text = c
            if c == col:
                text += " ↑" if ascending else " ↓"
            tree.heading(c, text=text)
