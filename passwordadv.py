import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Password Generator")

        # Password length
        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0)
        self.length_entry = tk.Entry(master, width=5)
        self.length_entry.grid(row=0, column=1)

        # Password complexity
        self.complexity_label = tk.Label(master, text="Password Complexity:")
        self.complexity_label.grid(row=1, column=0)
        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")
        self.complexity_menu = tk.OptionMenu(master, self.complexity_var, "Low", "Medium", "High")
        self.complexity_menu.grid(row=1, column=1)

        # Character sets
        self.letters_var = tk.IntVar()
        self.numbers_var = tk.IntVar()
        self.symbols_var = tk.IntVar()
        self.letters_check = tk.Checkbutton(master, text="Letters", variable=self.letters_var)
        self.letters_check.grid(row=2, column=0)
        self.numbers_check = tk.Checkbutton(master, text="Numbers", variable=self.numbers_var)
        self.numbers_check.grid(row=2, column=1)
        self.symbols_check = tk.Checkbutton(master, text="Symbols", variable=self.symbols_var)
        self.symbols_check.grid(row=2, column=2)

        # Generate password button
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=3)

        # Password display
        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.grid(row=4, column=0, columnspan=3)
        self.password_entry = tk.Entry(master, width=40)
        self.password_entry.grid(row=5, column=0, columnspan=3)

        # Copy to clipboard button
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=6, column=0, columnspan=3)

    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_var.get()
        has_letters = self.letters_var.get()
        has_numbers = self.numbers_var.get()
        has_symbols = self.symbols_var.get()

        char_set = ''
        if has_letters:
            char_set += string.ascii_letters
        if has_numbers:
            char_set += string.digits
        if has_symbols:
            char_set += string.punctuation

        if complexity == "Low":
            password = ''.join(random.choice(char_set) for _ in range(length))
        elif complexity == "Medium":
            password = ''.join(random.choice(char_set) for _ in range(length // 2)) + ''.join(random.choice(string.ascii_letters) for _ in range(length // 2))
        elif complexity == "High":
            password = ''.join(random.choice(char_set) for _ in range(length // 3)) + ''.join(random.choice(string.ascii_letters) for _ in range(length // 3)) + ''.join(random.choice(string.digits) for _ in range(length // 3))

        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
my_gui = PasswordGenerator(root)
root.mainloop()
