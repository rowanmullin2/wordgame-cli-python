import tkinter as ttk
from tkinter import messagebox

def createWindow():
    window = ttk.Tk()
    window.title("Word Game")
    window.geometry("800x600")

    # Event listener for button click
    def on_button_click():
        messagebox.showinfo("Info", "Button clicked!"+" input: "+input_field.get())

    # test button
    button = ttk.Button(window, text="Click Me", command=on_button_click)
    button.pack(pady=20)

    # test input field
    input_field = ttk.Entry(window, width=10)
    input_field.pack(pady=20)

    return window

createWindow().mainloop()