import tkinter as tk
from tkinter import messagebox
import random
import csv
import os
import re

# ================== THEME ==================
BG = "#f3f4f6"
CARD = "#e0f2fe"
PRIMARY = "#4f46e5"
DANGER = "#ef4444"
SUCCESS = "#22c55e"
TEXT = "#111827"
FONT = ("Segoe UI", 10)
TITLE_FONT = ("Segoe UI", 18, "bold")

CSV_FILE = "exam_sets.csv"
EXPORT_FILE = "exam_sets_export.csv"

# ================== NATURAL SORT ==================
def natural_key(s):
    return [int(t) if t.isdigit() else t.lower()
            for t in re.split(r'(\d+)', s)]

# ================== CSV INIT ==================
def ensure_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            csv.writer(f).writerow(
                ["Roll Number", "Set Number", "Level", "Question Changed"]
            )

ensure_csv()

# ================== APP ==================
class ExamSetGenerator:
    def __init__(self, root):
        self.root = root
        root.title("Exam Question Generator")
        root.geometry("1100x740")
        root.configure(bg=BG)

        self.level_sets = {}     # level -> list of sets
        self.last_set = {}       # level -> last used set

        tk.Label(root, text="Exam Question Generator",
                 font=TITLE_FONT, bg=BG, fg=TEXT).pack(pady=10)

        # ---------- LEVEL CONFIG ----------
        config = tk.Frame(root, bg=CARD, padx=20, pady=15)
        config.pack(fill="x", padx=20, pady=8)

        tk.Label(config, text="Instructor Level Configuration",
                 bg=CARD, font=("Segoe UI", 12, "bold"))\
            .grid(row=0, column=0, columnspan=5, sticky="w")

        tk.Label(config, text="Level Name", bg=CARD, font=FONT)\
            .grid(row=1, column=0, sticky="w")
        self.level_name_entry = tk.Entry(config, width=18, font=FONT)
        self.level_name_entry.grid(row=1, column=1)

        tk.Label(config, text="Set Numbers (comma separated)", bg=CARD, font=FONT)\
            .grid(row=1, column=2, sticky="w")
        self.level_sets_entry = tk.Entry(config, width=25, font=FONT)
        self.level_sets_entry.grid(row=1, column=3)

        tk.Button(
            config, text="Add Level",
            bg=SUCCESS, fg="white", font=FONT,
            relief="flat", padx=20,
            command=self.add_level
        ).grid(row=1, column=4, padx=10)

        self.level_list = tk.Listbox(
            config, width=85, height=4, font=("Consolas", 10)
        )
        self.level_list.grid(row=2, column=0, columnspan=5, pady=5)

        # ---------- STUDENT ACTIONS ----------
        card = tk.Frame(root, bg=CARD, padx=20, pady=15)
        card.pack(fill="x", padx=20, pady=8)

        tk.Label(card, text="Roll Number", bg=CARD, font=FONT)\
            .grid(row=0, column=0, sticky="w")
        self.roll_entry = tk.Entry(card, width=25, font=FONT)
        self.roll_entry.grid(row=0, column=1)

        tk.Label(card, text="Select Level", bg=CARD, font=FONT)\
            .grid(row=1, column=0, sticky="w")

        self.level_var = tk.StringVar()
        self.level_menu = tk.OptionMenu(card, self.level_var, "")
        self.level_menu.grid(row=1, column=1, sticky="w")

        tk.Button(card, text="Generate Set",
                  bg=PRIMARY, fg="white", font=FONT,
                  relief="flat", padx=20,
                  command=self.generate_set)\
            .grid(row=0, column=2, padx=10)

        tk.Button(card, text="Change Set",
                  bg=DANGER, fg="white", font=FONT,
                  relief="flat", padx=20,
                  command=self.change_set)\
            .grid(row=1, column=2, padx=10)

        tk.Button(card, text="Export CSV",
                  bg=SUCCESS, fg="white", font=FONT,
                  relief="flat", padx=20,
                  command=self.export_csv)\
            .grid(row=2, column=2, padx=10)

        # ---------- SEARCH ----------
        tk.Label(card, text="Find Roll (substring)", bg=CARD, font=FONT)\
            .grid(row=2, column=0, sticky="w")
        self.find_entry = tk.Entry(card, width=25, font=FONT)
        self.find_entry.grid(row=2, column=1)

        tk.Button(card, text="Find",
                  bg="#0ea5e9", fg="white", font=FONT,
                  relief="flat", padx=20,
                  command=self.find_roll)\
            .grid(row=2, column=3, padx=10)

        # ---------- LISTBOX ----------
        self.listbox = tk.Listbox(
            root, font=("Consolas", 11),
            width=120, height=16,
            bg="#f8fafc", fg=TEXT,
            selectbackground="#93c5fd"
        )
        self.listbox.pack(padx=20, pady=10)

        self.refresh_listbox()

    # ---------- ADD LEVEL ----------
    def add_level(self):
        name = self.level_name_entry.get().strip()
        raw = self.level_sets_entry.get().strip()

        try:
            sets = [int(x) for x in raw.split(",") if x.strip().isdigit()]
            if not name or not sets:
                raise ValueError
        except:
            messagebox.showerror("Invalid", "Enter valid level name and set numbers")
            return

        self.level_sets[name] = sets
        self.last_set[name] = None

        self.level_list.insert(tk.END, f"{name:15} → {sets}")

        menu = self.level_menu["menu"]
        menu.add_command(label=name, command=lambda v=name: self.level_var.set(v))
        if not self.level_var.get():
            self.level_var.set(name)

        self.level_name_entry.delete(0, tk.END)
        self.level_sets_entry.delete(0, tk.END)

    # ---------- CSV HELPERS ----------
    def read_csv(self):
        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = [r for r in reader if len(r) >= 4]
        return header, rows

    def write_sorted_csv(self, header, rows):
        rows.sort(key=lambda r: natural_key(r[0]))
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)

    # ---------- REFRESH ----------
    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        self.listbox.insert(
            tk.END,
            "ROLL NUMBER                | SET | LEVEL        | QUESTION CHANGED"
        )
        self.listbox.insert(tk.END, "-" * 120)

        _, rows = self.read_csv()
        rows.sort(key=lambda r: natural_key(r[0]))

        for r in rows:
            self.listbox.insert(
                tk.END,
                f"{r[0]:25} |  {r[1]:>2}  | {r[2]:12} | {r[3]}"
            )

    # ---------- GENERATE ----------
    def generate_set(self):
        roll = self.roll_entry.get().strip()
        level = self.level_var.get()

        if not roll or level not in self.level_sets:
            messagebox.showerror("Error", "Invalid roll or level")
            return

        header, rows = self.read_csv()
        if any(r[0] == roll for r in rows):
            messagebox.showwarning("Exists", "Roll already exists")
            return

        available = self.level_sets[level].copy()
        if self.last_set[level] in available:
            available.remove(self.last_set[level])

        set_no = random.choice(available)
        rows.append([roll, str(set_no), level, "NO"])
        self.last_set[level] = set_no

        self.write_sorted_csv(header, rows)
        self.refresh_listbox()
        self.roll_entry.delete(0, tk.END)

    # ---------- CHANGE SET ----------
    def change_set(self):
        sel = self.listbox.curselection()
        if not sel or sel[0] < 2:
            return

        idx = sel[0] - 2
        header, rows = self.read_csv()
        roll, old_set, level, _ = rows[idx]

        available = self.level_sets[level].copy()
        if int(old_set) in available:
            available.remove(int(old_set))

        new_set = random.choice(available)
        rows[idx][1] = str(new_set)
        rows[idx][3] = "YES"
        self.last_set[level] = new_set

        self.write_sorted_csv(header, rows)
        self.refresh_listbox()

    # ---------- FIND ----------
    def find_roll(self):
        target = self.find_entry.get().lower().strip()
        self.listbox.selection_clear(0, tk.END)

        for i in range(2, self.listbox.size()):
            if target in self.listbox.get(i).lower():
                self.listbox.selection_set(i)
                self.listbox.see(i)

    # ---------- EXPORT ----------
    def export_csv(self):
        with open(CSV_FILE, "r", newline="") as src, \
             open(EXPORT_FILE, "w", newline="") as dest:
            csv.writer(dest).writerows(csv.reader(src))
        messagebox.showinfo("Exported", "CSV exported successfully")

# ================== RUN ==================
root = tk.Tk()
ExamSetGenerator(root)
root.mainloop()
