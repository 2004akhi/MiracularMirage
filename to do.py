# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 20:11:51 2024

@author: user
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import datetime

# Function to display motivational quotes
def display_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. - Confucius"
    ]
    messagebox.showinfo("Motivational Quote", random.choice(quotes))

# Function to add tasks to the to-do list
def add_task():
    task = task_entry.get()
    due_date = due_date_entry.get()
    if task == "" or due_date == "":
        messagebox.showwarning("Warning", "Please enter both task and due date!")
        return
    todo_list.insert(tk.END, f"Task: {task} - Due Date: {due_date}")
    task_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Task added successfully!")

# Function to remind about due dates
def check_due_dates():
    today = datetime.date.today()
    due_dates = [task.split(" - Due Date: ")[1] for task in todo_list.get(0, tk.END)]
    for due_date in due_dates:
        due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
        if due_date_obj == today:
            messagebox.showinfo("Reminder", f"Task with due date {due_date} is due today!")

# Main function
def main():
    global todo_list, task_entry, due_date_entry

    # Create the main window
    root = tk.Tk()
    root.title("To-Do List App")

    # Load and display image
    image = Image.open("todo_list_image.jpg")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

    # Create and display widgets
    task_label = tk.Label(root, text="Task:")
    task_label.pack()
    task_entry = tk.Entry(root)
    task_entry.pack()

    due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
    due_date_label.pack()
    due_date_entry = tk.Entry(root)
    due_date_entry.pack()

    add_button = tk.Button(root, text="Add Task", command=add_task)
    add_button.pack()

    quote_button = tk.Button(root, text="Get Motivational Quote", command=display_quote)
    quote_button.pack()

    reminder_button = tk.Button(root, text="Check Due Dates", command=check_due_dates)
    reminder_button.pack()

    todo_list = tk.Listbox(root)
    todo_list.pack()

    root.mainloop()


    main()