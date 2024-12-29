import tkinter as tk
from math import sqrt

# Function to calculate the roots of the quadratic equation
def calculate_roots():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        discriminant = b**2 - 4*a*c
        
        # Check if discriminant is positive, negative, or zero
        if discriminant > 0:
            root1 = (-b + sqrt(discriminant)) / (2*a)
            root2 = (-b - sqrt(discriminant)) / (2*a)
            result_label.config(text=f"X = {root1:.2f}\nX = {root2:.2f}", fg="red", font=("Helvetica", 12, "bold"))
        elif discriminant == 0:
            root = -b / (2*a)
            result_label.config(text=f"X = {root:.2f}", fg="red", font=("Helvetica", 12, "bold"))
        else:
            real_part = -b / (2*a)
            imaginary_part = sqrt(abs(discriminant)) / (2*a)
            result_label.config(text=f"Complex roots: {real_part:.2f} ± {imaginary_part:.2f}i", fg="red", font=("Helvetica", 12, "bold"))
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.", fg="red", font=("Helvetica", 12))

# Set up the main window
window = tk.Tk()
window.title("Quadratic Solver")
window.geometry("213x299")  # Set initial window size to 213x299 (Width x Height)
window.config(bg="#1c1c1c")  # Dark background
window.resizable(True, True)  # Allow resizing

# Frame for entry fields (single box)
input_frame = tk.Frame(window, bg="#1c1c1c", bd=2, relief="solid")
input_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Labels and entry fields (simplified)
label_a = tk.Label(input_frame, text="Enter x²:", font=("Helvetica", 12), bg="#1c1c1c", fg="white", anchor="center")
label_a.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
entry_a = tk.Entry(input_frame, font=("Helvetica", 12), width=8, bd=2, relief="solid", fg="white", bg="#2f2f2f")
entry_a.grid(row=0, column=1, padx=5, pady=5)

label_b = tk.Label(input_frame, text="Enter x:", font=("Helvetica", 12), bg="#1c1c1c", fg="white", anchor="center")
label_b.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
entry_b = tk.Entry(input_frame, font=("Helvetica", 12), width=8, bd=2, relief="solid", fg="white", bg="#2f2f2f")
entry_b.grid(row=1, column=1, padx=5, pady=5)

# Label and entry for c (fixed to display correctly)
label_c = tk.Label(input_frame, text="Enter c:", font=("Helvetica", 12), bg="#1c1c1c", fg="white", anchor="center")
label_c.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
entry_c = tk.Entry(input_frame, font=("Helvetica", 12), width=8, bd=2, relief="solid", fg="white", bg="#2f2f2f")
entry_c.grid(row=2, column=1, padx=5, pady=5)

# Calculate button with dark red color
calculate_button = tk.Button(window, text="Calculate", font=("Helvetica", 12), command=calculate_roots, bg="#8B0000", fg="white", relief="raised", padx=10, pady=5)
calculate_button.pack(pady=10)

# Result label with initial text
result_label = tk.Label(window, text="Roots will be displayed here.", font=("Helvetica", 12), bg="#1c1c1c", fg="red")
result_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
