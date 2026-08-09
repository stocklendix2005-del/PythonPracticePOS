from tkinter import *
from CustomTitleBar import CustomToplevel


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
