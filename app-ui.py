import tkinter as ttk
from tkinter import messagebox

def createWindow():
    window = ttk.Tk()
    window.title("Word Game")
    window.geometry("800x600")

    # Event listener for button click
    def on_button_click():
        messagebox.showinfo("Info", "Button clicked!"+" input: "+input_field1.get())
    
    # Title display
    title = ttk.Label(window, text="Word Game", font=('Times New Roman', 30))
    title.pack(pady=20)

    # test button
    button = ttk.Button(window, text="Click Me", command=on_button_click)
    button.pack(pady=20)

    #grid layout

    # test input field
    input_field1 = ttk.Entry(window, font=('Times New Roman', 50), width=1)
    #input_field1.pack(pady=20, ipady=5)
    """
    input_field1.grid(row=0, column=0, padx=10, pady=10)
    input_field2 = ttk.Entry(window, font=('Times New Roman', 50), width=1)
    input_field2.pack(pady=20, ipady=5)
    input_field3 = ttk.Entry(window, font=('Times New Roman', 50), width=1)
    input_field3.pack(pady=20, ipady=5)
    input_field4 = ttk.Entry(window, font=('Times New Roman', 50), width=1)
    input_field4.pack(pady=20, ipady=5)
    input_field5 = ttk.Entry(window, font=('Times New Roman', 50), width=1)
    input_field5.pack(pady=20, ipady=5)
    """

    return window

createWindow().mainloop()