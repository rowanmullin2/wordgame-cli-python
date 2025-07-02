import tkinter as ttk
from tkinter import messagebox

FONT = 'Times New Roman'

RULES = """
Welcome to the Word Game!
In this game, you will be presented with a grid of 5 boxes.
You need to input a 5-letter word by typing one letter in each box.
Once you have entered your word, the game will then validate it against the word you are trying to guess.
The game will provide feedback on your guess, indicating which letters are correct, and the right position, which letters are correct, but in the wrong position and which letters aren't in the word.
If you need help, click the "Rules" button to see the instructions again.
Have fun and good luck!
"""

def createWindow():
  window = ttk.Tk()
  window.title("Word Game")
  window.geometry("800x600")

  # Event listener for button click
  def on_rules_button_click():
    messagebox.showinfo("Rules / Info", RULES)
  
  # Title display
  title = ttk.Label(window, text="Word Game", font=(FONT, 30))
  title.pack(pady=20)

  # Rules button
  rules_button = ttk.Button(window, text="Rules", command=on_rules_button_click)
  rules_button.pack(pady=20)

  #grid layout
  grid_frame = ttk.Frame(window)
  grid_frame.pack(pady=20)

  # word input fields

  # first row
  input_field1 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field1.grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=10)
  input_field2 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field2.grid(row=1, column=2, padx=10, pady=10, ipadx=10, ipady=10)
  input_field3 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field3.grid(row=1, column=3, padx=10, pady=10, ipadx=10, ipady=10)
  input_field4 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field4.grid(row=1, column=4, padx=10, pady=10, ipadx=10, ipady=10)
  input_field5 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field5.grid(row=1, column=5, padx=10, pady=10, ipadx=10, ipady=10)
  # second row
  input_field6 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field6.grid(row=2, column=1, padx=10, pady=10, ipadx=10, ipady=10)
  input_field7 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field7.grid(row=2, column=2, padx=10, pady=10, ipadx=10, ipady=10)
  input_field8 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field8.grid(row=2, column=3, padx=10, pady=10, ipadx=10, ipady=10)
  input_field9 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field9.grid(row=2, column=4, padx=10, pady=10, ipadx=10, ipady=10)
  input_field10 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field10.grid(row=2, column=5, padx=10, pady=10, ipadx=10, ipady=10)
  # third row
  input_field11 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field11.grid(row=3, column=1, padx=10, pady=10, ipadx=10, ipady=10)
  input_field12 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field12.grid(row=3, column=2, padx=10, pady=10, ipadx=10, ipady=10)
  input_field13 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field13.grid(row=3, column=3, padx=10, pady=10, ipadx=10, ipady=10)
  input_field14 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field14.grid(row=3, column=4, padx=10, pady=10, ipadx=10, ipady=10)
  input_field15 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field15.grid(row=3, column=5, padx=10, pady=10, ipadx=10, ipady=10)
  # fourth row
  input_field16 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field16.grid(row=4, column=1, padx=10, pady=10, ipadx=10, ipady=10)
  input_field17 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field17.grid(row=4, column=2, padx=10, pady=10, ipadx=10, ipady=10)
  input_field18 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field18.grid(row=4, column=3, padx=10, pady=10, ipadx=10, ipady=10)
  input_field19 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field19.grid(row=4, column=4, padx=10, pady=10, ipadx=10, ipady=10)
  input_field20 = ttk.Entry(grid_frame, font=(FONT, 50), justify="center", width=1)
  input_field20.grid(row=4, column=5, padx=10, pady=10, ipadx=10, ipady=10)

  # input_field.get() - used to retrieve the input from the fields

  return window

createWindow().mainloop()