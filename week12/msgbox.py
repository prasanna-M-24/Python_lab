import tkinter as tk
from tkinter import messagebox, filedialog

def show_message():
    messagebox.showinfo("Hello", "This is a Messagebox example!")

def open_file():
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if file_path:
        messagebox.showinfo("File Selected", f"You selected:\n{file_path}")

root = tk.Tk()
root.title("Messagebox and FileDialog Demo")
root.geometry("400x200")

btn_message = tk.Button(root, text="Show Messagebox", command=show_message, font=("Arial", 12), bg="lightblue")
btn_message.pack(pady=20)

btn_file = tk.Button(root, text="Open File Dialog", command=open_file, font=("Arial", 12), bg="lightgreen")
btn_file.pack(pady=20)

root.mainloop()