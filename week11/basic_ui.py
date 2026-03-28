import tkinter as tk
root = tk.Tk()
root.title("Hello World App")
root.geometry("300x150")   
label = tk.Label(root, text="Hello World", font=("Arial", 20), fg="blue")
label.pack()   
root.mainloop()