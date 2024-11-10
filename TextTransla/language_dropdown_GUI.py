import os
import tkinter as tk
import sys
import threading
import subprocess
import time
from tkinter import ttk
from googletrans import LANGUAGES
lang_dict = {value: key for key, value in LANGUAGES.items()}
langs = []
for lang in lang_dict:
    if lang == "arabic" or lang == "french" or lang == "hindi" or lang == "turkish":
        langs.append(lang)
        
lang_to_model = {  
                 "arabic" : "vosk-model-ar-0.22-linto-1.1.0",
                    "french" : "vosk-model-fr-0.6-linto-2.2.0",
                    "turkish" : "vosk-model-small-tr-0.3",
                 "russian" : "vosk-model-ru-0.42",
                 "hindi" : "vosk-model-hi-0.22"
                 }

name_selected = False
selected_language = None
def main():
    root = tk.Tk()
    root.title("Instant Language Translator")
    root.state('zoomed')
    root.geometry("800x600")

    main_frame = ttk.Frame(root)
    main_frame.pack(expand = True, fill = 'both')

    proj_label = tk.Label(main_frame, text="Instant Language Translator", font=("Helvetica", 55), bg="white", fg="blue")
    proj_label.pack(padx=10, pady=10)
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
    for i, lang in enumerate(langs):
        tab_button = tk.Button(tab_frame, text=lang, font = ("Helvetica", 18), bg ="blue", fg ="white", command=lambda name = lang: curr_lang(name), width=15, height=3)
        tab_button.grid(row=0, column=i, padx=8, pady = 25)
        if i == 5:
            break


    selected_tab_label = tk.Label(root, text="Select a Language:", font=("Helvetica", 35), bg = "light blue", pady = 10)
    selected_tab_label.place(x = 159, y = 350)

    names_label = tk.Label(root, text="Umair Ali\n Faraz Akber\nAhmed Bouhraoua\nTaha Hayali", font=("Helvetica", 15), justify="center", padx = 15, pady = 10)
    names_label.place(x=30, y=20)

    team_label = tk.Label(root, text = "TYPE INT", font = ("Helvetica", 25, "bold italic"), fg = "red")
    team_label.place(x=1250, y = 30)


    content_notebook = ttk.Notebook(root)
    content_notebook.pack(expand=True, fill="both")
    
    def click_button():
        if name_selected and selected_language:
            subprocess.Popen(["python3", "offline.py", selected_language])
            print(f"Starting Vosk server with language: {selected_language}")
            time.sleep(4)
            subprocess.Popen(["python3", "face_detection_with_subtitlesv.py"])
    def start_task():
        task_thread = threading.Thread(target=click_button)
        task_thread.start()

    def curr_lang(tab_name):
        global name_selected, selected_language
        selected_tab_label.config(text="Select a Language: " + tab_name)
        selected_language = lang_to_model[tab_name] 
        name_selected = True
        print(f"Selected language: {selected_language}")

    root.mainloop()

main()
