import tkinter as tk

def display_text():
    user_input = entry.get()
    label_output.config(text=f"You entered: {user_input}")

root = tk.Tk()
root.title("GUI Application")
root.geometry("350x200")
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack()
entry = tk.Entry(root, width=25, font=("Arial", 12))
entry.pack()
button = tk.Button(root, text="Submit", command=display_text, font=("Arial", 12), bg="lightblue")
button.pack()
label_output = tk.Label(root, text="", font=("Arial", 12), fg="green")
label_output.pack()

root.mainloop()