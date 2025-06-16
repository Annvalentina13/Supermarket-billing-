# 🛒 Supermarket Billing System

A fully functional **Supermarket Billing System** built using Python's `tkinter` library. This simple desktop application allows supermarket staff to quickly generate customer bills by selecting products, calculating totals, applying tax, and saving bills for record-keeping.

---

## 📌 Key Features

✅ Easy-to-use GUI interface using Tkinter  
✅ Pre-defined product catalog with item-wise pricing  
✅ Add items to cart with quantity management  
✅ Automatic calculation of:
- Subtotal
- GST (5% tax)
- Final total amount  
✅ Generate unique Bill numbers automatically  
✅ Save bills as text files for future reference  
✅ Simple, lightweight & easy to modify

---

## 🎯 Functional Workflow

1. Select product from dropdown.
2. Enter quantity for the selected product.
3. Click `Add to Cart` to add the item.
4. The bill gets updated dynamically.
5. View Subtotal, Tax, and Final Amount.
6. Save the generated bill as a text file.
7. Start a new billing session with `Clear Cart`.

---

## 🖥️ Tech Stack

| Technology | Purpose       |
|-------------|----------------|
| Python 3.x  | Core programming |
| Tkinter     | GUI framework |
| OS Module   | File operations |
| Random Module | Auto-generate bill numbers |

---

## supermarket-billing-system/
- │
- ├── supermarket_billing.py   # Main application code
- ├── saved_bills/             # Folder where generated bills are saved (created automatically)
- └── README.md                # Project documentation
