import tkinter as tk
from tkinter import ttk

from utils import initializing_components, send_request_button
from styles import FOREGROUND_COLOR, BACKGROUND_COLOR_WINDOW

# Config window
root = tk.Tk()
root.title("Requesty")
style = ttk.Style()

# Styles
root.configure(background=BACKGROUND_COLOR_WINDOW)

style.configure("TLabel",
                foreground=FOREGROUND_COLOR,
                background=BACKGROUND_COLOR_WINDOW,
                font="Arial 30")
style.configure("TButton",
                foreground="black",
                background="white")
style.configure("TEntry",
                width=20,
                foreground="black",
                background=BACKGROUND_COLOR_WINDOW,
                font="Arial 13")
style.configure("TRadiobutton",
                foreground=FOREGROUND_COLOR,
                background=BACKGROUND_COLOR_WINDOW,
                font="Arial 13")


var_method = tk.StringVar()


def test():
    """test"""
    print(var_method.get())


# Components
url_question = ttk.Label(root, text="URL")
url = ttk.Entry(root)

get_method_radio_button = ttk.Radiobutton(
    root, variable=var_method, value="GET", text="GET", command=test)
#post_method_radio_button = ttk.Radiobutton(
#    root, variable=var_method, value="POST", text="POST", command=test)

send_button = ttk.Button(root, text="Send Request",
                         command=lambda: send_request_button(url, method=var_method))


# Main function
def run_window():
    """Run window"""
    initializing_components(
        url_question, url, get_method_radio_button, send_button)

    print(get_method_radio_button.winfo_class())

    root.mainloop()
