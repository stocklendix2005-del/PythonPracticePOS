from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


import tkinter as tk
import urllib.parse
import webbrowser


def search_query(query):
    # Safely encode the search text (e.g., "oppo reno 2z" -> "oppo%20reno%202z")
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={encoded_query}"

    # Open the URL in the system's default browser
    webbrowser.open(url)


# Initialize Tkinter window
root = tk.Tk()
root.title("Search Browser Example")
root.geometry("300x150")

# Target search term
search_term = "oppo reno 2z"

# Create button with a lambda function to pass the query argument
btn = tk.Button(
    root,
    text=f'Search "{search_term}"',
    command=lambda: search_query(search_term),
    padx=10,
    pady=5,
)
btn.pack(expand=True)

root.mainloop()
