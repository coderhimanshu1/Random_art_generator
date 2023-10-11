import tkinter as tk
from tkinter import ttk
import turtle
import random

def random_art():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.clear()

    for _ in range(random.randint(10, 30)):  # Repeat the pattern multiple times
        artistic_walk()

def artistic_walk():
    """Makes the turtle take a series of artistic steps."""
    # Select random attributes
    t.color(random.choice(colors))
    t.pensize(random.randint(1, 5))

    choice = random.choice(['line', 'circle', 'star', 'curve'])

    if choice == 'line':
        t.forward(random.randint(30, 100))
        t.right(random.randint(-180, 180))

    elif choice == 'circle':
        rad = random.randint(10, 50)
        t.circle(rad, random.randint(-180, 180))

    elif choice == 'star':
        points = random.randint(3, 6)
        size = random.randint(20, 100)
        for _ in range(points):
            t.forward(size)
            t.right(360 / points)

    elif choice == 'curve':
        for _ in range(random.randint(2, 6)):
            t.circle(random.randint(10, 40), 45)

    if random.randint(0, 1):
        t.penup()
    else:
        t.pendown()

# Create the main window
root = tk.Tk()
root.title("Random Art Generator")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Button to generate random art
generate_btn = ttk.Button(frame, text="Generate Random Art", command=random_art)
generate_btn.grid(row=0, column=0, pady=20)

# Set up the turtle canvas with specified dimensions
canvas_frame = ttk.Frame(root, padding="10")
canvas_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

canvas = turtle.ScrolledCanvas(canvas_frame, width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=tk.YES)

t = turtle.RawTurtle(canvas)
t.speed(0)

colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "pink", "brown", "gray"]

root.mainloop()
