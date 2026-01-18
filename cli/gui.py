import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# FIX IMPORT PATH
sys.path.append(os.path.dirname(__file__))

from classifier import classify_downloads
from duplicate_finder import clean_duplicates
from undoer import undo_last_operation
from searcher import search_files

selected_path = ""

def choose_folder():
    global selected_path
    selected_path = filedialog.askdirectory()
    path_label.config(text=selected_path)

def classify_action():
    if not selected_path:
        messagebox.showerror("Error", "Select folder first")
        return
    classify_downloads(selected_path)
    messagebox.showinfo("Done", "Classification completed")

def undo_action():
    undo_last_operation()
    messagebox.showinfo("Done", "Undo completed")

def clean_duplicates_action():
    if not selected_path:
        messagebox.showerror("Error", "Select folder first")
        return
    clean_duplicates(selected_path)

def search_action():
    if not selected_path:
        messagebox.showerror("Error", "Select folder first")
        return
    keyword = search_entry.get().strip()
    if not keyword:
        messagebox.showerror("Error", "Enter keyword")
        return
    search_files(selected_path, keyword)

# ---------------- GUI ----------------

root = tk.Tk()
root.title("SortDown")
root.geometry("600x400")

tk.Label(root, text="SortDown", font=("Arial", 18, "bold")).pack(pady=10)

tk.Button(root, text="Select Folder", command=choose_folder).pack()
path_label = tk.Label(root, text="No folder selected", wraplength=450)
path_label.pack(pady=5)

tk.Button(root, text="Classify Files", width=40, command=classify_action).pack(pady=5)
tk.Button(root, text="Undo Last Classification", width=40, command=undo_action).pack(pady=5)
tk.Button(root, text="Clean Duplicates", width=40, command=clean_duplicates_action).pack(pady=5)

tk.Label(root, text="Search File Name").pack(pady=5)
search_entry = tk.Entry(root, width=40)
search_entry.pack()
tk.Button(root, text="Search", command=search_action).pack(pady=5)

root.mainloop()
