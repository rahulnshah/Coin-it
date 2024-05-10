import tkinter as tk

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    
    # don't want the values to be negative
    if value - 1 >= 0:
        lbl_value["text"] = f"{value - 1}"

def increment_pennies():
    value = int(lbl_value["text"])

    # increment the count of pennies by value
    coin_counts[1] += value

    # reset the text of pennies
    pennies_count_label["text"] = f"{coin_counts[1]}"

    # calculate net balance
    current_balance = int(balance_count_label["text"])
    current_balance += 1 * value
    balance_count_label["text"] = f"{current_balance}"

def increment_nickels():
    value = int(lbl_value["text"])

    # increment the count of pennies by value
    coin_counts[5] += value

    # reset the text of pennies
    nickels_count_label["text"] = f"{coin_counts[5]}"

    # calculate net balance
    current_balance = int(balance_count_label["text"])
    current_balance += 5 * value
    balance_count_label["text"] = f"{current_balance}"

def increment_dimes():
    value = int(lbl_value["text"])

    # increment the count of pennies by value
    coin_counts[10] += value

    # reset the text of pennies
    dimes_count_label["text"] = f"{coin_counts[10]}"

    # calculate net balance
    current_balance = int(balance_count_label["text"])
    current_balance += 10 * value
    balance_count_label["text"] = f"{current_balance}"

def increment_quarters():
    value = int(lbl_value["text"])

    # increment the count of pennies by value
    coin_counts[25] += value

    # reset the text of pennies
    quarters_count_label["text"] = f"{coin_counts[25]}"

    # calculate net balance
    current_balance = int(balance_count_label["text"])
    current_balance += 25 * value
    balance_count_label["text"] = f"{current_balance}"

def decrement_pennies():
    value = int(lbl_value["text"])

    if coin_counts[1] - value >= 0:
        # increment the count of pennies by value
        coin_counts[1] -= value

        # reset the text of pennies
        pennies_count_label["text"] = f"{coin_counts[1]}"

        # calculate net balance
        current_balance = int(balance_count_label["text"])
        current_balance -= 1 * value
        balance_count_label["text"] = f"{current_balance}"


def decrement_nickels():
    value = int(lbl_value["text"])

    if coin_counts[5] - value >= 0:
        # increment the count of pennies by value
        coin_counts[5] -= value

        # reset the text of pennies
        nickels_count_label["text"] = f"{coin_counts[5]}"

        # calculate net balance
        current_balance = int(balance_count_label["text"])
        current_balance -= 5 * value
        balance_count_label["text"] = f"{current_balance}"

def decrement_dimes():
    value = int(lbl_value["text"])

    if coin_counts[10] - value >= 0:
        # increment the count of pennies by value
        coin_counts[10] -= value

        # reset the text of pennies
        dimes_count_label["text"] = f"{coin_counts[10]}"

        # calculate net balance
        current_balance = int(balance_count_label["text"])
        current_balance -= 10 * value
        balance_count_label["text"] = f"{current_balance}"

def decrement_quarters():
    value = int(lbl_value["text"])

    if coin_counts[25] - value >= 0:
        # increment the count of pennies by value
        coin_counts[25] -= value

        # reset the text of pennies
        quarters_count_label["text"] = f"{coin_counts[25]}"

        # calculate net balance
        current_balance = int(balance_count_label["text"])
        current_balance -= 25 * value
        balance_count_label["text"] = f"{current_balance}"

def give_min_coins():
    amount = int(amount_entry.get())
    dp = [amount + 1] * (amount + 1)

    # dp[0] is fewest number of coins we need to make up 0 cents, which is 0 coins 
    dp[0] = 0

    for i in range(1, len(dp)):
        for coin_amount in coin_counts:
            if coin_amount <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin_amount])

    if dp[amount] != (amount + 1):
        second_label["text"] = str(dp[amount])
    else:
        second_label["text"] = "-1"

def get_coin_combinations():
    # get the length of 
    min_coins_needed = second_label["text"]
    
coin_counts = {
    1: 0,    # Pennies
    5: 0,    # Nickels
    10: 0,   # Dimes
    25: 0    # Quarters
}

window = tk.Tk()

# Set the title of the window
window.title("Coin it!")

# Set the color of the window to thistle
window.configure(background="thistle")

window.columnconfigure(0, weight=1)
window.rowconfigure([0,1,2,3], weight=1)
# header frame
header_frame = tk.Frame(window, background="thistle")
header_frame.grid(row=0, column=0, padx=10, pady=10)

# Create a label for the header with the title of the app
header_label = tk.Label(header_frame, bg="thistle", text="Coin it!", font=("Arial", 24,  "italic"), fg="gold")
header_label.grid(row=0,column=0, padx=5, pady=5)

# Top Frame
top_frame = tk.Frame(window, bg="thistle")
top_frame.grid(row=1, column=0, padx=10, pady=10)

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
bottom_frame = tk.Frame(window, bg="thistle")
bottom_frame.grid(row=2, column=0, padx=10, pady=10)

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
btn_increase = tk.Button(bottom_frame, text="+", command=increase)
btn_increase.grid(row=0, column=1, padx=5, pady=5)

lbl_value = tk.Label(bottom_frame, text="0")
lbl_value.grid(row=0, column=2, padx=5, pady=5)

btn_decrease = tk.Button(bottom_frame, text="-", command=decrease)
btn_decrease.grid(row=0, column=3, padx=5, pady=5)

# plus_nickels_button = tk.Button(bottom_frame, text="+", command=increment_nickels)
# plus_nickels_button.grid(row=1, column=1, padx=5, pady=5)

# # labels_nickels = tk.Label(bottom_frame, text="0")
# # labels_nickels.grid(row=1, column=2, padx=5, pady=5)

# minus_nickels_button = tk.Button(bottom_frame, text="-", command=decrement_nickels)
# minus_nickels_button.grid(row=1, column=3, padx=5, pady=5)

# plus_dimes_button = tk.Button(bottom_frame, text="+", command=increment_dimes)
# plus_dimes_button.grid(row=2, column=1, padx=5, pady=5)

# # labels_dimes = tk.Label(bottom_frame, text="0")
# # labels_dimes.grid(row=2, column=2, padx=5, pady=5)

# minus_dimes_button = tk.Button(bottom_frame, text="-", command=decrement_dimes)
# minus_dimes_button.grid(row=2, column=3, padx=5, pady=5)

# plus_quarters_button = tk.Button(bottom_frame, text="+", command=increment_quarters)
# plus_quarters_button.grid(row=3, column=1, padx=5, pady=5)

# # labels_quarters = tk.Label(bottom_frame, text="0")
# # labels_quarters.grid(row=3, column=2, padx=5, pady=5)

# minus_quarters_button = tk.Button(bottom_frame, text="-", command=decrement_quarters)
# minus_quarters_button.grid(row=3, column=3, padx=5, pady=5)

# Take Button Column
take_pennies_button = tk.Button(bottom_frame, text="Take Pennies", command=decrement_pennies)
take_pennies_button.grid(row=0, column=4, padx=5, pady=5)

take_nickels_button = tk.Button(bottom_frame, text="Take Nickels", command=decrement_nickels)
take_nickels_button.grid(row=1, column=4, padx=5, pady=5)

take_dimes_button = tk.Button(bottom_frame, text="Take Dimes", command=decrement_dimes)
take_dimes_button.grid(row=2, column=4, padx=5, pady=5)

take_quarters_button = tk.Button(bottom_frame, text="Take Quarters", command=decrement_quarters)
take_quarters_button.grid(row=3, column=4, padx=5, pady=5)

summary_frame = tk.Frame(window, bg="thistle")
summary_frame.grid(row=3, column=0, padx=10, pady=10)

first_label = tk.Label(summary_frame, text="You need min. of")
second_label = tk.Label(summary_frame, text="0")
min_coins_label = tk.Label(summary_frame, text="coins to make ")
amount_entry = tk.Entry(summary_frame, width=5, justify="center")
third_label = tk.Label(summary_frame, text="cents.")
give_min_coins_btn = tk.Button(summary_frame, text="Enter", command=give_min_coins)

first_label.grid(row=0, column=0)
second_label.grid(row=0, column=1)
min_coins_label.grid(row=0, column=2)
amount_entry.grid(row=0, column=3)
third_label.grid(row=0, column=4)
give_min_coins_btn.grid(row=0, column=5)

window.mainloop()