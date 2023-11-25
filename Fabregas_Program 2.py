import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from PIL import Image, ImageTk

def button_click(number):
    current = entry_var.get()
    entry_var.set(current + str(number))

def clear_entry():
    entry_var.set("")

def calculate_apples_and_remaining_money():
    try:
        # money & apple price
        money = float(entry_var.get())
        apple_price = float(entry_apple_price.get())

        # remaining money and apple
        max_apples = int(money // apple_price)
        remaining_money = money % apple_price

        # result display
        result_text = f"You can buy {max_apples} apples.\nRemaining money: {remaining_money:.2f} pesos"
        entry_var.set(result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Main Window
window = tk.Tk()
window.title("My Shopping Calculator")
image_path = "C:\\Users\\uella blainne\\Downloads\\Program 2 Window Background.gif"
bg_image = Image.open(image_path)
bg_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(window, image=bg_photo)
background_label.place(relwidth=1, relheight=1)
title_font = tkfont.Font(family="calibri", size=24, weight="bold", slant="italic")
title_label = tk.Label(window, text="My Shopping Calculator", font=title_font)
title_label.grid(row=0, column=0, columnspan=4)
entry_var = tk.StringVar()
entry_var.set("")
entry_display = tk.Entry(window, textvariable=entry_var, 
    font=("Times New Roman", 16), 
    justify="right", bd=10)
entry_display.grid(row=1, column=0, columnspan=4)

# numeric buttons
buttons = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', '+']

row_val = 2
col_val = 0

for button in buttons:
    tk.Button(window, 
        text=button, 
        font=("Times New Roman", 16), 
        padx=30, pady=30, 
        bg="#ff6666",
        command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

tk.Button(window, 
    text="C", 
    font=("Times New Roman", 16), 
    padx=20, pady=20, 
    bg="#ff6666",
    command=clear_entry).grid(row=row_val, column=col_val, columnspan=2)

# apple price
label_apple_price = tk.Label(window, 
    text="Price of an apple", 
    font=("Times New Roman", 12))
label_apple_price.grid(row=row_val + 1, column=0, columnspan=4)

entry_apple_price = tk.Entry(window, 
    font=("Times New Roman", 12),
    bg="#ff6666",)
entry_apple_price.grid(row=row_val + 2, column=0, columnspan=4)

# calculate button
calculate_button = tk.Button(window, 
    text="Calculate", 
    font=("Times New Roman", 16), 
    bg="#ff6666",
    padx=20, pady=20,
    command=calculate_apples_and_remaining_money)
calculate_button.grid(row=row_val + 3, column=0, columnspan=4)

# Run the GUI
window.mainloop()
