import os
import tkinter as tk
import sys
import threading
from tkinter import ttk
from googletrans import LANGUAGES
lang_dict = {value: key for key, value in LANGUAGES.items()}
langs = list(lang_dict.keys())

def end():
    sys.exit()

def click_button():
    import face_detection_with_subtitles as c
    return c

def start_task():
    # Run the long task in a separate thread
    task_thread = threading.Thread(target=click_button)
    task_thread.start()

def curr_lang(lang):
    global button_lang_select
    button_lang_select.config(text="Selected Language: " + lang, bg="blue", fg="white")
    return
def language_tab():
    return

def gui_language_dropdown():
    return

root = tk.Tk()
root.title("Instant Language Translator")
root.state('zoomed')
root.geometry("800x600")

# Main frame
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Project label
proj_label = tk.Label(main_frame, text="Instant Language Translator", font=("Helvetica", 35), bg="white", fg="blue")
proj_label.pack(padx=10, pady=10)

# Left frame
left_frame = ttk.Frame(main_frame, width=100)
left_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)

# Tab list canvas
tab_list_canvas = tk.Canvas(left_frame)
tab_list_canvas.pack(fill=tk.BOTH, expand=True)
tab_list_frame = ttk.Frame(tab_list_canvas)
tab_list_canvas.create_window((0, 0), window=tab_list_frame, anchor='nw')

content_frame = ttk.Frame(main_frame)
content_frame.pack(side=tk.RIGHT, expand=True, fill='both')
button_open_applic = tk.Button(main_frame, text="Translate!", font = ("Helvetica", 45), bg = "green", fg = "white", command=lambda: start_task())
button_open_applic.pack(expand = True)
notebook = ttk.Notebook(root)
i = 0
for lang in langs:
    tab_frame = ttk.Frame(notebook)
    notebook.add(tab_frame, text=lang)
    i+=1
    if i > 5:
        break
languages_frame = ttk.LabelFrame(root, text="Available Languages", padding=(10, 5))
languages_frame.pack(side=tk.TOP, fill="x", padx=20, pady=(20, 10))


notebook.pack(expand = True, fill = 'both')
button_lang_select = tk.Label(main_frame, text = "Selected Language: ", font = ("Helvetica", 35), bg = "blue", fg = "white")
button_lang_select.pack(padx = 40, pady = 40)
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()