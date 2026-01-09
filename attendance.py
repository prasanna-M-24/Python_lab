import tkinter as tk
from tkinter import messagebox
import random

# ================== COLOR THEME ==================
BG = "#f3f4f6"
CARD = "#e0f2fe"
PRIMARY = "#4f46e5"
TEXT = "#111827"
FONT = ("Segoe UI", 10)
TITLE_FONT = ("Segoe UI", 18, "bold")

# ================== LEVEL → SET MAP ==================
LEVEL_SETS = {
    "Foundation": [1, 2, 3],
    "Standard": [4, 5, 6],
    "Challenging": [7, 8, 9],
    "Advanced": [10, 11, 12]
}

# ================== APP ==================
class ExamSetGenerator:
    def __init__(self, root):
        self.root = root
        root.title("Exam Question Generator")
        root.geometry("720x520")
        root.configure(bg=BG)

        tk.Label(
            root,
            text="Exam Question Generator",
            font=TITLE_FONT,
            bg=BG,
            fg=TEXT
        ).pack(pady=15)

        card = tk.Frame(root, bg=CARD, padx=20, pady=20)
        card.pack(fill="x", padx=20, pady=10)

        tk.Label(card, text="Roll Number", bg=CARD, font=FONT)\
            .grid(row=0, column=0, sticky="w")
        self.roll_entry = tk.Entry(card, width=25, font=FONT)
        self.roll_entry.grid(row=0, column=1, pady=5)

        tk.Label(card, text="Select Level", bg=CARD, font=FONT)\
            .grid(row=1, column=0, sticky="w")

        self.level_var = tk.StringVar(value="Foundation")
        tk.OptionMenu(
            card, self.level_var,
            "Foundation", "Standard", "Challenging", "Advanced"
        ).grid(row=1, column=1, sticky="w")

        tk.Button(
            card, text="Generate Set",
            bg=PRIMARY, fg="white",
            font=FONT, relief="flat",
            padx=20,
            command=self.generate_set
        ).grid(row=2, column=0, columnspan=2, pady=15)

        self.listbox = tk.Listbox(
            root, font=("Consolas", 11),
            width=65, height=12,
            bg="#f8fafc", fg=TEXT
        )
        self.listbox.pack(padx=20, pady=10)

        self.listbox.insert(
            tk.END,
            "ROLL NUMBER                | SET | LEVEL"
        )
        self.listbox.insert(tk.END, "-" * 55)

    def generate_set(self):
        roll = self.roll_entry.get().strip()
        level = self.level_var.get()

        if not roll:
            messagebox.showerror("Error", "Roll number is required")
            return

        set_no = random.choice(LEVEL_SETS[level])

        self.listbox.insert(
            tk.END,
            f"{roll:25} |  {set_no:>2}  | {level}"
        )

        self.roll_entry.delete(0, tk.END)

# ================== RUN ==================
root = tk.Tk()
ExamSetGenerator(root)
root.mainloop()
