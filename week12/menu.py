import tkinter as tk

root = tk.Tk()
root.title("Menu and Menubutton Demo")
root.geometry("400x250")

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
menubar.add_cascade(label="Edit", menu=edit_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About")
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

menubutton = tk.Menubutton(root, text="Options", relief="raised")
menubutton.menu = tk.Menu(menubutton, tearoff=0)
menubutton["menu"] = menubutton.menu

menubutton.menu.add_command(label="Option 1")
menubutton.menu.add_command(label="Option 2")
menubutton.menu.add_command(label="Option 3")

menubutton.pack(pady=50)

root.mainloop()