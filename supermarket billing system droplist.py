import tkinter as tk
from tkinter import messagebox
import random
import os

class SupermarketBilling:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket Billing System")
        self.root.geometry("850x600")
        self.root.config(bg="lightyellow")

        self.items = {
            'Rice': 40,
            'Wheat': 35,
            'Oil': 120,
            'Sugar': 45,
            'Milk': 25,
            'Soap': 30,
            'Shampoo': 90,
            'Toothpaste': 50,
        }

        self.cart = {}
        self.total_price = 0
        self.tax = 0
        self.final_amount = 0

        self.bill_no = str(random.randint(1000, 9999))

        # Frames
        self.title = tk.Label(self.root, text="Supermarket Billing System", font=("Arial", 20, "bold"), bg="orange", fg="white")
        self.title.pack(fill=tk.X)

        self.left_frame = tk.Frame(self.root, bg="lightyellow")
        self.left_frame.place(x=20, y=60, width=300, height=500)

        self.right_frame = tk.Frame(self.root, bg="lightblue")
        self.right_frame.place(x=340, y=60, width=480, height=500)

        # Left Frame - Product selection
        tk.Label(self.left_frame, text="Product", font=("Arial", 12, "bold"), bg="lightyellow").pack(pady=5)
        self.product_var = tk.StringVar()
        self.product_menu = tk.OptionMenu(self.left_frame, self.product_var, *self.items.keys())
        self.product_menu.config(width=20)
        self.product_menu.pack(pady=5)

        tk.Label(self.left_frame, text="Quantity", font=("Arial", 12, "bold"), bg="lightyellow").pack(pady=5)
        self.qty_entry = tk.Entry(self.left_frame, width=22)
        self.qty_entry.pack(pady=5)

        self.add_btn = tk.Button(self.left_frame, text="Add to Cart", bg="green", fg="white", command=self.add_to_cart)
        self.add_btn.pack(pady=10)

        self.clear_btn = tk.Button(self.left_frame, text="Clear Cart", bg="red", fg="white", command=self.clear_cart)
        self.clear_btn.pack(pady=5)

        self.save_btn = tk.Button(self.left_frame, text="Save Bill", bg="blue", fg="white", command=self.save_bill)
        self.save_btn.pack(pady=5)

        # Right Frame - Bill area
        self.text_area = tk.Text(self.right_frame, font=("Courier", 10), wrap="word")
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.display_bill_header()

    def display_bill_header(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"\tABC Supermarket\n")
        self.text_area.insert(tk.END, f"Bill No: {self.bill_no}\n")
        self.text_area.insert(tk.END, f"{'-'*40}\n")
        self.text_area.insert(tk.END, f"{'Product':20}{'Qty':>5}{'Price':>10}\n")
        self.text_area.insert(tk.END, f"{'-'*40}\n")

    def add_to_cart(self):
        product = self.product_var.get()
        qty = self.qty_entry.get()

        if product == "" or qty == "":
            messagebox.showwarning("Input Error", "Please select product and enter quantity.")
            return

        try:
            qty = int(qty)
            price = self.items[product] * qty
            self.cart[product] = self.cart.get(product, 0) + qty
            self.total_price += price

            self.display_bill_header()
            for p, q in self.cart.items():
                p_price = self.items[p] * q
                self.text_area.insert(tk.END, f"{p:20}{q:>5}{p_price:>10.2f}\n")

            self.tax = round(self.total_price * 0.05, 2)
            self.final_amount = round(self.total_price + self.tax, 2)

            self.text_area.insert(tk.END, f"{'-'*40}\n")
            self.text_area.insert(tk.END, f"{'Subtotal':25}{self.total_price:>10.2f}\n")
            self.text_area.insert(tk.END, f"{'GST (5%)':25}{self.tax:>10.2f}\n")
            self.text_area.insert(tk.END, f"{'Total':25}{self.final_amount:>10.2f}\n")

            self.qty_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Invalid Quantity", "Please enter a valid number.")

    def clear_cart(self):
        self.cart.clear()
        self.total_price = 0
        self.tax = 0
        self.final_amount = 0
        self.display_bill_header()

    def save_bill(self):
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Cannot save an empty bill.")
            return

        bill_data = self.text_area.get(1.0, tk.END)
        folder = "saved_bills"
        os.makedirs(folder, exist_ok=True)
        filename = os.path.join(folder, f"bill_{self.bill_no}.txt")
        with open(filename, "w") as f:
            f.write(bill_data)

        messagebox.showinfo("Bill Saved", f"Bill saved as {filename}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SupermarketBilling(root)
    root.mainloop()
