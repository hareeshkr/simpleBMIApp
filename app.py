import tkinter as tk
from tkinter import Text

root = tk.Tk()
root.title("Simple BMI Calculator")

weight = tk.StringVar()
height = tk.StringVar()

def calc():
    weight = int(weight_entry.get())
    height = int(height_entry.get())
    bmi = weight / (height * height)
    tk.Label(root, text="Your BMI is " + str(bmi)).grid(row="3", column="0")


tk.Label(root, text="Enter your weight: ").grid(row="0", column="0")
tk.Label(root, text="Enter your height: ").grid(row="1", column="0")
weight_entry = tk.Entry(root, textvariable=weight)
height_entry = tk.Entry(root, textvariable=height)
tk.Button(root, text="Calculate BMI", command=calc).grid(row="2", column="0")

weight_entry.grid(row="0", column="1")
height_entry.grid(row="1", column="1")


root.mainloop()