import tkinter as tk
from tkinter import messagebox
import random
import csv
import os

# ================== COLOR THEME ==================
BG = "#f3f4f6"

CARD_REG = "#e0f2fe"     # light blue
CARD_LAT = "#ecfeff"     # light cyan
CARD_SET = "#fef9c3"     # light yellow
CARD_ACTION = "#ede9fe"  # light purple

PRIMARY = "#4f46e5"
DANGER = "#ef4444"
SUCCESS = "#22c55e"
TEXT = "#111827"

FONT = ("Segoe UI", 10)
TITLE_FONT = ("Segoe UI", 18, "bold")

# ================== LOGIC ==================

def generate_alpha_rolls(start, count):
    prefix = start[:-2]
    letter = start[-2].upper()
    digit = int(start[-1])
    rolls = []

    for _ in range(count):
        rolls.append(f"{prefix}{letter}{digit}")
        digit += 1
        if digit == 10:
            digit = 0
            letter = chr(ord(letter) + 1)
            if letter > 'Z':
                raise ValueError("Exceeded Z9 limit")
    return rolls

def generate_lateral_rolls(start, count):
    prefix = start[:-2]
    num = int(start[-2:])
    return [f"{prefix}{num+i:02d}" for i in range(count)]

def generate_sets(students, total_sets):
    sets = [(i % total_sets) + 1 for i in range(students)]
    random.shuffle(sets)

    for i in range(1, students):
        if sets[i] == sets[i-1] or abs(sets[i] - sets[i-1]) == 1:
            for j in range(i + 1, students):
                if (
                    sets[j] != sets[i-1]
                    and abs(sets[j] - sets[i-1]) != 1
                ):
                    sets[i], sets[j] = sets[j], sets[i]
                    break
    return sets

# ================== UI APP ==================

class ExamAllocator:
    def __init__(self, root):
        self.root = root
        root.title("Exam Allocation System")
        root.geometry("820x620")
        root.configure(bg=BG)

        tk.Label(
            root,
            text="Exam Allocation System",
            font=TITLE_FONT,
            bg=BG,
            fg=TEXT
        ).pack(pady=15)

        self.entries = {}

        # ---------- REGULAR CARD ----------
        reg_card = tk.Frame(root, bg=CARD_REG, padx=15, pady=10)
        reg_card.pack(fill="x", padx=20, pady=5)

        tk.Label(
            reg_card, text="Regular Students",
            bg=CARD_REG, font=("Segoe UI", 12, "bold")
        ).grid(row=0, column=0, columnspan=2, sticky="w")

        self.entries["reg_start"] = self.add_input(
            reg_card, "Start Roll (A0 / 23335A04A0)", 1
        )
        self.entries["reg_count"] = self.add_input(
            reg_card, "Number of Regular Students", 2
        )

        # ---------- LATERAL CARD ----------
        lat_card = tk.Frame(root, bg=CARD_LAT, padx=15, pady=10)
        lat_card.pack(fill="x", padx=20, pady=5)

        tk.Label(
            lat_card, text="Lateral Students",
            bg=CARD_LAT, font=("Segoe UI", 12, "bold")
        ).grid(row=0, column=0, columnspan=2, sticky="w")

        self.entries["lat_start"] = self.add_input(
            lat_card, "Lateral Start Roll", 1
        )
        self.entries["lat_count"] = self.add_input(
            lat_card, "Number of Lateral Students", 2
        )

        # ---------- SET CARD ----------
        set_card = tk.Frame(root, bg=CARD_SET, padx=15, pady=10)
        set_card.pack(fill="x", padx=20, pady=5)

        tk.Label(
            set_card, text="Exam Settings",
            bg=CARD_SET, font=("Segoe UI", 12, "bold")
        ).grid(row=0, column=0, columnspan=2, sticky="w")

        self.entries["sets"] = self.add_input(
            set_card, "Number of Question Sets", 1
        )
        self.entries["marks"] = self.add_input(
            set_card, "Initial Marks", 2
        )

        # ---------- ACTION CARD ----------
        action_card = tk.Frame(root, bg=CARD_ACTION, padx=15, pady=12)
        action_card.pack(fill="x", padx=20, pady=10)

        tk.Button(
            action_card, text="Generate Allocation",
            bg=PRIMARY, fg="white", font=FONT,
            relief="flat", padx=20,
            command=self.generate
        ).pack(side="left", padx=10)

        tk.Button(
            action_card, text="Change Set (-5 Marks)",
            bg=DANGER, fg="white", font=FONT,
            relief="flat", padx=20,
            command=self.change_set
        ).pack(side="left", padx=10)

        tk.Button(
            action_card, text="Export CSV",
            bg=SUCCESS, fg="white", font=FONT,
            relief="flat", padx=20,
            command=self.export_csv
        ).pack(side="left", padx=10)

        # ---------- TABLE ----------
        self.listbox = tk.Listbox(
            root, font=("Consolas", 10),
            bg="#f8fafc", fg=TEXT,
            selectbackground=PRIMARY,
            width=100, height=12,
            relief="flat"
        )
        self.listbox.pack(padx=20, pady=10)

    def add_input(self, parent, label, row):
        tk.Label(
            parent, text=label,
            bg=parent["bg"], font=FONT
        ).grid(row=row, column=0, sticky="w", pady=3)

        entry = tk.Entry(parent, width=20, font=FONT)
        entry.grid(row=row, column=1, pady=3)
        return entry

    def generate(self):
        try:
            rolls = []

            if self.entries["reg_start"].get():
                rolls += generate_alpha_rolls(
                    self.entries["reg_start"].get(),
                    int(self.entries["reg_count"].get())
                )

            if self.entries["lat_start"].get():
                rolls += generate_lateral_rolls(
                    self.entries["lat_start"].get(),
                    int(self.entries["lat_count"].get())
                )

            total_students = len(rolls)
            total_sets = int(self.entries["sets"].get())
            init_marks = int(self.entries["marks"].get())

            if total_students > 1 and total_sets < 3:
                messagebox.showerror(
                    "Invalid Configuration",
                    "At least 3 sets are required."
                )
                return

            self.rolls = rolls
            self.marks = [init_marks] * total_students
            self.sets = generate_sets(total_students, total_sets)

            self.listbox.delete(0, tk.END)
            self.listbox.insert(
                tk.END,
                "ROLL NUMBER                | SET | MARKS"
            )
            self.listbox.insert(
                tk.END,
                "-" * 55
            )

            for i in range(total_students):
                self.listbox.insert(
                    tk.END,
                    f"{self.rolls[i]:25} |  {self.sets[i]:>2}  |  {self.marks[i]}"
                )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def change_set(self):
        sel = self.listbox.curselection()
        if not sel or sel[0] < 2:
            return

        i = sel[0] - 2
        self.marks[i] -= 5
        self.sets[i] = random.randint(
            1, int(self.entries["sets"].get())
        )

        self.listbox.delete(sel[0])
        self.listbox.insert(
            sel[0],
            f"{self.rolls[i]:25} |  {self.sets[i]:>2}  |  {self.marks[i]}"
        )

    def export_csv(self):
        with open("exam_allocation.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Roll Number", "Set Number", "Marks"])
            for i in range(len(self.rolls)):
                writer.writerow(
                    [self.rolls[i], self.sets[i], self.marks[i]]
                )

        messagebox.showinfo(
            "Exported",
            f"CSV saved at:\n{os.getcwd()}"
        )

# ================== RUN ==================
root = tk.Tk()
ExamAllocator(root)
root.mainloop()
