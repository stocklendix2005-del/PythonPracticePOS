import tkinter as tk


class CustomToplevel(tk.Toplevel):
    def __init__(
        self,
        parent,
        title="Custom Window",
        width=800,
        height=600,
        x=200,
        y=60,
        bg="#1A1D20",
        title_color="#FF9100",
    ):
        super().__init__(parent, bg=bg)

        # Remove standard window decorations and set geometry
        self.overrideredirect(True)
        self.geometry(f"{width}x{height}+{x}+{y}")

        # Track drag offset
        self._offset_x = 0
        self._offset_y = 0

        # --- Title Bar Setup ---
        self.title_bar = tk.Frame(self, bg=bg, height=32)
        self.title_bar.pack(fill=tk.X)

        self.title_label = tk.Label(
            self.title_bar,
            text=title,
            bg=bg,
            fg=title_color,
            font=("Segoe UI", 10, "bold"),
        )
        self.title_label.pack(side=tk.LEFT, padx=12, pady=6)

        # Binding window drag to title bar and label
        for element in (self.title_bar, self.title_label):
            element.bind("<Button-1>", self._start_move)
            element.bind("<B1-Motion>", self._do_move)

        self.focus()
        self.grab_set()

        def enforce_parent_alpha(event):
            parent.attributes("-alpha", 0.4)

        self.bind("<FocusIn>", enforce_parent_alpha)
        # self.bind("<Button-1>", enforce_parent_alpha)

        def close__focus_out():
            parent.attributes("-alpha", 1.0)
            new_focus = self.focus_get()
            if new_focus is None or not str(new_focus).startswith(str(self)):
                self.destroy()

        self.bind("<FocusOut>", lambda event: close__focus_out())

        def close_win():
            self.destroy()
            parent.attributes("-alpha", 1.0)

        # Close Button
        self.close_button = tk.Button(
            self.title_bar,
            text="✕",
            bg=bg,
            fg="white",
            bd=0,
            font=("Segoe UI", 11),
            activebackground="#c42b1c",
            activeforeground="white",
            command=lambda: close_win(),
        )
        self.close_button.pack(side=tk.RIGHT, padx=8)

        # --- Main Content Container ---
        # Any child widgets for this window should be placed inside content_area
        self.content_area = tk.Frame(self, bg=bg)
        self.content_area.pack(fill=tk.BOTH, expand=True)

    def _start_move(self, event):
        self._offset_x = event.x
        self._offset_y = event.y

    def _do_move(self, event):
        x = self.winfo_x() + (event.x - self._offset_x)
        y = self.winfo_y() + (event.y - self._offset_y)
        self.geometry(f"+{x}+{y}")
