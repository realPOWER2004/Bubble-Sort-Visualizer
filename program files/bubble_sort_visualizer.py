import ctypes
import tkinter as tk
import random
import time

# Load the shared C library
bubble_sort = ctypes.CDLL('./libbubblesort.so')  # Replace with the actual path to your shared library

# Define the function signature for C functions
bubble_sort.startSorting.argtypes = [ctypes.c_char_p]
bubble_sort.startSorting.restype = None
bubble_sort.generateRandomValues.argtypes = []
bubble_sort.generateRandomValues.restype = None
bubble_sort.resetInput.argtypes = []
bubble_sort.resetInput.restype = None

def start_sorting():
    input_text = entry.get()
    bubble_sort.startSorting(input_text.encode('utf-8'))
    visualize_sorting(input_text)

def visualize_sorting(input_text):
    numbers = list(map(int, input_text.split()))
    n = len(numbers)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                entry.delete(0, tk.END)  # Clear the input field
                entry.insert(0, ' '.join(map(str, numbers)))  # Update the input field
                draw_bars(numbers, j, j + 1)
                time.sleep(0.2)  # Adjust the delay for visualization
                draw_bars(numbers, -1, -1)  # Reset color to red

def draw_bars(numbers, highlight_index1, highlight_index2):
    canvas.delete('all')
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    bar_width = canvas_width / len(numbers)
    
    for i, number in enumerate(numbers):
        x0 = i * bar_width
        y0 = canvas_height
        x1 = (i + 1) * bar_width
        y1 = canvas_height - number * (canvas_height / 100)  # Scale the bar heights for visualization
        if i == highlight_index1 or i == highlight_index2:
            canvas.create_rectangle(x0, y0, x1, y1, fill="green")
        else:
            canvas.create_rectangle(x0, y0, x1, y1, fill="red")
    canvas.update()

def generate_random_values():
    random_values = [random.randint(1, 100) for _ in range(10)]
    entry.delete(0, tk.END)
    entry.insert(0, ' '.join(map(str, random_values)))
    bubble_sort.generateRandomValues()
    visualize_sorting(' '.join(map(str, random_values)))

def reset_input():
    bubble_sort.resetInput()
    entry.delete(0, tk.END)
    canvas.delete('all')

# Create the Tkinter window
window = tk.Tk()
window.title("Bubble Sort Visualizer")

# Canvas for visualization
canvas = tk.Canvas(window, bg='white')
canvas.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Entry field
entry_label = tk.Label(window, text="Enter numbers separated by spaces:")
entry_label.grid(row=1, column=0, columnspan=4, pady=10)
entry = tk.Entry(window, width=30)  # Slightly larger input field
entry.insert(0, "54 32 12 89 45")  # Initial input
entry.grid(row=2, column=0, columnspan=4)

# Start Sorting button
start_button = tk.Button(window, text="Start Sorting", command=start_sorting)
start_button.grid(row=3, column=0, columnspan=4, pady=10)

# Generate Random Values button
generate_random_button = tk.Button(window, text="Generate Random", command=generate_random_values)
generate_random_button.grid(row=4, column=0, columnspan=4, pady=10)

# Reset button
reset_button = tk.Button(window, text="Reset", command=reset_input)
reset_button.grid(row=5, column=0, columnspan=4, pady=10)

# Adjust row and column weights to allow resizing
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
window.grid_rowconfigure(0, weight=1)

# Initially draw bars with current canvas size
draw_bars([int(num) for num in entry.get().split()], -1, -1)

window.mainloop()
