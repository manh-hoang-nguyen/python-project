import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import threading
import ifcopenshell


def start_pb():
    pb.start()
    # for i in range(0, 101):
    #     time.sleep(0.05)
    ifc_file_path = "Duplex_Plumbing_20121113.ifc"
    ifcopenshell.open(ifc_file_path)
    print("finish")


def start_pb_thread():
    thread1 = threading.Thread(target=start_pb)
    thread1.start()


win = tk.Tk()

win.title("progress bar")
win.geometry("400x200")
progress_var = tk.IntVar()
pb = ttk.Progressbar(win, maximum=100, variable=progress_var, length=300)
pb.pack()

Button(win, text="start", command=start_pb_thread).pack(pady=20)
win.mainloop()
