import tkinter as tk
from tkinter import messagebox  # Import the messagebox module

# Function to simulate shaft rotation based on HT and VT values
def rotate_shaft(HT, VT):
    # Round the values to the nearest 0.05 increment
    HT = round(HT / 0.05) * 0.05
    VT = round(VT / 0.05) * 0.05
    
    # Simulate shaft rotation based on user input
    did_it_work = messagebox.askquestion("Shaft Rotation", f"Does it work with HT={HT:.2f} and VT={VT:.2f}?")
    return did_it_work == 'yes'

def find_optimal_HT(min_value, max_value):
    while max_value - min_value >= 0.05:
        current_value = (max_value + min_value) / 2
        
        # Clamp current_value to the specified range
        current_value = max(0.05, min(0.4, current_value))
        
        # Check HT and use the fixed VT for optimization
        if rotate_shaft(current_value, 0.40):  # Use a fixed VT of 0.20 for HT optimization
            max_value = current_value
        else:
            min_value = current_value
    
    # Round the output to the nearest 0.05 increment
    optimal_HT = round(max_value / 0.05) * 0.05
    
    return optimal_HT

def find_optimal_VT(min_value, max_value, optimal_HT):
    while max_value - min_value >= 0.05:
        current_value = (max_value + min_value) / 2
        
        # Clamp current_value to the specified range
        current_value = max(0.05, min(0.4, current_value))
        
        # Check VT using the optimal HT value
        if rotate_shaft(optimal_HT, current_value):
            max_value = current_value
        else:
            min_value = current_value
    
    # Round the output to the nearest 0.05 increment
    optimal_VT = round(max_value / 0.05) * 0.05
    
    return optimal_VT

# # Function to perform optimization
# def optimize_tolerance(min_value, max_value, increment):
#     while max_value - min_value >= increment:
#         current_value = (max_value + min_value) / 2
#         if rotate_shaft(current_value, current_value):
#             max_value = current_value
#         else:
#             min_value = current_value
    
#     return round(max_value / increment) * increment

# Function to handle the optimization process
def optimize():
    min_ht = float(min_ht_var.get())
    max_ht = float(max_ht_var.get())
    min_vt = float(min_vt_var.get())
    max_vt = float(max_vt_var.get())
    increment = float(increment_var.get())
    
    # Optimize HT
    optimal_HT = find_optimal_HT(min_ht, max_ht)
    optimal_ht_result_var.set(f"Optimal HT: {optimal_HT:.2f}")
    
    # Optimize VT using the optimal HT value
    optimal_VT = find_optimal_VT(min_vt, max_vt, optimal_HT)
    optimal_vt_result_var.set(f"Optimal VT: {optimal_VT:.2f}")

# Create the main application window
app = tk.Tk()
app.title("Bearing Tolerance Calibration")

# Create and set variables
min_ht_var = tk.DoubleVar(value=0.01)
max_ht_var = tk.DoubleVar(value=0.4)
min_vt_var = tk.DoubleVar(value=0.01)
max_vt_var = tk.DoubleVar(value=0.4)
increment_var = tk.DoubleVar(value=0.05)
optimal_ht_result_var = tk.StringVar()
optimal_vt_result_var = tk.StringVar()

# Create labels, entry fields, and buttons
label_min_ht = tk.Label(app, text="Min HT:")
entry_min_ht = tk.Entry(app, textvariable=min_ht_var)
label_max_ht = tk.Label(app, text="Max HT:")
entry_max_ht = tk.Entry(app, textvariable=max_ht_var)
label_min_vt = tk.Label(app, text="Min VT:")
entry_min_vt = tk.Entry(app, textvariable=min_vt_var)
label_max_vt = tk.Label(app, text="Max VT:")
entry_max_vt = tk.Entry(app, textvariable=max_vt_var)
label_increment = tk.Label(app, text="Increment:")
entry_increment = tk.Entry(app, textvariable=increment_var)
optimize_button = tk.Button(app, text="Optimize", command=optimize)
optimal_ht_label = tk.Label(app, textvariable=optimal_ht_result_var)
optimal_vt_label = tk.Label(app, textvariable=optimal_vt_result_var)

# Arrange widgets using grid layout
label_min_ht.grid(row=0, column=0)
entry_min_ht.grid(row=0, column=1)
label_max_ht.grid(row=0, column=2)
entry_max_ht.grid(row=0, column=3)
label_min_vt.grid(row=1, column=0)
entry_min_vt.grid(row=1, column=1)
label_max_vt.grid(row=1, column=2)
entry_max_vt.grid(row=1, column=3)
label_increment.grid(row=2, column=0)
entry_increment.grid(row=2, column=1)
optimize_button.grid(row=2, column=2, columnspan=2)
optimal_ht_label.grid(row=3, column=0, columnspan=2)
optimal_vt_label.grid(row=3, column=2, columnspan=2)

# Start the Tkinter main loop
app.mainloop()
