import os
import tkinter as tk
import sys
import threading
from tkinter import ttk
from googletrans import LANGUAGES
lang_dict = {value: key for key, value in LANGUAGES.items()}
langs = list(lang_dict.keys())
name_selected = False
def click_button():
    if name_selected:
        import face_detection_with_subtitles as c
        return c

def start_task():
    # Run the long task in a separate thread
    task_thread = threading.Thread(target=click_button)
    task_thread.start()
def curr_lang(tab_name):
    global name_selected
    selected_tab_label.config(text="Select a Language: " + tab_name)
    name_selected = True
root = tk.Tk()
root.title("Instant Language Translator")
root.state('zoomed')
root.geometry("800x600")

# Main frame
main_frame = ttk.Frame(root)
main_frame.pack(expand = True, fill = 'both')

# Project label
proj_label = tk.Label(main_frame, text="Instant Language Translator", font=("Helvetica", 55), bg="white", fg="blue")
proj_label.pack(padx=10, pady=10)
name_selected = False
left_frame = ttk.Frame(main_frame, width=100)
left_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)
tab_list_canvas = tk.Canvas(left_frame)
tab_list_canvas.pack(fill=tk.BOTH, expand=True)
tab_list_frame = ttk.Frame(tab_list_canvas)
tab_list_canvas.create_window((0, 0), window=tab_list_frame, anchor='nw')
root.bind('<Escape>', lambda e: root.destroy())
content_frame = ttk.Frame(main_frame)
content_frame.pack(side = tk.LEFT, expand=True, fill='both')
button_open_applic = tk.Button(main_frame, text="Translate!", font = ("Helvetica", 40), bg = "green", fg = "white", command=lambda: start_task(), justify="center")
button_open_applic.pack(side = tk.LEFT, expand = True, fill = 'both')
notebook = ttk.Notebook(root)

tab_frame = ttk.Frame(root)
tab_frame.pack(side=tk.TOP, pady=10)

tab_buttons = []
for i, lang in enumerate(langs):
    tab_button = tk.Button(tab_frame, text=lang, font = ("Helvetica", 18), bg ="blue", fg ="white", command=lambda name = lang: curr_lang(name), width=15, height=2)
    tab_button.grid(row=0, column=i, padx=8)
    if i == 5:
        break

# Display the currently selected tab
selected_tab_label = tk.Label(root, text="Select a Language:", font=("Helvetica", 35), bg = "light blue", pady = 10)
selected_tab_label.place(x = 159, y = 400)

names_label = tk.Label(root, text="Umair Ali\n Faraz Akber\nAhmed Algerian\nTaha Hayali", font=("Helvetica", 15), justify="center", padx = 15, pady = 10)
names_label.place(x=30, y=20)

team_label = tk.Label(root, text = "TYPE INT", font = ("Helvetica", 25, "bold italic"), fg = "red")
team_label.place(x=1250, y = 30)

root.mainloop()
# Create content frames for each tab (using Notebook for content organization)
content_notebook = ttk.Notebook(root)
content_notebook.pack(expand=True, fill="both")

root.mainloop()