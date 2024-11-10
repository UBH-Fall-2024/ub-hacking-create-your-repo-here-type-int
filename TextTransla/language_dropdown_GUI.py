import os
import tkinter as tk
from tkinter import ttk
from googletrans import LANGUAGES
lang_dict = {value: key for key, value in LANGUAGES.items()}
langs = lang_dict.keys

def main():
    root = tk.Tk()
    root.title("Instant Language Translator")
    root.state('zoomed')
    root.geometry("800x600")
    root.rowconfigure(1, weight = 1)
    root.columnconfigure(1, weight = 1)

    proj_label = tk.Label(root, text = "Instant Language Translator", font = ("Helvetica", 35), bg = "white", fg = "blue")
    proj_label.grid(row=0, column = 0, columnspan = 5, padx = 10, pady = 10, sticky = "nsew")






    root.mainloop()


#button that is clicked which sends user to web app
def click_button():
    return

# dictionary for language translated and targets
def language_tab():
    return

def gui_language_dropdown():
    return

main()