import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# configurasi
window = tk.Tk()
window.configure(bg="white")
window.title("Input Data mahasiswa")
window.geometry("400x400")
window.resizable(False, False)

# variabel
NAMA = tk.StringVar()
NPM = tk.StringVar()
SEMESTER = tk.StringVar()

# fungsi button
def kirim_data():
    pesan = f"Nama saya {NAMA.get()} Dengan NPM {NPM.get()} semester {SEMESTER.get()}"
    showinfo(title="HALO MAHASISWA",message=pesan)

## frame input
input_frame = ttk.Frame(window)
# penempatan ada grid, pack, place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# nama
label_nama = ttk.Label(input_frame, text="Input Nama :")
label_nama.pack(padx=10,  fill="x", expand=True)
input_nama = ttk.Entry(input_frame,textvariable=NAMA)
input_nama.pack(padx=10,  fill="x", expand=True)

# npm
label_npm = ttk.Label(input_frame, text="Input NPM :")
label_npm.pack(padx=10,  fill="x", expand=True)
input_npm = ttk.Entry(input_frame, textvariable=NPM)
input_npm.pack(padx=10,  fill="x", expand=True)

# semester
label_semester = ttk.Label(input_frame, text="Input Semester :")
label_semester.pack(padx=10,  fill="x",expand=True)
input_semester = ttk.Entry(input_frame, textvariable=SEMESTER)
input_semester.pack(padx=10,  fill="x",expand=True)

# tombol
tombol = ttk.Button(input_frame, text="Enter", command=kirim_data)
tombol.pack(padx=10,  fill="x", pady=10,expand=True)

window.mainloop()