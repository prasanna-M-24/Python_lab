import tkinter as tk

root = tk.Tk()
root.title("Listbox and Scrollbar Demo")
root.geometry("300x250")

frame = tk.Frame(root)
frame.pack(pady=20)

listbox = tk.Listbox(frame, width=25, height=10)
listbox.pack(side="left", fill="y")

scrollbar = tk.Scrollbar(frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

for i in range(1, 51):   
    listbox.insert(tk.END, f"Item {i}")

root.mainloop()