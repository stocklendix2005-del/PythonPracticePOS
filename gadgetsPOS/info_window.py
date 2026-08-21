from tkinter import *
from CustomTitleBar import CustomToplevel
from tkinter import messagebox


def open_info_window(root, values):
    values = values
    if values:
        win = CustomToplevel(
            parent=root, title="INFO", width=500, height=500, x=730, y=250, bg="#0C131A"
        )
        win.configure(bd=2, highlightthickness=2, highlightcolor="#2c3e50")

        def info_layout():
            frames = []
            for i in range(1, 6):
                frame = Frame(
                    win,
                    bg="grey",
                    bd=2,
                    highlightthickness=2,
                    height=90,
                    highlightcolor="yellow",
                )
                frame.rowconfigure(0, weight=0)
                frame.rowconfigure(1, weight=1)
                frame.pack(fill="x", side="top")
                frames.append(frame)

            info_code = values[1]

            if info_code.startswith("G0"):
                titles = ["DISPLAY:", "CONNECTIVITY:", "CHIPSET", "BATTERY", "BUILD"]
            else:
                titles = [
                    "TOTAL SALES",
                    "CREDIT LIMIT",
                    "SUCCESSFUL SALES",
                    "FAILED SALES",
                    "STATUS",
                ]

            def title_griding(frame, title):
                return Label(
                    frame,
                    text=f"{title}",
                    font=("arial", 11, "bold"),
                    fg="orange",
                    bg="grey",
                ).grid(row=0, sticky="n", column=0, padx=10)

            title_griding(frames[0], titles[0])
            title_griding(frames[1], titles[1])
            title_griding(frames[2], titles[2])
            title_griding(frames[3], titles[3])
            title_griding(frames[4], titles[4])

        info_layout()
