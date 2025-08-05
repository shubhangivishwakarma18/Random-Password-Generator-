import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  

def generate_password():
    length = int(length_slider.get())
    use_letters = var_letters.get()
    use_digits = var_digits.get()
    use_symbols = var_symbols.get()

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    entry_result.delete(0, tk.END)
    entry_result.insert(0, password)

def copy_to_clipboard():
    password = entry_result.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

window = tk.Tk()
window.title("Random Password Generator")
window.geometry("400x300")
window.resizable(False, False)

tk.Label(window, text="Select Password Length:").pack(pady=5)
length_slider = tk.Scale(window, from_=4, to=30, orient=tk.HORIZONTAL)
length_slider.set(15)
length_slider.pack()

var_letters = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)
var_uppercase = tk.BooleanVar(value=True)

tk.Checkbutton(window, text="Include Letters (A-Z, a-z)", variable=var_letters).pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Include Numbers (0-9)", variable=var_digits).pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Include Symbols (!@#$)", variable=var_symbols).pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Include Uppercase (A-Z)", variable=var_letters).pack(anchor="w", padx=20)

tk.Button(window, text="Generate Password", command=generate_password).pack(pady=10)

entry_result = tk.Entry(window, width=30, font=("Arial", 12), justify='center')
entry_result.pack(pady=5)

tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)
window.mainloop()
