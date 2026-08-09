from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import os
import sys
import pywinstyles

import sqlite3
from menu_panel import sliding_menu
from notifications import open_notifications
from customers import open_customers

window = Tk()
window.title("Len App")
# window.geometry("400x400")
window.state("zoomed")
window.lift()
window.focus_force()
Icon = PhotoImage(file="C:\\python-practice\\image1.png")
window.iconphoto(True, Icon)
window.config(background="#d9d8ea")

dashboard_frame = Frame(window, bg="#0C131A")
dashboard_frame.rowconfigure(0, weight=0)
dashboard_frame.rowconfigure(1, weight=1)
dashboard_frame.rowconfigure(2, weight=0)
dashboard_frame.columnconfigure(0, weight=0)
dashboard_frame.columnconfigure(1, weight=1)
dashboard_frame.columnconfigure(2, weight=0)

img_path = r"C:\python-practice\submit-button-png-18010.png"
pil_img = Image.open(img_path)
pil_img = pil_img.resize((70, 40), Image.Resampling.LANCZOS)
submit__button = ImageTk.PhotoImage(pil_img)

img_path = r"C:\\python-practice\\delete-button-png-28554.png"
pil_img = Image.open(img_path)
pil_img = pil_img.resize((70, 40), Image.Resampling.LANCZOS)
delete__button = ImageTk.PhotoImage(pil_img)

img_path = r"C:\python-practice\logo.png"
pil_img = Image.open(img_path)
pil_img = pil_img.resize((120, 100), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(pil_img)

img_path = r"C:\python-practice\instructions.png"
pil_img = Image.open(img_path)
pil_img = pil_img.resize((500, 800), Image.Resampling.LANCZOS)
instructionspng = ImageTk.PhotoImage(pil_img)

slide_frame, toggle = sliding_menu(window)

menu_button = Button(
    dashboard_frame,
    text="☰",
    font=("arial", 25, "bold"),
    bg="#0C131A",
    bd=0,
    activebackground="#0C131A",
    fg="white",
    command=toggle,
)
menu_button.grid(row=0, column=0, sticky="nw", pady=25, padx=15)

dashboard_frame.pack(fill=BOTH, expand=True)
dashboard_label = Label(
    dashboard_frame,
    text="D A S H B O A R D   M E N U",
    fg="#FFFFFF",
    font=("Arial", 25, "bold"),
    bg="#0C131A",
    height=5,
    width=50,
)
dashboard_label.grid(row=0, column=1, sticky="s")

notification_button = Button(
    dashboard_frame,
    text="🔔",
    font=("arial", 25),
    fg="white",
    bg="#0C131A",
    bd=0,
    command=lambda: open_notifications(window),
    activebackground="#0C131A",
)
notification_button.grid(row=0, column=2, sticky="ne", pady=20, padx=15)

tools_frame = Frame(dashboard_frame, bg="#0C131A")
tools_frame.grid(row=1, column=0, sticky="nsew")


open_customer = Button(
    tools_frame,
    text="👥",
    bg="#0C131A",
    width=5,
    fg="white",
    command=lambda: open_customers(window),
    activebackground="#0C131A",
    activeforeground="white",
    font=("arial", 20),
    bd=0,
)
open_customer.pack(pady=(10, 0))
open_customer_lab = Label(
    tools_frame, text="Customers", width=10, bg="#0C131A", fg="white", font=("arial", 8)
)
open_customer_lab.pack(pady=(0, 20))

open_gadget = Button(
    tools_frame,
    text="   🖥️",
    bg="#0C131A",
    width=5,
    fg="white",
    activebackground="#0C131A",
    activeforeground="white",
    font=("arial", 20),
    bd=0,
)
open_gadget.pack(pady=(10, 0), padx=(5, 0))
open_gadget_lab = Label(
    tools_frame, text="Inventory", width=10, bg="#0C131A", fg="white", font=("arial", 8)
)
open_gadget_lab.pack(pady=(0, 20))

open_finance = Button(
    tools_frame,
    text="🪙",
    bg="#0C131A",
    width=5,
    fg="white",
    activebackground="#0C131A",
    activeforeground="white",
    font=("arial", 30),
    bd=0,
)
open_finance.pack(pady=(10, 0), padx=(0, 5))
open_finance_lab = Label(
    tools_frame, text="Finance", width=10, bg="#0C131A", fg="white", font=("arial", 8)
)
open_finance_lab.pack(pady=(0, 20))

open_settings = Button(
    tools_frame,
    text="    🛠️",
    bg="#0C131A",
    width=5,
    fg="white",
    activebackground="#0C131A",
    activeforeground="white",
    font=("arial", 30),
    bd=0,
)
open_settings.pack(pady=(10, 0), padx=(0, 5))
open_settings_lab = Label(
    tools_frame, text="Settings", width=10, bg="#0C131A", fg="white", font=("arial", 8)
)
open_settings_lab.pack(pady=(0, 20))

body_frame = Frame(dashboard_frame, bg="white")
body_frame.grid(row=1, column=1, sticky="nsew")


# body_frame = Frame(window,bd=2)
# body_frame.configure(bg="#030035",relief="groove",bd=3)
# body_frame.pack(fill=BOTH,expand=True)

img_path = r"C:\python-practice\logo.png"
pil_img = Image.open(img_path)
pil_img = pil_img.resize((2000, 800), Image.Resampling.LANCZOS)
body_image = ImageTk.PhotoImage(pil_img)
Label(body_frame, image=body_image).place(x=0, y=0, relwidth=1, relheight=1)


Label(
    dashboard_frame,
    text="Copyright © 2026 LEN APP. All rights reserved.",
    font=("calibri", 12),
    fg="white",
    bg="#0C131A",
).grid(row=2, column=1, sticky="s", pady=10)

# exit_button = Button(bottom_frame,
#                      text=' EXIT ',
#                      font=("Arial",18),
#                      bg="#1A1D20",
#                      fg='white',
#                      width=10,
#                      height=0,
#                      activebackground='red',
#                      command=window.destroy
#                      )
# exit_button.pack(pady=10,side="bottom")


# def info_frame():
#     i_frame = Frame(body_frame,
#                     bg="#1A1D20",
#                     bd=2,
#                     height=400,
#                     width=100)
#     i_frame.pack(side=TOP,expand=True)
#     text_widget = Text(i_frame, wrap="word", font=("Arial", 12),
#                        bg="#d9d8ea",
#                       height=10)
#     text_widget.pack(padx=10,fill=X, pady=10)
#     text_content =("""Ownership: LEN APP, including its design, code, and content, is the exclusive property of its creators. Unauthorized reproduction or distribution is prohibited.

# Usage Rights: Users are granted a limited, non-transferable license to use LEN APP for managing stock and sales.

# Data Privacy: LEN APP respects user data. Sales and inventory records remain confidential and are not shared with third parties without consent.

# Limitations: LEN APP is provided “as is.” The creators are not liable for losses resulting from misuse, technical errors, or inaccurate data entry.

# Updates: Features may be updated periodically. Continued use of LEN APP implies acceptance of new terms.

# Termination: Violation of these terms may result in suspension or termination of access.""")
#     text_widget.insert("1.0", text_content)
#     text_widget.config(state="disabled",
#                        background="#DBBC93",
#                      fg='black',)
#     back_bt = Button(i_frame,text="Quit",
#                      bg="#DBBC93",
#                      fg='black',
#                      font=('Arial',13),
#                      command=i_frame.destroy)
#     back_bt.pack(pady=15,side=BOTTOM)

# info_bt = Button(body_frame,
#                      text='T&Cs ',
#                      font=("Arial",18),
#                      bg="#FF9100",
#                      fg="#1A1D20",
#                      width=10,
#                      height=0,
#                      activebackground='red',
#                      command=info_frame
#                      )
# info_bt.place(relx=0.50,rely=0.75,anchor="center")

# text_label = Label(body_frame,
#                    text="Welcome to dashboard menu!",
#                    font=('Arial',30,'bold'),
#                    fg="#00F0FF",
#                    bg="#1A1D20",
#                 #    image=body_image,
#                    compound="bottom",
#                    width=30)
# text_label.place(relx=0.50,rely=0.15,anchor="center")

# def stock_alert():
#     for widget in not_frame.winfo_children():
#         widget.destroy()

#     conn = sqlite3.connect('phones.db')
#     c = conn.cursor()
#     c.execute('SELECT * FROM phones WHERE quantity < 5')
#     phones = c.fetchall()
#     conn.close()

#     if not phones:
#         Label(not_frame,text='No Notifications!',
#               font=('arial',12,'bold'),
#               fg='red',
#               bg="#1A1D20"
#               ).pack()
#     else:
#         for phone in phones:
#             Label(not_frame,text=f"{phone[1]} {phone[2]} is low on stock ⚠",
#                   font=("arial",13),
#                   bg="#1A1D20",
#                   fg='white').pack(pady=3)
#     window.after(5000,stock_alert)


# # not_frame = Frame(dashboard_frame,bg="#1A1D20")
# # not_frame.configure(height=10)
# # not_frame.pack(expand=True)

# stock_alert()

# text_label2 = Label(body_frame,
#                     text="\nThe navigation pannel involve:",
#                      fg="#d9d8ea",
#                      bg="#d9d8ea",
#                      font=('Arial',18,'bold'),
#                      width=500,
#                      height=5
#                      )
# text_label2.pack(pady=20)


def create_styled_button(parent, lb, cmd=None):
    return Button(
        parent,
        text=lb,
        fg="#1A1D20",
        font=("Arial", 14, "bold"),
        bg="#00F0FF",
        relief="groove",
        command=cmd,
        width=50,
        height=1,
    )


def open_add_gadget():
    add_window = Toplevel(window)
    add_window.transient(window)
    add_window.grab_set()
    add_window.geometry("500x900+690+50")
    add_window.config(background="#d9d8ea")
    add_window.title("ADD GADGET")
    label = Label(
        add_window,
        text="Follow Below Steps to Add Gadget",
        fg="#000000",
        bg="#d9d8ea",
        font=("Arial", 20, "bold"),
    )
    label.pack(pady=44)

    label = Label(
        add_window,
        text="Brand Name",
        font=(
            "Arial",
            16,
        ),
        fg="#232323",
    )
    brand_entry = Entry(
        add_window,
        font=(
            "Calibri light",
            14,
        ),
        relief="flat",
        fg="#064F21",
        width=10,
        bg="#FFFFFF",
    )
    label.pack(pady=25)
    brand_entry.pack()

    label = Label(
        add_window,
        text="Model Name",
        font=(
            "Arial",
            16,
        ),
        fg="#232323",
    )
    model_entry = Entry(
        add_window,
        font=(
            "Calibri light",
            14,
        ),
        relief="flat",
        fg="#064F21",
        width=10,
        bg="#FFFFFF",
    )
    label.pack(pady=25)
    model_entry.pack()

    label = Label(
        add_window,
        text="Enter Price",
        font=(
            "Arial",
            16,
        ),
        fg="#232323",
    )
    price_entry = Entry(
        add_window,
        font=(
            "Calibri light",
            14,
        ),
        relief="flat",
        fg="#064F21",
        width=10,
        bg="#FFFFFF",
    )
    label.pack(pady=25)
    price_entry.pack()

    label = Label(
        add_window,
        text="Category",
        font=(
            "Arial",
            16,
        ),
        fg="#232323",
    )
    options = ("phones", "computers", "laptops", "tablets")
    category_combo = ttk.Combobox(
        add_window,
        values=options,
        state="readonly",
        font=(
            "Arial",
            16,
        ),
        width=8,
    )

    label.pack(pady=25)
    category_combo.pack()

    label = Label(
        add_window,
        text="Quantity",
        font=(
            "Arial",
            16,
        ),
        fg="#232323",
    )
    quantity_entry = Entry(
        add_window,
        font=(
            "Calibri light",
            14,
        ),
        relief="flat",
        fg="#064F21",
        width=10,
        bg="#FFFFFF",
    )
    label.pack(pady=25)
    quantity_entry.pack()

    def submit_gadgets():
        brand = brand_entry.get()
        model = model_entry.get()
        price = price_entry.get()
        category = category_combo.get()
        quantity = quantity_entry.get()
        conn = sqlite3.connect("phones.db")
        c = conn.cursor()
        if (
            brand == ""
            or model == ""
            or price == ""
            or category == ""
            or quantity == ""
        ):
            Label(
                add_window,
                text="Enter the answers in all fields",
                fg="red",
                bg="#d9d8ea",
                font=("Arial", 15),
            ).pack(pady=6)
            return
        if not price.isdigit() or not quantity.isdigit():
            messagebox.showerror("Error", "*price and quantity must be integers")
            return
        price = int(price)
        quantity = int(quantity)
        if int(price) <= 0 or int(quantity) <= 0:
            messagebox.showerror("Error", "Values must be greater than 0 ❌")
            return

        c.execute(
            """INSERT INTO phones(brand,model,price,category,quantity)
                  VALUES(?,?,?,?,?)""",
            (brand, model, price, category, quantity),
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Successful", "Gadget added successfully ✅")
        add_window.destroy()

    button = Button(
        add_window,
        image=submit__button,
        fg="#000000",
        activebackground="#d9d8ea",
        bg="#d9d8ea",
        font=(
            "Arial",
            16,
        ),
        bd=0,
        command=submit_gadgets,
    )
    button.pack(pady=5)

    brand_entry.bind("<Return>", lambda event: model_entry.focus())
    model_entry.bind("<Return>", lambda event: price_entry.focus())
    price_entry.bind("<Return>", lambda event: category_combo.focus())
    category_combo.bind("<Return>", lambda event: quantity_entry.focus())
    quantity_entry.bind("<Return>", lambda event: submit_gadgets())

    button_exit = Button(
        add_window,
        text="EXIT",
        font=(
            "Arial",
            16,
        ),
        fg="#36FF80",
        bg="#000000",
        command=add_window.destroy,
    )
    button_exit.pack(pady=10)


def open_view_gadgets():
    view_window = Toplevel(window)
    view_window.transient(window)
    view_window.grab_set()
    view_window.geometry("1500x800+200+60")
    view_window.title = "Display Gadets"
    view_window.config(background="#1A1D20")
    top_frame = Frame(view_window)
    top_frame.config(background="#1A1D20", width=100, relief="groove")
    top_frame.pack(pady=30, padx=50)

    search_entry = Entry(
        top_frame, bg="#ffffff", fg="#000000", width=15, font=("arial", 12, "bold")
    )
    search_entry.pack(side=LEFT, pady=10, ipady=5, ipadx=5)

    table_frame = Frame(view_window, background="#1A1D20")
    table_frame.pack(fill=BOTH, expand=True)
    image = PhotoImage(file="C:\\python-practice\\table_bg.png")
    image_lab = Label(table_frame, image=image)
    image_lab.place(x=0, y=0, relwidth=1, relheight=1)
    table_frame.image = image

    down_frame = Frame(view_window, bg="#1A1D20")
    down_frame.configure(width=100)
    down_frame.pack(expand=True)

    exit_button = Button(
        down_frame,
        text="BACK",
        fg="#FF9100",
        bg="#1A1D20",
        font=("Arial", 10, "bold", "underline"),
        width=10,
        activeforeground="#FF9100",
        bd=0,
        highlightthickness=0,
        activebackground="#1A1D20",
        command=view_window.destroy,
    )
    exit_button.pack(pady=10, padx=15, side=LEFT)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "Purple.Treeview",
        font=("arial", 13, "bold"),
        padding=18,
        background="#00F5FF",
        foreground="#000000",
    )
    style.configure(
        "Treeview",
        rowheight=30,
        font=("arial", 12),
        foreground="#000000",
        background="#d9d8ea",
    )

    style.map(
        "Treeview",
        background=[("selected", "#232323")],
        foreground=[("selected", "white")],
    )

    scrollbar = Scrollbar(table_frame, orient=VERTICAL)

    tree = ttk.Treeview(
        table_frame,
        columns=("ITEM_CODE", "BRAND", "MODEL", "PRICE", "CATEGORY", "QUANTITY"),
        show="headings",
        yscrollcommand=scrollbar.set,
    )
    scrollbar.config(command=tree.yview)

    tree.column("ITEM_CODE", width=50)
    tree.column("BRAND", width=120, anchor="w")
    tree.column("MODEL", width=150, anchor="w")
    tree.column("PRICE", width=100, anchor="w")
    tree.column("CATEGORY", width=120, anchor="w")
    tree.column("QUANTITY", width=80, anchor="w")

    tree.heading("ITEM_CODE", text="ID")
    tree.heading("BRAND", text="BRAND")
    tree.heading("MODEL", text="MODEL")
    tree.heading("PRICE", text="PRICE")
    tree.heading("CATEGORY", text="CATEGORY")
    tree.heading("QUANTITY", text="QUANTITY")

    scrollbar.pack(fill=Y, side=RIGHT)

    tree.pack(fill=BOTH, expand=True)

    def load_gadgets(data):
        for row in tree.get_children():
            tree.delete(row)
        for phone in data:
            tree.insert(
                "",
                END,
                values=(phone[1], phone[2], phone[3], phone[4], phone[5], phone[6]),
            )

    conn = sqlite3.connect("phones.db")
    c = conn.cursor()
    c.execute("SELECT * FROM phones")
    phones = c.fetchall()
    conn.close()

    load_gadgets(phones)

    def refresh_table():
        conn = sqlite3.connect("phones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM phones")
        phones = c.fetchall()
        conn.close()
        load_gadgets(phones)
        view_window.after(100000, refresh_table)

    refresh_table()

    def delete__refresh():
        search_entry.delete(0, END)
        return refresh_table()

    delete_refresh = Button(
        top_frame,
        text="X",
        bg="#ffffff",
        fg="#000000",
        bd=0,
        activebackground="#ffffff",
        highlightthickness=0,
        font=("arial", 12, "bold"),
        command=delete__refresh,
    )
    delete_refresh.pack(side=LEFT, pady=10, ipady=3)

    def search_gadgets():
        search__term = search_entry.get()

        conn = sqlite3.connect("phones.db")
        c = conn.cursor()
        c.execute(
            """SELECT * FROM phones
                   WHERE LOWER(brand) LIKE LOWER(?) OR
                  LOWER(model) LIKE LOWER(?) OR
                  LOWER(category) LIKE LOWER(?)""",
            (
                "%" + search__term + "%",
                "%" + search__term + "%",
                "%" + search__term + "%",
            ),
        )
        results = c.fetchall()

        load_gadgets(results)
        conn.close()

    search_button = Button(
        top_frame,
        text="GO",
        bg="#1A1D20",
        font=("calibri", 15, "bold", "underline"),
        fg="#FF9100",
        highlightthickness=0,
        activebackground="#d9d8ea",
        bd=0,
        command=search_gadgets,
    )
    search_entry.bind("<Return>", lambda event: search_gadgets())
    search_button.pack(side=LEFT, padx=10, ipady=2)

    add_button = Button(
        down_frame,
        text="ADD GADGET",
        fg="#FF9100",
        bg="#1A1D20",
        font=("Arial", 10, "bold", "underline"),
        width=15,
        activeforeground="#FF9100",
        bd=0,
        highlightthickness=0,
        activebackground="#1A1D20",
        command=open_add_gadget,
    )
    add_button.pack(pady=20, padx=15, side=LEFT)

    def update_inventory():
        selected = tree.focus()
        values = tree.item(selected, "values")
        if not selected:
            messagebox.showerror("error", "please select gadget")
        else:
            update_win = Toplevel(view_window, bg="#d9d8ea")
            update_win.transient(window)
            update_win.grab_set()
            update_win.geometry("500x900+690+50")
            update_win.title("UPDATE GADGET")
            up_frame = Frame(update_win)
            up_frame.config(background="#d9d8ea")
            up_frame.pack(fill=X, expand=True)
            Label(
                up_frame,
                text=f"You are updating {values[1]}  {values[2]}",
                font=("Arial", 12, "bold"),
                fg="#000000",
                height=2,
                width=35,
                bg="#d9d8ea",
            ).pack()
            brand_frame = Frame(update_win, bg="#d9d8ea", height=30)
            brand_frame.pack(fill=X, expand=True)

            brand_label = Label(
                brand_frame,
                text=f"BRAND: ",
                font=("constantia", 13, "bold"),
                fg="#172A0D",
                width=18,
                bg="#d9d8ea",
            )
            brand_label.pack(pady=8, side=LEFT, padx=10)

            brand_ent = Entry(
                brand_frame, font=("Arial", 12), fg="#172A0D", width=18, bg="#FFF3F3"
            )
            brand_ent.insert(0, f"{values[1]}")
            brand_ent.pack(pady=15, side=LEFT, padx=10)

            model_frame = Frame(update_win, bg="#d9d8ea", height=30)
            model_frame.pack(fill=X, expand=True)

            model_label = Label(
                model_frame,
                text=f"MODEL: ",
                font=("constantia", 13, "bold"),
                fg="#172A0D",
                width=18,
                bg="#d9d8ea",
            )
            model_label.pack(pady=15, side=LEFT, padx=10)

            model_ent = Entry(
                model_frame, font=("Arial", 12), fg="#172A0D", width=18, bg="#FFF3F3"
            )
            model_ent.insert(0, f"{values[2]}")
            model_ent.pack(pady=15, side=LEFT, padx=10)

            price_frame = Frame(update_win, bg="#d9d8ea", height=30)
            price_frame.pack(fill=X, expand=True)

            price_label = Label(
                price_frame,
                text=f"PRICE: ",
                font=("constantia", 13, "bold"),
                fg="#172A0D",
                width=18,
                bg="#d9d8ea",
            )
            price_label.pack(pady=15, side=LEFT, padx=10)

            price_ent = Entry(
                price_frame, font=("Arial", 12), fg="#172A0D", width=18, bg="#FFF3F3"
            )
            price_ent.insert(0, f"{values[3]}")
            price_ent.pack(pady=15, side=LEFT, padx=10)

            quantity_frame = Frame(update_win, bg="#d9d8ea", height=30)
            quantity_frame.pack(fill=X, expand=True)

            quantity_label = Label(
                quantity_frame,
                text=f"QUANTITY: ",
                font=("constantia", 13, "bold"),
                fg="#172A0D",
                width=18,
                bg="#d9d8ea",
            )
            quantity_label.pack(pady=15, side=LEFT, padx=10)

            quantity_ent = Entry(
                quantity_frame, font=("Arial", 12), fg="#172A0D", width=18, bg="#FFF3F3"
            )
            quantity_ent.insert(0, f"{values[5]}")
            quantity_ent.pack(pady=15, side=LEFT, padx=10)

            category_frame = Frame(update_win, bg="#d9d8ea", height=30)
            category_frame.pack(fill=X, expand=True)

            category_label = Label(
                category_frame,
                text=f"CATEGORY: ",
                font=("constantia", 13, "bold"),
                fg="#172A0D",
                width=18,
                bg="#d9d8ea",
            )
            category_label.pack(pady=15, side=LEFT, padx=10)

            options = ("phones", "computers", "laptops", "tablets")
            category_combo = ttk.Combobox(
                category_frame,
                values=options,
                state="readonly",
                font=(
                    "Arial",
                    16,
                ),
                width=8,
            )
            category_combo.set(f"{values[4]}")
            category_combo.pack(pady=15, side=LEFT, padx=10)

            category_framee = Frame(update_win, bg="#ffffff", height=30)
            category_framee.pack(fill=X, expand=True)

            def save_button():
                brand = brand_ent.get()
                model = model_ent.get()
                price = price_ent.get()
                quantity = quantity_ent.get()
                category_ent = category_combo.get()
                if (
                    quantity == ""
                    or model == ""
                    or price == ""
                    or category_ent == ""
                    or quantity == ""
                    or brand == ""
                ):
                    messagebox.showerror("Error", "All fields must be filled!")
                    return
                if not price.isdigit() or not quantity.isdigit():
                    messagebox.showerror(
                        "Error", "*price and quantity must be integers"
                    )
                    return
                price = int(price)
                quantity = int(quantity)
                if price <= 0 or quantity <= 0:
                    messagebox.showerror("Error", "Values must be greater than 0 ❌")
                    return

                else:
                    confirm = messagebox.askyesno("update?", "Are you sure")
                    if confirm:
                        conn = sqlite3.connect("phones.db")
                        c = conn.cursor()
                        c.execute(
                            """UPDATE phones SET 
                              brand = ?,
                              model = ?,
                              price = ?,
                              quantity = ?,
                              category = ?
                              WHERE item_code = ?""",
                            (
                                brand,
                                model,
                                price,
                                quantity,
                                category_ent,
                                values[0],
                            ),
                        )
                        conn.commit()
                        conn = sqlite3.connect("phones.db")
                        c = conn.cursor()
                        c.execute("SELECT * FROM phones")
                        updated_list = c.fetchall()
                        load_gadgets(updated_list)
                        conn.close()
                        messagebox.showinfo(
                            "successfull", f"{values[0]} updated successfully"
                        )
                        update_win.destroy()

            sbutton = Button(
                category_framee,
                text="SAVE",
                fg="#033A1A",
                bg="#F3F3F3",
                font=(
                    "Arial",
                    10,
                ),
                width=10,
                activebackground="#5DFF05",
                command=save_button,
            )
            exit = Button(
                category_framee,
                text="BACK",
                fg="#521919",
                bg="#F8F8F8",
                font=(
                    "Arial",
                    10,
                ),
                width=10,
                activebackground="#FF0505",
                command=update_win.destroy,
            )
            exit.pack(pady=15, side=BOTTOM)
            sbutton.pack(pady=15)

    update_button = Button(
        down_frame,
        text="UPDATE GADGET",
        fg="#FF9100",
        bg="#1A1D20",
        font=("Arial", 10, "bold", "underline"),
        width=15,
        activeforeground="#FF9100",
        bd=0,
        highlightthickness=0,
        activebackground="#1A1D20",
        command=update_inventory,
    )

    update_button.pack(pady=20, padx=15, side=LEFT)

    def delete_gadget():
        selected = tree.focus()
        if not selected:
            messagebox.showerror("Error", "Select the row to delete!")
            return
        else:
            values = tree.item(selected, "values")
            item_id = values[0]

            confirm = messagebox.askyesno(
                "confirm", f"Are you sure to delete {values[1]}"
            )
            if confirm:
                conn = sqlite3.connect("phones.db")
                c = conn.cursor()
                c.execute("""DELETE FROM phones WHERE id = ?""", (item_id,))

                conn.commit()
                conn.close()
                tree.delete(selected)
                messagebox.showinfo(
                    "successfull", f"{values[1]} {values[2]} deleted successfully"
                )

    delete_button = Button(
        down_frame,
        text="DELETE",
        fg="#FF9100",
        bg="#1A1D20",
        font=("Arial", 10, "bold", "underline"),
        width=10,
        activeforeground="#FF9100",
        bd=0,
        highlightthickness=0,
        activebackground="#1A1D20",
        command=delete_gadget,
    )
    delete_button.pack(pady=20, padx=15, side=LEFT)


def place_sales():
    sale_window = Toplevel(window, bg="#d9d8ea")
    sale_window.geometry("1500x800+200+60")
    sale_window.title("Place a Sale")
    sale_window.transient(window)
    sale_window.grab_set()

    sale_window.grid_columnconfigure(0, weight=1)
    sale_window.grid_columnconfigure(1, weight=1)
    sale_window.grid_columnconfigure(2, weight=1)
    sale_top_frame = Frame(sale_window)
    sale_top_frame.config(bg="#d9d8ea")
    sale_top_frame.pack(pady=25, fill=X)

    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Good Morning!"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon!"
    elif 18 <= current_hour < 22:
        greeting = "Good Evening!"
    else:
        greeting = "Good Night!"

    welcome_label = Label(
        sale_top_frame,
        text=f"{greeting} Sales Personnel",
        bg="#565567",
        fg="#A2DE82",
        font=("constatia", 18, "bold"),
        width=89,
        height=5,
    )
    welcome_label.pack()

    sale_mid_frame = Frame(sale_window, bg="#565567")
    sale_mid_frame.pack(expand=True, side=TOP)

    class App:
        def __init__(self):
            self.values = None
            self.new_sale_window = None

        def new_sale(self):
            self.new_sale_window = Toplevel(sale_window, bg="#1A1D20")
            self.new_sale_window.transient(sale_window)
            self.new_sale_window.grab_set()
            self.new_sale_window.state("zoomed")

            self.new_sale_window.rowconfigure(0, weight=0)
            self.new_sale_window.rowconfigure(1, weight=0)
            self.new_sale_window.rowconfigure(2, weight=0)
            self.new_sale_window.rowconfigure(3, weight=0)
            self.new_sale_window.rowconfigure(4, weight=1)
            self.new_sale_window.columnconfigure(0, weight=1)
            self.new_sale_window.columnconfigure(1, weight=1)
            self.new_sale_window.columnconfigure(2, weight=1)

            logo_label = Label(
                self.new_sale_window,
                text="GADGET HUB",
                font=("arial", 13, "bold"),
                fg="#00F5FF",
                bg="#1A1D20",
                image=logo,
                compound="top",
                bd=0,
                highlightthickness=0,
                anchor="center",
            )
            logo_label.grid(row=0, column=1, pady=30, padx=10)

            canvas = Canvas(
                self.new_sale_window,
                bg="#1A1D20",
                bd=0,
                highlightthickness=0,
                height=10,
            )
            canvas.create_line(20, 0, 2000, 0, fill="#FF9100")
            canvas.grid(row=2, column=0, columnspan=3, sticky="ew")

            description_frame2 = Frame(
                self.new_sale_window, bd=0, highlightthickness=0, bg="#1A1D20", width=30
            )
            description_frame2.grid(row=3, column=2, padx=(20, 0), pady=10)

            description_image = Label(
                self.new_sale_window, image=instructionspng, bg="#1A1D20", bd=0
            )
            description_image.grid(row=3, rowspan=2, column=0, sticky="nsew")

            text_item = Text(
                description_frame2,
                bg="#1A1D20",
                width=50,
                wrap=WORD,
                height=20,
                bd=0,
                highlightthickness=0,
                fg="#FF9100",
                font=("arial", 11),
            )
            text_item.pack(padx=(0, 20))
            descriptions = """This product comes with premium plans i.e\n  1. Basic setup. click here.\n  2. Standard setup. click here.\n  3. Super setup. click here."""
            text_item.insert("1.0", descriptions)
            text_item.config(state="disabled")

            self.customer_frame = Frame(self.new_sale_window, bg="#1A1D20")
            self.customer_frame.grid(row=3, column=1, pady=10, sticky="n")
            Label(
                self.customer_frame,
                text="Customer",
                font=("arial", 13, "bold"),
                fg="#FF9100",
                bg="#1A1D20",
            ).pack(pady=10)
            Label(
                self.customer_frame,
                text="To complete the sale operation, click \nbelow link to add customer",
                font=("Varela Round", 11),
                fg="#DDDCDC",
                bg="#1A1D20",
            ).pack()
            self.customer_entry = Entry(
                self.customer_frame, width=20, bg="#000407", state="readonly"
            )
            self.customer_entry.pack(pady=10)

            Button(
                self.customer_frame,
                text="click to open customers",
                font=("Varela Round", 11, "underline"),
                fg="#00F5FF",
                bg="#1A1D20",
                activebackground="#1A1D20",
                activeforeground="#00F5FF",
                bd=0,
                highlightthickness=0,
                command=self.customer_selection,
            ).pack(pady=5)

            self.item_frame = Frame(self.new_sale_window, bd=2, bg="#1A1D20")
            self.item_frame.grid(row=4, column=1, pady=10, sticky="nsew")
            Label(
                self.item_frame,
                text="Item",
                font=("arial", 13, "bold"),
                fg="#FF9100",
                bg="#1A1D20",
            ).pack(pady=10)
            Label(
                self.item_frame,
                text="click the ➕ below to select \nitem and complete operation",
                font=("Varela Round", 11),
                fg="#DDDCDC",
                bg="#1A1D20",
            ).pack()
            self.item_entry = Entry(
                self.item_frame, bg="#000000", fg="#000000", width=20, state="readonly"
            )
            self.item_entry.pack(pady=(10, 0))
            Button(
                self.item_frame,
                text="➕",
                font=("arial", 13),
                bg="#1A1D20",
                fg="#FF9100",
                bd=2,
                command=self.item_selection_win,
            ).pack(pady=5)
            quantity_frame = Frame(
                self.item_frame,
                bg="#1A1D20",
                bd=2,
                highlightthickness=2,
                highlightcolor="#FF9100",
                highlightbackground="#FF9100",
            )
            quantity_frame.pack(pady=10)
            self.item_quantity = Entry(quantity_frame, width=5, font=("arial", 11))
            self.item_quantity.pack(pady=5, ipadx=5, side="right")
            Label(
                quantity_frame,
                text="Qty:",
                fg="#FF9100",
                bg="#1A1D20",
                font=("arial", 11),
            ).pack(padx=5, side="right")
            # self.item_entry.bind("<FocusIn>",lambda event:self.item_selection_win())
            action_frame = Frame(self.item_frame, bg="#1A1D20")
            action_frame.pack(pady=15, expand=True)
            Label(
                action_frame,
                text="Actions",
                fg="#FF9100",
                bg="#1A1D20",
                font=("arial", 13, "bold"),
            ).pack(pady=10)
            add_button = Button(
                action_frame,
                text="Add",
                bg="#1A1D20",
                activebackground="#1A1D20",
                activeforeground="#FF9100",
                fg="#00F5FF",
                bd=0,
                highlightthickness=0,
                font=("arial", 11, "bold", "underline"),
                command=self.receipt_refresh_item,
            )
            add_button.pack(pady=10, padx=20, side="left")
            cancel_button = Button(
                action_frame,
                text="Cancel",
                bg="#1A1D20",
                activebackground="#1A1D20",
                activeforeground="#FF9100",
                fg="#FF5E00",
                bd=0,
                highlightthickness=0,
                font=("arial", 11, "bold", "underline"),
                command=self.cancel_sale,
            )
            cancel_button.pack(pady=10, padx=20, side="right")

            self.receipt_frame = Frame(
                self.new_sale_window,
                bg="#FAFCFF",
                bd=2,
                relief="solid",
                highlightcolor="#FF9100",
                highlightbackground="#FF9100",
            )
            self.receipt_frame.grid(
                row=4, rowspan=2, column=2, padx=100, pady=(0, 100), sticky="nsew"
            )
            self.receipt_frame.grid_propagate(False)

            self.receipt_frame.rowconfigure(0, weight=0, minsize=10)
            self.receipt_frame.rowconfigure(1, weight=0, minsize=10)
            self.receipt_frame.rowconfigure(2, weight=0, minsize=10)
            self.receipt_frame.rowconfigure(3, weight=1)
            self.receipt_frame.rowconfigure(4, weight=0)
            self.receipt_frame.rowconfigure(5, weight=0)
            self.receipt_frame.columnconfigure(0, weight=1)
            self.receipt_frame.columnconfigure(1, weight=1)
            self.receipt_frame.columnconfigure(2, weight=0)

            Label(
                self.receipt_frame,
                text="GADGET HUB",
                anchor="w",
                font=("Courier New", 13, "bold"),
            ).grid(row=0, column=0, pady=5, sticky="w")
            #  if self.customer_entry.get() == "":
            #      name = "Customer Name"
            #  else:
            #      name = self.customer_entry.get()

            self.customer_name = Label(
                self.receipt_frame,
                text="Customer:",
                anchor="w",
                font=("Courier New", 10, "bold"),
            )
            self.customer_name.grid(row=1, column=0, pady=5, sticky="w")

            self.receipt_date_lab = Label(
                self.receipt_frame,
                text=f'Date: {datetime.now().strftime("%d.%m.%Y, %H:%M:%S")}',
                font=("Courier New", 10, "bold"),
            )
            self.receipt_date_lab.grid(row=2, column=0, pady=5, sticky="w")

            #  receipt_body_frame = Frame(self.receipt_frame,bg="#FAFCFF")
            #  receipt_body_frame.pack(expand=True,fill="both")
            style = ttk.Style()
            style.theme_use("clam")
            style.configure(
                "Blue.Treeview",
                font=("Courier New", 10),
                rowheight=20,
                foreground="#000000",
                background="#ffffff",
            )

            style.map(
                "Blue.Treeview",
                background=[("selected", "#DDD9D9")],
                foreground=[("selected", "#000000")],
            )
            scrollbar = Scrollbar(self.receipt_frame, orient="vertical")
            self.receipt_tree = ttk.Treeview(
                self.receipt_frame,
                columns=("I.ID", "ITEM", "Qty", "VAT%", "Total", "PRICE"),
                show="headings",
                style="Blue.Treeview",
                yscrollcommand=scrollbar.set,
            )
            scrollbar.configure(command=self.receipt_tree.yview)

            self.receipt_tree["displaycolumns"] = ("ITEM", "Qty", "PRICE", "Total")

            self.receipt_tree.column("ITEM", width=120)
            self.receipt_tree.column("Qty", width=20)
            self.receipt_tree.column("PRICE", width=20)
            self.receipt_tree.column("Total", width=20)

            self.receipt_tree.heading("ITEM", text="ITEM")
            self.receipt_tree.heading("Qty", text="Qty")
            self.receipt_tree.heading("Total", text="Total")
            self.receipt_tree.heading("PRICE", text="PRICE")

            scrollbar.grid(row=3, column=2, rowspan=2, sticky="ns")
            self.receipt_tree.grid(row=3, column=0, columnspan=2, sticky="nsew")

            self.grand_total_lab = Label(
                self.receipt_frame,
                text="Grand Total:",
                font=("Courier New", 10, "bold"),
                bg="#ffffff",
                fg="#000000",
            )
            self.grand_total_lab.grid(row=5, column=1, columnspan=2, sticky="e")

            self.print_button = Button(
                self.receipt_frame,
                text="PRINT",
                fg="#030303",
                bg="#B8C6C7",
                state="disabled",
                width=10,
                command=self.print_receipt,
            )
            self.print_button.grid(row=5, column=0, sticky="w")

        def update_grand_total(self):
            grand_total = 0.00
            for child in self.receipt_tree.get_children():
                child_values = self.receipt_tree.item(child, "values")
                if child_values:
                    total_str = (
                        child_values[4].replace("Kes", "").replace(",", "").strip()
                    )
                    grand_total += float(total_str)
            self.grand_total_lab.config(text=f"Grand Total: Kes {grand_total:,.2f}")

        def receipt_refresh_item(self):
            item_name = self.item_entry.get().strip()
            quantity = self.item_quantity.get().strip()
            if not item_name or not quantity:
                messagebox.showerror("Error", "please, select item and quantity")
                return
            if not quantity.isdigit() or int(quantity) <= 0:
                messagebox.showerror("Error", "Quantity must be a positive digit!")
                return
            model = self.values[1]
            conn = sqlite3.connect("phones.db")
            c = conn.cursor()
            c.execute(
                """SELECT * FROM phones WHERE LOWER(model) = LOWER(?)""", (model,)
            )
            result = c.fetchone()
            conn.close()
            if int(quantity) > int(result[6]):
                messagebox.showerror("Low Stock", "SELECT A LOWER QUANTITY")
                return
            try:
                print(result[4])
                if not result:
                    messagebox.showerror("Error", "no matching item")
                    return
                vat = 10
                item_id = result[0]
                price = result[4]
                total = int(quantity) * int(price)  #
                print(total)
                self.receipt_tree.insert(
                    "",
                    "end",
                    values=(
                        item_id,
                        item_name,
                        quantity,
                        f"{vat}",
                        f"{total:,.2f}",
                        price,
                    ),
                )
                self.print_button.configure(state="normal", bg="#00F5FF")
                self.update_grand_total()

                self.item_entry.config(state="normal")
                self.item_entry.delete(0, "end")
                self.item_entry.config(state="readonly")
                self.item_quantity.delete(0, "end")
                print("receipt_refresh_item(self): is good")
            except Exception as e:
                print(e)
                messagebox.showinfo("Error", "Something went wrong!")

        def receipt_refresh_customer(self):
            current_customer_val = self.customer_entry.get().strip()
            self.display_name = (
                current_customer_val if current_customer_val else "Customer:"
            )
            self.customer_name.configure(text=f"Customer: {self.display_name}")

        def item_selection_win(self):
            self.item_selection = Toplevel(self.new_sale_window, bg="#1A1D20", bd=2)
            self.item_selection.geometry("1000x500+450+400")

            top_frame = Frame(self.item_selection, bg="#1A1D20", bd=2)
            top_frame.pack(fill=X, side="top")
            Label(top_frame, image=logo, bd=0, highlightthickness=0).pack(pady=5)
            search_frame = Frame(top_frame, bg="#1A1D20", bd=2, relief="solid")
            search_frame.pack(expand=True, pady=5)
            self.search_entry_item = Entry(
                search_frame, width=20, font=("helvetica", 11, "bold")
            )
            self.search_entry_item.pack(pady=10, side="left")
            self.search_entry_item.focus_set()

            def on__focus_out():
                new_focus = self.item_selection.focus_get()
                if new_focus is None or not str(new_focus).startswith(
                    str(self.item_selection)
                ):
                    self.item_selection.destroy()

            self.item_selection.bind("<FocusOut>", lambda event: on__focus_out())

            body_frame = Frame(self.item_selection, bg="#1A1D20", bd=2, relief="solid")
            body_frame.pack(fill="both", expand=True, side="top")
            scrollbar = Scrollbar(body_frame, orient="vertical")
            scrollbar.pack(side="right", fill="y")
            style = ttk.Style()
            style.theme_use("clam")
            style.configure(
                "Yellow.Treeview",
                foreground="#1A1D20",
                background="#FF9100",
                font=("arial", 13, "bold"),
            )
            style.map(
                "Treeview",
                background=[("selected", "#00F5FF")],
                foreground=[("selected", "#1A1D20")],
            )
            style.configure(
                "Treeview",
                rowheight=30,
                font=("arial", 12),
                background="#1A1D20",
                border=2,
                foreground="#FF9100",
            )
            self.tree_ = ttk.Treeview(
                body_frame,
                columns=("BRAND", "MODEL", "PRICE", "QUANTITY"),
                show="headings",
                yscrollcommand=scrollbar.set,
            )
            scrollbar.config(command=self.tree_.yview)

            self.tree_.column("BRAND", width=50)
            self.tree_.column("MODEL", width=50)
            self.tree_.column("PRICE", width=50)
            self.tree_.column("QUANTITY", width=50)

            self.tree_.heading("BRAND", text="BRAND")
            self.tree_.heading("MODEL", text="MODEL")
            self.tree_.heading("PRICE", text="PRICE")
            self.tree_.heading("QUANTITY", text="QUANTITY")

            self.tree_.pack(fill="both", expand=True)

            def load_customers(data):
                for row in self.tree_.get_children():
                    self.tree_.delete(row)
                for phone in data:
                    self.tree_.insert(
                        "",
                        END,
                        values=(phone[2], phone[3], f"KES {phone[4]:,.2f}", phone[6]),
                    )

            conn = sqlite3.connect("phones.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM phones")
            phones = cursor.fetchall()
            conn.close()
            load_customers(phones)

            def search_customers():
                searched_customer = self.search_entry_item.get()
                conn = sqlite3.connect("phones.db")
                cursor = conn.cursor()
                cursor.execute(
                    """SELECT * FROM phones WHERE LOWER(brand) LIKE LOWER(?) OR
                                LOWER(model) LIKE LOWER(?) OR LOWER(id) LIKE LOWER(?)""",
                    (
                        "%" + searched_customer + "%",
                        "%" + searched_customer + "%",
                        "%" + searched_customer + "%",
                    ),
                )
                customers = cursor.fetchall()
                conn.close()
                load_customers(customers)

            self.search_entry_item.bind("<Return>", lambda event: search_customers())
            self.tree_.bind("<Double-1>", lambda event: self.after_selection_())

        def after_selection_(self):
            selected_i = self.tree_.focus()
            if not selected_i:
                return
            if self.customer_entry.get() == "":
                messagebox.showerror("Error", "Select Customer!")
            else:
                self.values = self.tree_.item(selected_i, "values")
                self.item_entry.configure(state="normal")
                self.item_entry.delete(0, END)
                self.item_entry.insert(0, f"{self.values[0]} {self.values[1]}")
                self.item_entry.configure(
                    state="readonly", font=("arial", 13), bg="#ACB3B9", width=20
                )
                self.item_selection.destroy()
                self.item_selection = None

        def customer_selection(self):
            self.selection_window = Toplevel(self.new_sale_window, bg="#1A1D20", bd=2)
            self.selection_window.geometry("1000x500+450+200")

            top_frame = Frame(self.selection_window, bg="#1A1D20", bd=2)
            top_frame.pack(fill=X, side="top")
            Label(top_frame, image=logo, bd=0, highlightthickness=0).pack(pady=5)
            search_frame = Frame(top_frame, bg="#1A1D20", bd=2, relief="solid")
            search_frame.pack(expand=True, pady=5)
            search_entry = Entry(search_frame, width=20, font=("helvetica", 11, "bold"))
            search_entry.pack(pady=10, side="left")
            search_entry.focus_set()

            def on_focus_out():
                new_focus = self.selection_window.focus_get()
                if new_focus is None or not str(new_focus).startswith(
                    str(self.selection_window)
                ):
                    self.selection_window.destroy()

            self.selection_window.bind("<FocusOut>", lambda event: on_focus_out())

            body_frame = Frame(
                self.selection_window, bg="#1A1D20", bd=2, relief="solid"
            )
            body_frame.pack(fill="both", expand=True, side="top")
            scrollbar = Scrollbar(body_frame, orient="vertical")
            scrollbar.pack(side="right", fill="y")
            style = ttk.Style()
            style.theme_use("clam")
            style.configure(
                "Grey.Treeview",
                foreground="#1A1D20",
                background="#00F5FF",
                font=("arial", 13, "bold"),
            )
            style.map(
                "Treeview",
                background=[("selected", "#FF9100")],
                foreground=[("selected", "#1A1D20")],
            )
            style.configure(
                "Treeview",
                rowheight=30,
                font=("arial", 12),
                background="#1A1D20",
                border=2,
                foreground="#00F5FF",
            )
            self.tree = ttk.Treeview(
                body_frame,
                columns=("NAME", "MOBILE", "CREDIT", "BALANCE"),
                show="headings",
                yscrollcommand=scrollbar.set,
            )
            scrollbar.config(command=self.tree.yview)

            self.tree.column("NAME", width=50)
            self.tree.column("MOBILE", width=50)
            self.tree.column("BALANCE", width=50)
            self.tree.column("CREDIT", width=50)

            self.tree.heading("NAME", text="NAME")
            self.tree.heading("MOBILE", text="MOBILE")
            self.tree.heading("BALANCE", text="BALANCE")
            self.tree.heading("CREDIT", text="CREDIT")

            self.tree.pack(fill="both", expand=True)

            def load_customers(data):
                for row in self.tree.get_children():
                    self.tree.delete(row)
                for customer in data:
                    self.tree.insert(
                        "", END, values=(customer[1], customer[3], "0.00", "0.00")
                    )

            conn = sqlite3.connect("phones.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers")
            customers = cursor.fetchall()
            conn.close()
            load_customers(customers)

            def search_customers():
                searched_customer = search_entry.get()
                conn = sqlite3.connect("phones.db")
                cursor = conn.cursor()
                cursor.execute(
                    """SELECT * FROM customers WHERE LOWER(name) LIKE LOWER(?) OR
                                LOWER(mobile) LIKE LOWER(?) OR LOWER(id) LIKE LOWER(?)""",
                    (
                        "%" + searched_customer + "%",
                        "%" + searched_customer + "%",
                        "%" + searched_customer + "%",
                    ),
                )
                customers = cursor.fetchall()
                conn.close()
                load_customers(customers)

            Button(
                search_frame,
                text="ENTER",
                font=("arial", 12, "underline"),
                bg="#1A1D20",
                fg="#FF9100",
                bd=0,
                highlightthickness=0,
                command=search_customers,
            ).pack(side="left")
            search_entry.bind("<Return>", lambda event: search_customers())
            Button(
                search_frame,
                text="SUBMIT",
                font=("arial", 11, "underline"),
                fg="#00F5FF",
                bg="#1A1D20",
                bd=0,
                highlightthickness=0,
                command=self.after_selection,
            ).pack(side="bottom")
            self.tree.bind("<Double-1>", lambda event: self.after_selection())

        def after_selection(self):
            selected = self.tree.focus()
            if not selected:
                return

            values = self.tree.item(selected, "values")
            self.customer_entry.configure(state="normal")
            self.customer_entry.delete(0, END)
            self.customer_entry.insert(0, values[1])
            self.customer_entry.configure(state="readonly", font=("arial", 13))
            self.receipt_refresh_customer()
            self.selection_window.destroy()
            self.selection_window = None

        def cancel_sale(self):
            confirm = messagebox.askyesno(
                "Confirm cancellation", "Are you sure to Reset\nOrder?"
            )
            if confirm:
                self.customer_entry.configure(state="normal")
                self.item_entry.configure(state="normal")
                self.customer_entry.delete(0, END)
                self.item_entry.delete(0, END)
                self.item_quantity.delete(0, END)
                self.customer_entry.configure(state="readonly")
                self.item_entry.configure(state="readonly")
                self.print_button.configure(state="disabled", bg="#B8C6C7")
                self.grand_total_lab.config(text="Grand Total:")
                self.customer_name.configure(text=f"Customer:")
                for row in self.receipt_tree.get_children():
                    self.receipt_tree.delete(row)

        def print_receipt(self):
            confirm = messagebox.askyesno("PRINT RECEIPT", "PRINT RECEIPT?")
            if confirm:
                try:
                    grand_total = float(
                        self.grand_total_lab.cget("text")
                        .replace("Grand Total:", "")
                        .replace("Kes", "")
                        .replace(",", "")
                        .strip()
                    )
                    date = f"{self.receipt_date_lab.cget("text")}"
                    customer_name = self.display_name
                    vat = 10
                    customer_name = customer_name
                    conn = sqlite3.connect("phones.db")
                    cursor = conn.cursor()
                    cursor.execute(
                        """SELECT * FROM customers WHERE LOWER(name) = LOWER(?)""",
                        (customer_name,),
                    )
                    customers = cursor.fetchone()
                    conn.close()
                    if not customers:
                        messagebox.showerror("DB ERROR", "Customers DB Error")
                        return
                    location = customers[4]

                    conn = sqlite3.connect("phones.db")
                    cursor = conn.cursor()
                    cursor.execute(
                        """INSERT INTO sales(customer,location,date,vat,grand_total)
                                    VALUES(?,?,?,?,?)""",
                        (customer_name, location, date, vat, grand_total),
                    )
                    sale_id = cursor.lastrowid

                    for child in self.receipt_tree.get_children():
                        self.items = self.receipt_tree.item(child, "values")
                        item_id = self.items[0]
                        item_name = self.items[1]
                        quantity = self.items[2]
                        price = self.items[5]
                        total = self.items[4]

                        cursor.execute(
                            """SELECT quantity FROM phones WHERE id=(?)""", (item_id,)
                        )
                        real_quantity = cursor.fetchone()
                        new_quantity = int(real_quantity[0]) - int(quantity)
                        cursor.execute(
                            """UPDATE phones SET quantity =(?) WHERE id = (?)""",
                            (new_quantity, item_id),
                        )
                        conn.commit()
                        print("stock deducted")

                        cursor.execute(
                            """INSERT INTO sale_items(sale_id,item_id,item_name,quantity,unit_price,total_price)
                                        VALUES(?,?,?,?,?,?)""",
                            (sale_id, item_id, item_name, quantity, price, total),
                        )
                        print("sale recorded")

                    conn.commit()
                    cursor.execute("SELECT * FROM sale_items")
                    sales = cursor.fetchall()
                    print(sales)
                    conn.close()

                    confirm = messagebox.askyesno("CONTINUE?", f"PRINT SL000{sale_id}?")
                    if confirm:
                        receipt_text = "       GADGET HUB       \n"
                        receipt_text += f" SL000{sale_id}       \n"
                        receipt_text += f" {self.display_name} \n"
                        receipt_text += f" {location}       \n"
                        receipt_text += f" {self.receipt_date_lab.cget("text")} \n"
                        receipt_text += "=" * 36 + "\n"

                        receipt_text += f"{'ITEM':<20} {'QTY':<3} {'TOTAL':>11}\n"
                        receipt_text += "-" * 30 + "\n"
                        for child in self.receipt_tree.get_children():
                            self.val = self.receipt_tree.item(child, "values")
                            if self.val:
                                item_name = self.val[1][
                                    :20
                                ]  # Truncate long names to 14 chars so it doesn't break alignment
                                qty = self.val[2][:3]
                                to_tal = self.val[4][:11]
                                receipt_text += (
                                    f"{item_name:<20} {qty:<3} {to_tal:>11}\n"
                                )

                        receipt_text += "-" * 36 + "\n"
                        grand_total_str = self.grand_total_lab.cget("text")
                        receipt_text += f"{grand_total_str:>30}\n"  # Push to the right
                        receipt_text += "=" * 36 + "\n"
                        receipt_text += "    Thank you for shopping!   \n"
                        receipt_text += "\n\n\n"

                        filename = "temp_receipt.txt"
                        with open(filename, "w") as f:
                            f.write(receipt_text)

                        # 5. Send to OS Printer
                        #         try:
                        #             if sys.platform == "win32":
                        # # Windows: Uses the default text editor to print silently
                        #                 os.startfile(filename, "print")
                        #             else:
                        #                 os.system(f"lpr {filename}")
                        #         except Exception as e:
                        #             messagebox.showerror("Print Error", f"Could not print: {e}")
                        print("place it")
                        print("it'ill work here")

                except Exception as e:
                    messagebox.showerror("Print Error", f"Could not print:\n {e}")
                    print(e)

    app = App()
    new_sale_bt = Button(
        sale_mid_frame,
        text="➕",
        font=("arial", 14, "bold"),
        fg="#A2DE82",
        bg="black",
        width=50,
        command=app.new_sale,
    )
    new_sale_bt.grid(row=0, column=0, sticky=N, padx=30, pady=30)

    class History:
        def __init__(self):
            self.new_history_win = None

        def history_window(self):
            self.new_history_win = Toplevel(sale_window, bg="#1A1D20")
            self.new_history_win.overrideredirect(True)
            self.new_history_win.geometry("1500x800+200+60")

            def start_move(event):
                self.new_history_win.x = event.x
                self.new_history_win.y = event.y

            def do_move(event):
                x = self.new_history_win.winfo_x() + (event.x - self.new_history_win.x)
                y = self.new_history_win.winfo_y() + (event.y - self.new_history_win.y)
                self.new_history_win.geometry(f"+{x}+{y}")

            title_bar = Frame(self.new_history_win, bd=2, bg="#1A1D20", height=32)
            title_bar.pack(fill=X)
            title_bar.bind("<Button-1>", start_move)
            title_bar.bind("<B1-Motion>", do_move)

            title_label = Label(
                title_bar,
                text="History Window",
                bg="#1A1D20",
                fg="#FF9100",
                font=("Segou UI", 10),
            )
            title_label.pack(side=LEFT, pady=12)
            title_label.bind("<Button-1>", start_move)
            title_label.bind("<B1-Motion>", do_move)

            close_button = Button(
                title_bar,
                text="✕",
                bg="#1A1D20",
                fg="white",
                bd=0,
                font=("Segoe UI", 11),
                activebackground="#c42b1c",
                activeforeground="white",
                command=self.new_history_win.destroy,
            )
            close_button.pack(side=RIGHT, padx=8)

            content = Frame(self.new_history_win, bg="#1A1D20")
            content.pack(fill=BOTH, expand=True)

            control_frame = Frame(content, bg="#1A1D20")
            control_frame.pack(fill=X)

            search_button = Button(
                content, text="🔍", bg="#1A1D20", fg="#FF9100", bd=0, font=("arial", 14)
            )
            search_button.pack(padx=30)

    sale_bottom_frame = Frame(sale_window, bg="#565567", width=89, height=10)
    sale_bottom_frame.pack(pady=0, fill=X)

    cancel_bt = Button(
        sale_bottom_frame,
        text="Cancel",
        font=("calibri", 14),
        fg="#A2DE82",
        bg="#000000",
        height=0,
        width=10,
        command=sale_window.destroy,
    )
    cancel_bt.pack(pady=30)

    def customers_():

        customer_win = Toplevel(sale_window, bg="#1A1D20")
        customer_win.transient(sale_window)
        customer_win.grab_set()
        customer_win.state("zoomed")
        customer_win.lift()
        customer_win.focus_force()
        customer_win.geometry("1500x800+200+60")
        customer_win.title = "MANAGE CUSTOMERS"

        topframe = Frame(customer_win, bg="#1A1D20", bd=2, height=100)
        topframe.pack(fill=X, pady=0, side=TOP)

        title_frame = Frame(topframe, bg="#1A1D20")
        title_frame.pack(pady=20, expand=True)

        New_customer_frame = Frame(topframe, bg="#1A1D20")
        New_customer_frame.pack(pady=20, expand=True)

        Label(
            title_frame,
            image=logo,
            fg="#DDDCDC",
            bg="#1A1D20",
        ).pack(pady=10)
        Label(
            title_frame,
            text="Manage Customer by Action",
            font=("ARIAL", 16, "bold"),
            fg="#DDDCDC",
            bg="#1A1D20",
            width=50,
        ).pack(pady=5)

        main_frame = Frame(customer_win, bg="#1A1D20")
        main_frame.pack(expand=True, fill="both", side=TOP, pady=0)

        bottom_frame = Frame(customer_win, bg="#1A1D20")
        bottom_frame.pack(pady=50)
        canvas = Canvas(main_frame, bg="#9e9eab", borderwidth=0, highlightthickness=0)
        scrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)

        scrollable_frame = Frame(canvas, bg="#9e9eab")

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas_window = canvas.create_window(
            (0, 0), window=scrollable_frame, anchor="nw"
        )

        canvas.bind(
            "<Configure>", lambda e: canvas.itemconfig(canvas_window, width=e.width)
        )

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        customer_win.bind_all("<MouseWheel>", on_mousewheel)

        search_frame = Frame(topframe, bg="#1A1D20")
        search_frame.pack(expand=True)

        search_entry = Entry(
            search_frame,
            bg="#FFFFFF",
            width=20,
            font=("calibri", 14, "bold"),
            bd=0,
            highlightthickness=0,
        )
        search_entry.pack(side=LEFT, pady=10, ipadx=4, ipady=9)

        def new_customer_btn_cmd():
            add_customer = Toplevel(customer_win)
            add_customer.transient(customer_win)
            add_customer.grab_set()
            add_customer.geometry("500x810+690+50")
            add_customer.config(background="#d9d8ea")
            add_customer.title("ADD CUSTOMER")

            customer_name = Label(
                add_customer,
                text=f"FULL NAMES: ",
                font=("constantia", 13, "bold"),
                fg="#C0FF9E",
                width=18,
                bg="#000000",
            )
            customer_name.pack(pady=20)

            name_entry = Entry(
                add_customer, font=("Arial", 12), fg="#172A0D", width=18, bg="#FFF3F3"
            )

            name_entry.pack(pady=20)

            location_label = Label(
                add_customer,
                text=f"LOCATION: ",
                font=("constantia", 13, "bold"),
                fg="#C0FF9E",
                width=18,
                bg="#000000",
            )
            location_label.pack(pady=20)

            location_ent = Entry(
                add_customer, font=("Arial", 12), fg="#172A0D", width=18, bg="#FFF3F3"
            )
            location_ent.pack(pady=20)

            id_label = Label(
                add_customer,
                text=f"NATIONAL ID NO: ",
                font=("constantia", 13, "bold"),
                fg="#C0FF9E",
                width=18,
                bg="#000000",
            )
            id_label.pack(pady=20)

            id_ent = Entry(
                add_customer, font=("Arial", 12), fg="#172A0D", width=18, bg="#FFF3F3"
            )
            id_ent.pack(pady=20)

            mobile_label = Label(
                add_customer,
                text=f"MOBILE NUMBER: ",
                font=("constantia", 13, "bold"),
                fg="#C0FF9E",
                width=18,
                bg="#000000",
            )
            mobile_label.pack(pady=20)

            mobile_ent = Entry(
                add_customer, font=("Arial", 12), fg="#172A0D", width=18, bg="#FFF3F3"
            )
            mobile_ent.pack(pady=20)

            status_label = Label(
                add_customer,
                text=f"CUSTOMER STATUS: ",
                font=("constantia", 13, "bold"),
                fg="#C0FF9E",
                width=18,
                bg="#000000",
            )
            status_label.pack(pady=20)

            options = ("Active", "Inactive", "Busy", "Closed")
            status_combo = ttk.Combobox(
                add_customer,
                values=options,
                state="readonly",
                font=(
                    "Arial",
                    16,
                ),
                width=8,
            )
            status_combo.pack(pady=20)

            exit_frame = Frame(add_customer, bg="#000000")
            exit_frame.pack(fill=X, side=BOTTOM, expand=True)

            Button(
                exit_frame,
                text="CLOSE",
                bg="#C0FF9E",
                fg="#000000",
                font=("calibri", 14, "bold"),
                command=add_customer.destroy,
            ).pack(pady=10, side=BOTTOM)

            conn = sqlite3.connect("customers.db")
            c = conn.cursor()

            def submit_customer():
                id_number = id_ent.get()
                location = location_ent.get()
                name = name_entry.get()
                mobile = mobile_ent.get()
                status = status_combo.get()

                if (
                    status == ""
                    or mobile == ""
                    or name == ""
                    or location == ""
                    or id_number == ""
                ):
                    messagebox.showerror("Error!", "Fill all fields!")
                    return
                if not mobile.isdigit() or not id_number.isdigit():
                    messagebox.showerror("Error!", "ID and MOBILE must be digits!")
                    return
                else:
                    confirm = messagebox.askyesno("Proceed?", "Are you sure to submit?")

                    if confirm:
                        conn = sqlite3.connect("phones.db")
                        c = conn.cursor()

                        c.execute(
                            """INSERT INTO 
                          customers(id_number,name,location,mobile,status)
                          VALUES(?,?,?,?,?)""",
                            (id_number, name, location, mobile, status),
                        )
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success!", f"{name} saved!")
                        add_customer.destroy()

            id_ent.bind("<Return>", lambda event: mobile_ent.focus())
            location_ent.bind("<Return>", lambda event: id_ent.focus())
            name_entry.bind("<Return>", lambda event: location_ent.focus())
            mobile_ent.bind("<Return>", lambda event: status_combo.focus())
            status_combo.bind("<Return>", lambda event: submit_customer())

            Button(
                exit_frame,
                image=submit__button,
                bg="#000000",
                fg="#000000",
                font=("calibri", 14, "bold"),
                bd=0,
                activebackground="#000000",
                command=submit_customer,
            ).pack(pady=10, side=TOP)

        Label(
            New_customer_frame,
            text="To add a new customer",
            font=("calibri", 14),
            bg="#1A1D20",
            fg="#FF9100",
        ).pack(pady=5, side=LEFT)
        new_customer_btn = Button(
            New_customer_frame,
            text="click here",
            bg="#1A1D20",
            fg="#00F5FF",
            bd=0,
            activeforeground="#00F5FF",
            activebackground="#1A1D20",
            highlightthickness=0,
            font=("calibri", 14, "underline"),
            command=new_customer_btn_cmd,
        )
        new_customer_btn.pack(pady=5, side=LEFT)

        def display_customers(customers):
            for widget in scrollable_frame.winfo_children():
                widget.destroy()

            for i, customer in enumerate(customers, start=1):

                status = customer[6]

                if status == "Active":
                    bg = "#ABF584"
                elif status == "Closed":
                    bg = "#F87069"
                elif status == "Busy":
                    bg = "#F8F873"
                else:
                    bg = "#F0F0E2"

                if i % 2 == 0:
                    row_colour = "#5A6B70"
                else:
                    row_colour = "#29413F"

                row_frame = Frame(scrollable_frame, bg=row_colour, bd=2)
                row_frame.pack(fill="x", padx=10, pady=5)

                row_frame.grid_columnconfigure(0, weight=1)
                row_frame.grid_columnconfigure(1, weight=1)
                row_frame.grid_columnconfigure(2, weight=1)
                row_frame.grid_columnconfigure(3, weight=1)
                row_frame.grid_columnconfigure(4, weight=1)
                row_frame.grid_columnconfigure(5, weight=1)

                # img_path = r"C:\\python-practice\\image1.png"

                # pil_img = Image.open(img_path)
                # pil_img = pil_img.resize((10, 10), Image.Resampling.LANCZOS)
                # customer_win.profile_pic = ImageTk.PhotoImage(pil_img)

                # Label(row_frame,image=customer[5]).grid(row=0, column=0, sticky="w", padx=5, pady=10)

                Label(
                    row_frame,
                    text=f"{customer[1]}",
                    # image=customer_win.profile_pic,
                    font=("arial", 16, "bold"),
                    bg=row_colour,
                    fg="white",
                    anchor="w",
                    width=20,
                    # image=customer_win.profile_pic,
                    # compound="right"
                ).grid(row=0, column=0, sticky="w", padx=0, pady=10)

                Label(
                    row_frame,
                    text=customer[3],
                    font=("arial", 14, "bold"),
                    bg=row_colour,
                    width=30,
                    fg="white",
                    anchor="w",
                ).grid(row=0, column=1, padx=0, sticky="w")

                Label(
                    row_frame,
                    text=f"{customer[2]}",
                    font=("arial", 14, "bold"),
                    bg=row_colour,
                    fg="white",
                    anchor="w",
                    width=20,
                ).grid(row=0, column=2, padx=0, sticky="w")

                Label(
                    row_frame,
                    text=f"{customer[4]}",
                    font=("arial", 14, "bold"),
                    bg=row_colour,
                    fg="white",
                    anchor="w",
                    width=20,
                ).grid(row=0, column=3, padx=0, sticky="w")

                Label(
                    row_frame,
                    text=f"{customer[6]}",
                    font=("arial", 14, "bold"),
                    bg=row_colour,
                    fg=bg,
                    anchor="w",
                    width=20,
                ).grid(row=0, column=4, padx=0, sticky="w")

                def customer_action(customer):
                    action_win = Toplevel(customer_win)
                    action_win.transient(customer_win)
                    action_win.grab_set()
                    # action_win.state("zoomed")
                    action_win.geometry("480x600+690+200")
                    action_win.title("Customer Action")
                    action_win.config(bg="#d9d8ea")

                    frame_bg = "#1A1D20"
                    header_frame = Frame(
                        action_win, bg="#1A1D20", bd=2, relief="groove"
                    )
                    header_frame.pack(fill=X, side=TOP, padx=0, pady=(0, 10))

                    img_path = r"default_pic.png"

                    try:
                        pil_img = Image.open(img_path)
                        pil_img = pil_img.resize((65, 65), Image.Resampling.LANCZOS)
                        action_win.profile_pic = ImageTk.PhotoImage(pil_img)

                        pic_label = Label(
                            header_frame, image=action_win.profile_pic, bg=frame_bg
                        )
                    except Exception as e:
                        pic_label = Label(
                            header_frame,
                            text="👤",
                            font=("Arial", 32),
                            fg="#ffffff",
                            bg=frame_bg,
                        )

                    pic_label.pack(side="left", padx=20, pady=15)

                    text_container = Frame(header_frame, bg=frame_bg)
                    text_container.pack(side="left", fill="both", expand=True, pady=15)

                    Label(
                        text_container,
                        text=f"{customer[1]}",
                        font=("Arial", 16, "bold"),
                        fg="#d9d8ea",
                        bg=frame_bg,
                        anchor="w",
                    ).pack(fill=X)
                    Label(
                        text_container,
                        text=f"ID: {customer[1]} | {customer[3]}",
                        font=("Arial", 10, "italic"),
                        fg="#d9d8ea",
                        bg=frame_bg,
                        anchor="w",
                    ).pack(fill=X)

                    id_frame = Frame(action_win, bg=frame_bg, bd=3, relief="groove")
                    id_frame.pack(fill=X, side=TOP, pady=5)
                    Label(
                        id_frame,
                        text="Customer ID:",
                        font=("Arial", 14, "bold"),
                        fg="#d9d8ea",
                        bg=frame_bg,
                        width=15,
                        anchor=W,
                    ).pack(pady=15, padx=20, side="left")
                    id_entry = Entry(
                        id_frame, font=("Arial", 12), fg="#132A07", width=20
                    )
                    id_entry.insert(0, customer[2])
                    id_entry.config(state="readonly")
                    id_entry.pack(pady=15, side="left", padx=10, ipadx=5)

                    name_frame = Frame(action_win, bg=frame_bg, bd=3, relief="groove")
                    name_frame.pack(fill=X, side=TOP, pady=5)

                    Label(
                        name_frame,
                        text="Customer Names:",
                        font=("Arial", 14, "bold"),
                        fg="#d9d8ea",
                        bg=frame_bg,
                        width=15,
                        anchor="w",
                    ).pack(pady=15, padx=20, side="left")
                    name_entry = Entry(
                        name_frame, font=("Arial", 12), fg="#132A07", width=20
                    )
                    name_entry.insert(0, customer[3])
                    name_entry.config(state="readonly")
                    name_entry.pack(pady=15, side="left", padx=10, ipadx=5)

                    location_frame = Frame(
                        action_win, bg=frame_bg, bd=3, relief="groove"
                    )
                    location_frame.pack(fill=X, side=TOP, pady=5)
                    Label(
                        location_frame,
                        text="Location:",
                        font=("Arial", 14, "bold"),
                        fg="#d9d8ea",
                        bg=frame_bg,
                        width=15,
                        anchor="w",
                    ).pack(pady=15, padx=20, side="left")
                    location_entry = Entry(
                        location_frame, font=("Arial", 12), fg="#132A07", width=20
                    )
                    location_entry.insert(0, customer[4])
                    location_entry.pack(pady=15, side="left", padx=10, ipadx=5)

                    mobile_frame = Frame(action_win, bg=frame_bg, bd=3, relief="groove")
                    mobile_frame.pack(fill=X, side=TOP, pady=5)
                    Label(
                        mobile_frame,
                        text="Contacts:",
                        font=("Arial", 14, "bold"),
                        fg="#d9d8ea",
                        bg=frame_bg,
                        width=15,
                        anchor="w",
                    ).pack(pady=15, padx=20, side="left")
                    mobile_entry = Entry(
                        mobile_frame, font=("Arial", 12), fg="#132A07", width=20
                    )
                    mobile_entry.insert(0, customer[5])
                    mobile_entry.pack(pady=15, side="left", padx=10, ipadx=5)

                    status_frame = Frame(action_win, bg=frame_bg, bd=3, relief="groove")
                    status_frame.pack(fill=X, side=TOP, pady=5)
                    Label(
                        status_frame,
                        text="Status:",
                        font=("Arial", 14, "bold"),
                        fg="#d9d8ea",
                        bg=frame_bg,
                        width=15,
                        anchor="w",
                    ).pack(pady=15, padx=20, side="left")
                    values = ("Active", "Closed", "Busy", "Inactive")
                    status_combobox = ttk.Combobox(
                        status_frame,
                        font=("Arial", 12),
                        state="readonly",
                        # fg="#132A07",
                        values=values,
                        width=18,
                    )
                    status_combobox.set(customer[6])
                    status_combobox.pack(pady=15, side="left", padx=10, ipadx=5)

                    def edit_customer():
                        location = location_entry.get()
                        mobile = mobile_entry.get()
                        status = status_combobox.get()
                        id = id_entry.get()
                        name = name_entry.get()

                        if location == "" or mobile == "" or status == "":
                            messagebox.showerror("Error", "Fill All Fields!")
                            return
                        if location.isdigit():
                            messagebox.showerror("Error", "Wrong Location!")
                            return
                        if not mobile.isdigit() or len(mobile) != 10:
                            messagebox.showerror("Error", "Wrong Mobile \nNumber")
                            return
                        else:
                            confirm = messagebox.askyesno(
                                "Confirm", "Are you sure to\nUpdate customer?"
                            )
                            if confirm:
                                conn = sqlite3.connect("phones.db")
                                c = conn.cursor()
                                c.execute(
                                    """UPDATE customers SET
                                              location = (?),
                                              mobile = (?),
                                              status = (?)
                                              WHERE id_number =(?)""",
                                    (location, mobile, status, id),
                                )
                                conn.commit()
                                conn.close()
                                messagebox.showinfo(
                                    "Successful", f"{name}\nUpdated Successfully!"
                                )
                                action_win.destroy()

                    def delete_customer():
                        id = id_entry.get()
                        name = name_entry.get()

                        confirm = messagebox.askyesno("confirm", f"DELETE\n{name}")
                        if confirm:
                            conn = sqlite3.connect("phones.db")
                            c = conn.cursor()
                            c.execute(
                                """DELETE FROM customers
                                            WHERE id = (?)""",
                                (id,),
                            )
                            conn.commit()
                            conn.close()
                            messagebox.showinfo(
                                f"DELETE", f"{name}\nDELETED SUCCESSFULLY"
                            )
                            action_win.destroy()

                    bottom_frame = Frame(
                        action_win, bg="#1A1D20", bd=2, relief="groove"
                    )
                    bottom_frame.pack(fill=X, side=BOTTOM, padx=0, pady=(5, 0))

                    submit_button = Button(
                        bottom_frame,
                        image=submit__button,
                        fg="#000000",
                        activebackground=frame_bg,
                        bg=frame_bg,
                        font=(
                            "Arial",
                            16,
                        ),
                        bd=0,
                        command=edit_customer,
                    )
                    submit_button.pack(pady=10, padx=(20, 5), side=TOP)

                    delete_button = Button(
                        bottom_frame,
                        image=delete__button,
                        fg="#000000",
                        activebackground=frame_bg,
                        bg=frame_bg,
                        font=(
                            "Arial",
                            10,
                        ),
                        bd=0,
                        command=delete_customer,
                    )
                    delete_button.pack(side=BOTTOM, pady=(5, 5), padx=5)

                Button(
                    row_frame,
                    text="Action",
                    font=("Arial", 12, "bold"),
                    bg="#1A1D20",
                    fg="#00F5FF",
                    command=lambda c=customer: customer_action(c),
                ).grid(row=0, column=5, padx=5, sticky="e", pady=10)

        def refresh_customers():
            conn = sqlite3.connect("phones.db")
            c = conn.cursor()
            c.execute("SELECT * FROM customers")
            customers = c.fetchall()

            display_customers(customers)
            if customer_win.winfo_exists:
                customer_win.after(10000000, refresh_customers)

        def delete_refresh():
            search_entry.delete(0, END)
            return refresh_customers()

        Button(
            search_frame,
            text="X",
            bg="#ffffff",
            fg="#000000",
            font=("calibri", 17, "bold"),
            bd=0,
            highlightthickness=0,
            height=1,
            command=delete_refresh,
        ).pack(side=LEFT)

        def search_customers():
            search_term = search_entry.get()
            conn = sqlite3.connect("customers.db")
            c = conn.cursor()
            c.execute(
                """SELECT * FROM customers
                       WHERE LOWER(name) 
                      LIKE LOWER(?) OR 
                      LOWER(location) 
                      LIKE LOWER(?) OR
                      LOWER(mobile) 
                      LIKE LOWER(?) OR
                      LOWER(status)
                      LIKE LOWER(?)""",
                (
                    "%" + search_term + "%",
                    "%" + search_term + "%",
                    "%" + search_term + "%",
                    "%" + search_term + "%",
                ),
            )
            results = c.fetchall()
            conn.close()
            display_customers(results)

        Button(
            search_frame,
            text="GO",
            bg="#000000",
            fg="#FFFFFF",
            font=("calibri", 17, "bold"),
            bd=0,
            highlightthickness=0,
            command=search_customers,
        ).pack(padx=5, side=LEFT)

        refresh_customers()

    customers_bt = Button(
        sale_mid_frame,
        text="Customers",
        font=("arial", 14, "bold"),
        fg="#A2DE82",
        bg="black",
        activebackground="#000000",
        activeforeground="#A2DE82",
        width=50,
        command=customers_,
    )
    customers_bt.grid(row=1, column=0, sticky=S, padx=30, pady=30)

    history = History()
    customers_history_bt = Button(
        sale_mid_frame,
        text="History",
        font=("arial", 14, "bold"),
        fg="#A2DE82",
        activebackground="#000000",
        activeforeground="#A2DE82",
        bg="black",
        width=50,
        command=history.history_window,
    )
    customers_history_bt.grid(row=1, column=1, sticky=S, padx=30, pady=30)

    statistic_bt = Button(
        sale_mid_frame,
        text="Statistics",
        font=("arial", 14, "bold"),
        fg="#A2DE82",
        activebackground="#000000",
        activeforeground="#A2DE82",
        bg="black",
        width=50,
    )
    statistic_bt.grid(row=0, column=1, pady=10, sticky=E, padx=30)


# button1 = create_styled_button(body_frame, "MANAGE GADGETS",open_view_gadgets)
# button2 = create_styled_button(body_frame, "PLACE A SALE",place_sales)

# button1.place(relx =0.5, rely=0.45, anchor="center")
# button2.place(relx =0.5, rely=0.55, anchor="center")

window.mainloop()
