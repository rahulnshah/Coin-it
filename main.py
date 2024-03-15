import tkinter as tk

def increment_pennies():
    pass

def increment_nickels():
    pass

def increment_dimes():
    pass

def increment_quarters():
    pass

def decrement_pennies():
    pass

def decrement_nickels():
    pass

def decrement_dimes():
    pass

def decrement_quarters():
    pass

window = tk.Tk()

# Top Frame
top_frame = tk.Frame(window)
top_frame.grid(row=0, column=0, padx=10, pady=10)

# Labels for coin types
pennies_label = tk.Label(top_frame, text="Pennies")
pennies_label.grid(row=0, column=0, padx=5, pady=5)

nickels_label = tk.Label(top_frame, text="Nickels")
nickels_label.grid(row=1, column=0, padx=5, pady=5)

dimes_label = tk.Label(top_frame, text="Dimes")
dimes_label.grid(row=2, column=0, padx=5, pady=5)

quarters_label = tk.Label(top_frame, text="Quarters")
quarters_label.grid(row=3, column=0, padx=5, pady=5)

current_balance_label = tk.Label(top_frame, text="Net Balance")
current_balance_label.grid(row=4, column=0, padx=5, pady=5)

# Labels for coin counts (initially set to 0)
pennies_count_label = tk.Label(top_frame, text="0")
pennies_count_label.grid(row=0, column=1, padx=5, pady=5)

nickels_count_label = tk.Label(top_frame, text="0")
nickels_count_label.grid(row=1, column=1, padx=5, pady=5)

dimes_count_label = tk.Label(top_frame, text="0")
dimes_count_label.grid(row=2, column=1, padx=5, pady=5)

quarters_count_label = tk.Label(top_frame, text="0")
quarters_count_label.grid(row=3, column=1, padx=5, pady=5)

balance_count_label = tk.Label(top_frame, text="0")
balance_count_label.grid(row=4, column=1, padx=5, pady=5)

# Bottom Frame
bottom_frame = tk.Frame(window)
bottom_frame.grid(row=1, column=0, padx=10, pady=10)

# Add Button Column
add_pennies_button = tk.Button(bottom_frame, text="Add Pennies", command=increment_pennies)
add_pennies_button.grid(row=0, column=0, padx=5, pady=5)

add_nickels_button = tk.Button(bottom_frame, text="Add Nickels", command=increment_nickels)
add_nickels_button.grid(row=1, column=0, padx=5, pady=5)

add_dimes_button = tk.Button(bottom_frame, text="Add Dimes", command=increment_dimes)
add_dimes_button.grid(row=2, column=0, padx=5, pady=5)

add_quarters_button = tk.Button(bottom_frame, text="Add Quarters", command=increment_quarters)
add_quarters_button.grid(row=3, column=0, padx=5, pady=5)

# Plus Button, Entry Box, Minus Button Column
plus_pennies_button = tk.Button(bottom_frame, text="+", command=increment_pennies)
plus_pennies_button.grid(row=0, column=1, padx=5, pady=5)

labels_pennies = tk.Label(bottom_frame, text="0")
labels_pennies.grid(row=0, column=2, padx=5, pady=5)

minus_pennies_button = tk.Button(bottom_frame, text="-", command=decrement_pennies)
minus_pennies_button.grid(row=0, column=3, padx=5, pady=5)

plus_nickels_button = tk.Button(bottom_frame, text="+", command=increment_nickels)
plus_nickels_button.grid(row=1, column=1, padx=5, pady=5)

labels_nickels = tk.Label(bottom_frame, text="0")
labels_nickels.grid(row=1, column=2, padx=5, pady=5)

minus_nickels_button = tk.Button(bottom_frame, text="-", command=decrement_nickels)
minus_nickels_button.grid(row=1, column=3, padx=5, pady=5)

plus_dimes_button = tk.Button(bottom_frame, text="+", command=increment_dimes)
plus_dimes_button.grid(row=2, column=1, padx=5, pady=5)

labels_dimes = tk.Label(bottom_frame, text="0")
labels_dimes.grid(row=2, column=2, padx=5, pady=5)

minus_dimes_button = tk.Button(bottom_frame, text="-", command=decrement_dimes)
minus_dimes_button.grid(row=2, column=3, padx=5, pady=5)

plus_quarters_button = tk.Button(bottom_frame, text="+", command=increment_quarters)
plus_quarters_button.grid(row=3, column=1, padx=5, pady=5)

labels_quarters = tk.Label(bottom_frame, text="0")
labels_quarters.grid(row=3, column=2, padx=5, pady=5)

minus_quarters_button = tk.Button(bottom_frame, text="-", command=decrement_quarters)
minus_quarters_button.grid(row=3, column=3, padx=5, pady=5)

# Take Button Column
take_pennies_button = tk.Button(bottom_frame, text="Take Pennies", command=decrement_pennies)
take_pennies_button.grid(row=0, column=4, padx=5, pady=5)

take_nickels_button = tk.Button(bottom_frame, text="Take Nickels", command=decrement_nickels)
take_nickels_button.grid(row=1, column=4, padx=5, pady=5)

take_dimes_button = tk.Button(bottom_frame, text="Take Dimes", command=decrement_dimes)
take_dimes_button.grid(row=2, column=4, padx=5, pady=5)

take_quarters_button = tk.Button(bottom_frame, text="Take Quarters", command=decrement_quarters)
take_quarters_button.grid(row=3, column=4, padx=5, pady=5)

window.mainloop()