from tkinter import *


def delete_field(tree):
    selected = tree.focus()
    item_id = tree.item(selected, "values")[0]
