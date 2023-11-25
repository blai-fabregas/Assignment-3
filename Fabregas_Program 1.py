import tkinter as tk
from tkinter import messagebox

def open_shopping_window():
    # Shopping window
    shopping_window = tk.Toplevel()
    shopping_window.title("Uella's Epicurean Emporium")
    shopping_window.geometry("400x250")
    shopping_window.configure(bg="#e6f7ff")

    # Labels
    apple_label = tk.Label(shopping_window, 
        text="Quantity of Apples:", 
        font=("Times New Roman", 12), 
        bg="#e6f7ff")
    orange_label = tk.Label(shopping_window, 
        text="Quantity of Oranges:", 
        font=("Times New Roman", 12), 
        bg="#e6f7ff")
    result_label = tk.Label(shopping_window, 
        text="Total amount to pay:", 
        font=("Times New Roman", 14), 
        bg="#e6f7ff")
    
    # Entries
    apple_entry = tk.Entry(shopping_window, 
        font=("Times New Roman", 12))
    orange_entry = tk.Entry(shopping_window, 
        font=("Times New Roman", 12))

    # Summations
    calculate_button = tk.Button(shopping_window, text="Add to Cart", 
        command=lambda: calculate_total_amount(apple_entry, orange_entry, result_label, shopping_window),
        font=("Times New Roman", 12), 
        bg="#4caf50", 
        fg="white")

    apple_label.grid(
        row=0, 
        column=0, 
        padx=10, 
        pady=10)
    apple_entry.grid(
        row=0, 
        column=1, 
        padx=10, 
        pady=10)
    orange_label.grid(
        row=1, 
        column=0, 
        padx=10, 
        pady=10)
    orange_entry.grid(
        row=1, 
        column=1, 
        padx=10, 
        pady=10)
    calculate_button.grid(
        row=2, 
        column=0, 
        columnspan=2, 
        pady=10)
    result_label.grid(
        row=3, 
        column=0, 
        columnspan=2, 
        pady=10)

def proceed_to_payment(total_amount, shopping_window):
    payment_confirmation_window = tk.Toplevel(shopping_window)
    payment_confirmation_window.title("Payment Confirmation")
    payment_confirmation_window.geometry("300x150")
    payment_confirmation_window.configure(bg="#e6f7ff")

    confirmation_label = tk.Label(payment_confirmation_window, 
        text=f"Total Amount: {total_amount} pesos\nProceed to payment?",
        font=("Times New Roman", 14),
        bg="#e6f7ff")
    confirmation_label.pack(pady=20)

    yes_button = tk.Button(payment_confirmation_window, text="Yes", 
        command=lambda: complete_payment(shopping_window, payment_confirmation_window),
        font=("Times New Roman", 12), 
        bg="#4caf50", 
        fg="white")
    yes_button.pack(side=tk.LEFT, padx=10)

    no_button = tk.Button(payment_confirmation_window, text="No", 
        command=payment_confirmation_window.destroy,
        font=("Times New Roman", 12), 
        bg="#ff9999", 
        fg="white")
    no_button.pack(side=tk.RIGHT, padx=10)

def complete_payment(shopping_window, payment_confirmation_window):
    messagebox.showinfo("Payment Complete", "Payment has been successfully completed!")
    shopping_window.destroy()
    payment_confirmation_window.destroy()

def calculate_total_amount(apple_entry, orange_entry, result_label, shopping_window):
    try:
        # Quantity
        apple_quantity = int(apple_entry.get())
        orange_quantity = int(orange_entry.get())
        if apple_quantity < 0 or orange_quantity < 0:
            raise ValueError("Quantities must be positive.")

        # Total 
        total_amount = (apple_quantity * 20) + (orange_quantity * 25)

        # Result
        result_label.config(text=f"Total amount to pay: {total_amount} pesos", fg="green")
        shopping_window.configure(bg="#b9ffb0")

        proceed_to_payment(total_amount, shopping_window)

    except ValueError as e:
        messagebox.showerror("Error", str(e))
        result_label.config(text="Please enter valid numeric values for the quantities.", fg="red")
        shopping_window.configure(bg="#ff9999")

# Main Window
window = tk.Tk()
window.title("Fruitas")
window.geometry("768x864")

# Window Background Photo
image_path = "C:\\Users\\uella blainne\\Downloads\\Background Photo.gif"
photo = tk.PhotoImage(file=image_path)
background_label = tk.Label(window, image=photo)
background_label.place(relwidth=1, relheight=1) 

# 1st Button
open_shopping_button = tk.Button(window,
    text="Fill my Cart", 
    command=open_shopping_window, 
    font=("Times New Roman Bold", 50), 
    bg="#4caf50", 
    fg="white")
open_shopping_button.pack(side=tk.BOTTOM, padx=50, pady=100)

# Run
window.mainloop()
