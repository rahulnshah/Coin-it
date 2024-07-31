import tkinter as tk
import redis

class CoinApp(tk.Tk):
    # Class-level Redis client
    redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def __init__(self):
        super().__init__()
        self.title("Coin it!")
        self.configure(background="thistle")

        self.create_widgets()

    def create_widgets(self):
        # Header Frame
        self.header_frame = tk.Frame(self, background="thistle")
        self.header_frame.grid(row=0, column=0, padx=10, pady=10)
        self.header_label = tk.Label(self.header_frame, bg="thistle", text="Coin it!", font=("Arial", 24, "italic"), fg="gold")
        self.header_label.grid(row=0, column=0, padx=5, pady=5)

        # Top Frame
        self.top_frame = tk.Frame(self, bg="thistle")
        self.top_frame.grid(row=1, column=0, padx=10, pady=10)

        coin_labels = ["Pennies", "Nickels", "Dimes", "Quarters", "Net Balance"]
        self.coin_counts = ["pennies", "nickels", "dimes", "quarters"]
        self.coin_values = [1, 5, 10, 25]

        self.count_labels = {}
        for i, label in enumerate(coin_labels):
            tk.Label(self.top_frame, text=label).grid(row=i, column=0, padx=5, pady=5)
            if label != "Net Balance":
                count = self.get_coin_count(self.coin_counts[i])
                self.count_labels[self.coin_counts[i]] = tk.Label(self.top_frame, text=f"{count}")
                self.count_labels[self.coin_counts[i]].grid(row=i, column=1, padx=5, pady=5)
            else:
                self.balance_label = tk.Label(self.top_frame, text=f"{self.get_total_balance()}")
                self.balance_label.grid(row=i, column=1, padx=5, pady=5)

        # Bottom Frame
        self.bottom_frame = tk.Frame(self, bg="thistle")
        self.bottom_frame.grid(row=2, column=0, padx=10, pady=10)

        for i, coin in enumerate(self.coin_counts):
            tk.Button(self.bottom_frame, text=f"Add {coin.capitalize()}", command=lambda c=coin: self.increment_coin(c)).grid(row=i, column=0, padx=5, pady=5)
            tk.Button(self.bottom_frame, text=f"Take {coin.capitalize()}", command=lambda c=coin: self.decrement_coin(c)).grid(row=i, column=4, padx=5, pady=5)

        self.value_label = tk.Label(self.bottom_frame, text="0")
        self.value_label.grid(row=0, column=2, padx=5, pady=5)
        tk.Button(self.bottom_frame, text="+", command=self.increase).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.bottom_frame, text="-", command=self.decrease).grid(row=0, column=3, padx=5, pady=5)

        # Summary Frame
        self.summary_frame = tk.Frame(self, bg="thistle")
        self.summary_frame.grid(row=3, column=0, padx=10, pady=10)

        self.amount_entry = tk.Entry(self.summary_frame, width=5, justify="center")
        tk.Label(self.summary_frame, text="You need min. of").grid(row=0, column=0)
        self.min_coins_label = tk.Label(self.summary_frame, text="0")
        self.min_coins_label.grid(row=0, column=1)
        tk.Label(self.summary_frame, text="coins to make ").grid(row=0, column=2)
        self.amount_entry.grid(row=0, column=3)
        tk.Label(self.summary_frame, text="cents.").grid(row=0, column=4)
        tk.Button(self.summary_frame, text="Enter", command=self.give_min_coins).grid(row=0, column=5)

    def increase(self):
        value = int(self.value_label["text"])
        self.value_label["text"] = f"{value + 1}"

    def decrease(self):
        value = int(self.value_label["text"])
        if value > 0:
            self.value_label["text"] = f"{value - 1}"

    def get_coin_count(self, coin_type):
        count = CoinApp.redis_client.hget('user-session:123', coin_type)
        return int(count) if count else 0

    def get_total_balance(self):
        total_balance = 0
        for coin, value in zip(self.coin_counts, self.coin_values):
            total_balance += self.get_coin_count(coin) * value
        return total_balance

    def update_labels(self):
        for coin in self.coin_counts:
            self.count_labels[coin]["text"] = f"{self.get_coin_count(coin)}"
        self.balance_label["text"] = f"{self.get_total_balance()}"

    def increment_coin(self, coin_type):
        value = int(self.value_label["text"])
        CoinApp.redis_client.hincrby('user-session:123', coin_type, value)
        self.update_labels()

    def decrement_coin(self, coin_type):
        value = int(self.value_label["text"])
        current_count = self.get_coin_count(coin_type)
        if current_count >= value:
            CoinApp.redis_client.hincrby('user-session:123', coin_type, -value)
            self.update_labels()

    def give_min_coins(self):
        amount = int(self.amount_entry.get())
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        coin_counts = [1, 5, 10, 25]

        for i in range(1, len(dp)):
            for coin_amount in coin_counts:
                if coin_amount <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin_amount])

        if dp[amount] != (amount + 1):
            self.min_coins_label["text"] = str(dp[amount])
        else:
            self.min_coins_label["text"] = "-1"

if __name__ == "__main__":
    app = CoinApp()
    app.mainloop()