from tkinter import *
import psycopg2


connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="your_database_password",  
    port=5432
)
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    item_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price INTEGER NOT NULL,
    total_price INTEGER NOT NULL
);
''')
connection.commit()

class cafe():
    def __init__(self, root):
        self.root = root
        self.root.title("WELCOME TO OUR CAFE")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        self.root.config(bg="#2c3e50")

        title = Label(self.root, text="BTECH CAFE", font=("Arial", 30, "bold"), bg="black", fg="white")
        title.pack(side=TOP, fill=X)

        self.menu = {
            "pizza": 900,
            "burger": 9,
            "mango shake": 100,
            "cola": 300,
            "kurkure": 5,
            "french fries": 50,
            "pasta": 40,
        }
        self.order_total = 0
        self.orders = []  
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.root, text="Welcome to our restaurant", font=("Arial", 20, "bold"), bg="#9bc8f5", fg="red")
        self.label.pack(pady=20)

        self.menu_label = Button(self.root, text="Menu 📋", command=self.menu_display, font=("Arial", 24, "bold"), bg="purple", fg="green", activebackground="red")
        self.menu_label.place(x=20, y=100)

        self.order_button = Button(self.root, text="Order Now", command=self.order_now, font=("Arial", 18), bg="white", fg="blue")
        self.order_button.place(x=self.width - 180, y=100)

        self.order_frame = Frame(self.root, bg="#2c3e50")
        self.order_frame.pack(fill=BOTH, expand=True, pady=20)

    def menu_display(self):
        self.menu_window = Toplevel(self.root)
        self.menu_window.title("Menu")
        self.menu_window.geometry("600x600")
        self.menu_window.config(bg="purple")

        menu_title = Label(self.menu_window, text="Menu  📋", font=("Arial", 24, "bold"), bg="red", fg="black")
        menu_title.pack(pady=10)

        for item, price in self.menu.items():
            item_label = Label(self.menu_window, text=f"{item.title()}: ₹{price}", font=("Arial", 18, "bold"), bg="purple", fg="black", bd=2)
            item_label.pack(pady=5)

    def order_now(self):
        for widget in self.order_frame.winfo_children():
            widget.destroy()

        order_title = Label(self.order_frame, text="Your Order", font=("Arial", 24, "bold"), bg="#2c3e50", fg="white")
        order_title.pack(pady=10)

        self.item_entry = Entry(self.order_frame, font=("Arial", 18), bg="#ecf0f1", fg="#2c3e50")
        self.item_entry.pack(pady=10)
        quantity=Label(self.order_frame, text="Enter Quantity:", font=("Arial", 18,"bold"), bg="#2c3e50", fg="white")
        quantity.pack(pady=5)
        self.quantity_entry = Entry(self.order_frame, font=("Arial", 18), bg="#ecf0f1", fg="#2c3e50")
        self.quantity_entry.pack(pady=10)
        self.quantity_entry.insert(0, "1")  

        confirm_button = Button(self.order_frame, text="Confirm Item", command=self.confirm_item, font=("Arial", 18), bg="#2c3e50", fg="white")
        confirm_button.pack(pady=10)

        add_another_button = Button(self.order_frame, text="Add Another Item", command=self.add_another_item, font=("Arial", 18), bg="#3498db", fg="white")
        add_another_button.pack(pady=10)

        cancel_button = Button(self.order_frame, text="Cancel Order", command=self.cancel, font=("Arial", 18), bg="#e74c3c", fg="white")
        cancel_button.pack(pady=10)

        self.total_label = Label(self.order_frame, text=f"Current Total: ₹{self.order_total}", font=("Arial", 20, "bold"), bg="#2c3e50", fg="white")
        self.total_label.pack(pady=10)

    def confirm_item(self):
        item_name = self.item_entry.get().strip().lower()
        quantity = int(self.quantity_entry.get().strip()) if self.quantity_entry.get().isdigit() else 1

        if item_name in self.menu:
            price = self.menu[item_name]
            total_price = price * quantity
            self.order_total += total_price
            self.orders.append((item_name, quantity, price, total_price))

            for widget in self.order_frame.winfo_children():
                if isinstance(widget, Label) and "Item added" in widget.cget("text"):
                    widget.destroy()

            order_label = Label(self.order_frame, text=f"Item added: {item_name.title()} (x{quantity}) - ₹{total_price}", font=("Arial", 18), bg="#2c3e50", fg="white")
            order_label.pack(pady=5)

            
            cursor.execute(
                "INSERT INTO orders (item_name, quantity, price, total_price) VALUES (%s, %s, %s, %s)",
                (item_name, quantity, price, total_price)
            )
            connection.commit()
        else:
            order_label = Label(self.order_frame, text=f"Item not available: {item_name.title()}", font=("Arial", 18), bg="#2c3e50", fg="red")
            order_label.pack(pady=5)

        self.total_label.config(text=f"Current Total: ₹{self.order_total}")

    def add_another_item(self):
        self.item_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.quantity_entry.insert(0, "1")  
        add_another_label = Label(self.order_frame, text="You can add another item now.", font=("Arial", 18), bg="#2c3e50", fg="yellow")
        add_another_label.pack(pady=5)

    def cancel(self):
        self.order_total = 0
        self.orders.clear()
        for widget in self.order_frame.winfo_children():
            widget.destroy()
        cancel_label = Label(self.order_frame, text="Order Cancelled", font=("Arial", 24, "bold"), bg="#2c3e50", fg="white")
        cancel_label.pack(pady=20)

root = Tk()
obj = cafe(root)
root.mainloop()
