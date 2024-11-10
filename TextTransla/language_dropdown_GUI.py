import os
import tkinter as tk
import sys
import threading
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

    main_frame = ttk.Frame(root)
    main_frame.grid(row=0, column=0, sticky="nsew")  # Use grid instead of pack

    # Create a frame for the scrollable list of tabs on the left side
    left_frame = ttk.Frame(main_frame, width=100)
    left_frame.grid(row=0, column=0, sticky="ns")  # Align to the left with sticky

    # Create the scrollable list of folder names
    tab_list_canvas = tk.Canvas(left_frame)
    tab_list_canvas.grid(row=0, column=0, sticky="nsew")  # Fill available space in left_frame

    # Configure grid weights for expanding behavior within main_frame and left_frame
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)  # Allows the right side to expand
    left_frame.grid_rowconfigure(0, weight=1)
    left_frame.grid_columnconfigure(0, weight=1)

    button_send_to_web = tk.Button(root, text = "Translate!", command=lambda: start_task())
    button_send_to_web.grid(row = 1, column = 1, padx = 10, pady = 10)

    proj_label = tk.Label(root, text = "Instant Language Translator", font = ("Helvetica", 35), bg = "white", fg = "blue")
    proj_label.grid(row=0, column = 0, columnspan = 5, padx = 10, pady = 10, sticky = "nsew")

    button_exit = tk.Button(root, text = "End", command = root.quit())
    button_exit.grid(row = 2, column = 1, padx = 10, pady = 10)
    root.bind('<Escape>', lambda e: root.destroy())
    camera_works_path = os.path.abspath('../CameraWorks')
    sys.path.append(camera_works_path)
    def click_button():
        import face_detection_with_subtitles as c
        return c

    def start_task():
        # Run the long task in a separate thread
        task_thread = threading.Thread(target=click_button)
        task_thread.start()

    # dictionary for language translated and targets
    def language_tab():
        return

    def gui_language_dropdown():
        return


    root.mainloop()


main()