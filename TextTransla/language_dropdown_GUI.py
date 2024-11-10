import os
import tkinter as tk
import sys
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

    button_send_to_web = tk.Button(root, text = "Translate!", command=lambda: click_button())
    button_send_to_web.grid(row = 1, column = 1, padx = 10, pady = 10)

    button_exit = tk.Button(root, text = "End", command = exit)
    button_exit.grid(row = 2, column = 1, padx = 10, pady = 10)




    root.mainloop()


#button that is clicked which opens application
def click_button():
    camera_works_path = os.path.abspath('../CameraWorks')  # Adjust path as needed
    sys.path.append(camera_works_path)
    import face_detection_with_subtitles as c
    return c


# dictionary for language translated and targets
def language_tab():
    return

def gui_language_dropdown():
    return

main()