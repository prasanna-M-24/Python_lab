import tkinter as tk

root = tk.Tk()
root.title("Geometry Methods Demo")
root.geometry("400x300")

frame_pack = tk.Frame(root, bg="lightblue", bd=2, relief="solid")
frame_pack.pack(pady=10, fill="x")

label_pack = tk.Label(frame_pack, text="This is placed using pack()", bg="lightblue")
label_pack.pack(pady=5)

frame_grid = tk.Frame(root, bg="lightgreen", bd=2, relief="solid")
frame_grid.pack(pady=10, fill="x")

label_grid1 = tk.Label(frame_grid, text="Row 0, Col 0", bg="lightyellow")
label_grid2 = tk.Label(frame_grid, text="Row 0, Col 1", bg="lightpink")
label_grid3 = tk.Label(frame_grid, text="Row 1, Col 0", bg="lightgray")

label_grid1.grid(row=0, column=0, padx=5, pady=5)
label_grid2.grid(row=0, column=1, padx=5, pady=5)
label_grid3.grid(row=1, column=0, padx=5, pady=5)

frame_place = tk.Frame(root, bg="orange", bd=2, relief="solid", width=380, height=80)
frame_place.pack(pady=10)

label_place = tk.Label(frame_place, text="This is placed using place()", bg="orange")
label_place.place(x=100, y=20)

root.mainloop()