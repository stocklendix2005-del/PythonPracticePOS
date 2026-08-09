from tkinter import *
from CustomTitleBar import CustomToplevel
from database import get_notification

# print(get_notification)


def open_notifications(root):
    win = CustomToplevel(
        parent=root,
        title="Notifications",
        width=500,
        height=500,
        x=730,
        y=250,
        bg="white",
    )
    lbl = Label(
        win.content_area,
        text="Stock Alert",
        fg="#0C131A",
        bg="white",
        font=("arial", 13, "underline"),
    )
    lbl.pack(padx=20, pady=20)

    notification_frame = Frame(win.content_area, bg="white")
    notification_frame.pack(fill="x")

    low_stock = get_notification()

    if low_stock:
        for i, notification in enumerate(low_stock, start=1):
            not_label = Label(
                notification_frame,
                text=f"({i} {notification[2]} {notification[3]} - {notification[6]}",
                fg="yellow",
                font=("arial", 12, "bold"),
                bg="white",
            )
            not_label.pack(side="left")
    else:
        null_notificationsLabel = Label(
            notification_frame,
            text="Stock is healthy!",
            font=("arial", 12),
            fg="grey",
            bg="white",
        )
        null_notificationsLabel.pack(pady=10)

    update_header = Label(
        win.content_area,
        text=" Software Updates",
        fg="#0C131A",
        bg="white",
        font=("arial", 13, "underline"),
    )
    update_header.pack(padx=20, pady=20)
    update_frame = Frame(win.content_area, bg="white")
    update_frame.pack(fill="x")
    update_label = Label(
        update_frame,
        text="Software up to date.\nNew update will appear here.\n\nLENAPP Version: 1.00.0",
        font=("arial", 12, "bold"),
        fg="grey",
        bg="white",
    )
    update_label.pack(pady=10)
