import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import threading
import speech_recognition as sr

# Create root window
root = tk.Tk()
root.title("Speech Recognition")
root.geometry("400x350")

# Define color scheme and fonts
bg_color = "#dda0dd"
fg_color = "#000000"
button_color = "#4B8BBE"
font_style = Font(family="Helvetica", size=10, weight="bold")
title_font_style = Font(family="Helvetica", size=16, weight="bold")

# Configure root window
root.configure(bg=bg_color)

# Create a frame for title
title_frame = tk.Frame(root, bg=bg_color)
title_frame.pack(fill="x", padx=20, pady=10)

# Add a title label
title_label = ttk.Label(title_frame,text="Speech Recognition App",font=title_font_style, background=bg_color, foreground=fg_color)
title_label.pack()

# ... rest of your code ...
def take_speech(language):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        update_status("Listening...", "blue")
        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            update_status("Recognizing...", "blue")
            query = r.recognize_google(audio, language=language)
            update_result(f"Recognized Text: {query}", "black")

        except sr.UnknownValueError:
            update_result("Could not understand audio, please say that again.", "red")

        except sr.RequestError as e:
            update_result(f"Could not request results; {e}", "red")

        except Exception as e:
            update_result(f"An error occurred: {e}", "red")

        finally:
            progress.stop()

def on_select():
    language = language_var.get()
    if language in ["Hindi", "Kannada", "Tamil","Bengali","Telugu"]:
        progress.start()
        threading.Thread(target=take_speech, args=(language_codes[language],)).start()

def update_status(message, color):
    status_var.set(message)
    status_label.config(foreground=color)

def update_result(message, color):
    result_var.set(message)
    result_label.config(foreground=color)



# Change button color and font
style = ttk.Style()
style.configure("TButton", background=button_color, foreground=fg_color, font=font_style)

# ... rest of your code ...
language_label = ttk.Label(root, text="Select Language:", font=("Helvetica", 10, "bold"))
language_label.pack(pady=5)

language_var = tk.StringVar()
language_menu = ttk.Combobox(root, textvariable=language_var)
language_menu['values'] = ("Hindi", "Kannada", "Tamil","Bengali","Telugu")
language_menu.pack(pady=5)

# Recognition button
button = ttk.Button(root, text="Start Recognition", command=on_select)
button.pack(pady=10)

# Status display
status_var = tk.StringVar()
status_label = ttk.Label(root, textvariable=status_var, font=("Arial", 10), foreground="black")
status_label.pack(pady=5)

# Progress bar
progress = ttk.Progressbar(root, mode='indeterminate')
progress.pack(pady=5)

# Result display
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, font=("Arial", 12), wraplength=380, foreground="black")
result_label.pack(pady=10)

language_codes = {
    "Hindi": "hi-IN",
    "Kannada": "kn-IN",
    "Tamil": "ta-IN",
    "Bengali":"bn-IN",
    "Telugu":"te-IN"
}

root.mainloop()