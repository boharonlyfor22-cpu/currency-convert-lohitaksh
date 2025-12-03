import tkinter as tk
from tkinter import ttk, messagebox

class SimpleCurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Currency Converter")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        style = ttk.Style(self.root)
        style.theme_use('clam')

        # Variables
        self.from_currency = tk.StringVar()
        self.to_currency = tk.StringVar()
        self.amount = tk.StringVar()
        self.result = tk.StringVar()

        # Hard-coded exchange rates relative to USD
        # (1 USD = x units of currency)
        self.rates = {
            "USD": 1.0,
            "EUR": 0.92,
            "INR": 83.5,
            "GBP": 0.80,
            "JPY": 156.0,
            "AUD": 1.51,
            "CAD": 1.37
        }

        self._build_ui()

    def _build_ui(self):
        padding = {'padx': 10, 'pady': 10}

        ttk.Label(self.root, text="Amount:").grid(column=0, row=0, **padding)
        ttk.Entry(self.root, textvariable=self.amount).grid(column=1, row=0, **padding)

        ttk.Label(self.root, text="From:").grid(column=0, row=1, **padding)
        from_cb = ttk.Combobox(self.root, textvariable=self.from_currency, state="readonly")
        from_cb['values'] = list(self.rates.keys())
        from_cb.grid(column=1, row=1, **padding)
        from_cb.current(0)

        ttk.Label(self.root, text="To:").grid(column=0, row=2, **padding)
        to_cb = ttk.Combobox(self.root, textvariable=self.to_currency, state="readonly")
        to_cb['values'] = list(self.rates.keys())
        to_cb.grid(column=1, row=2, **padding)
        to_cb.current(1)

        convert_btn = ttk.Button(self.root, text="Convert", command=self.convert)
        convert_btn.grid(column=0, row=3, columnspan=2, **padding)

        ttk.Label(self.root, textvariable=self.result, font=('Arial', 12, 'bold')).grid(column=0, row=4, columnspan=2)

    def convert(self):
        try:
            amount = float(self.amount.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number")
            return

        frm = self.from_currency.get()
        to = self.to_currency.get()

        # Convert via USD as base
        try:
            amount_in_usd = amount / self.rates[frm]
            converted = amount_in_usd * self.rates[to]
        except KeyError:
            messagebox.showerror("Error", "Unsupported currency")
            return

        self.result.set(f"{amount:.2f} {frm} = {converted:.2f} {to}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCurrencyConverter(root)
    root.mainloop()
