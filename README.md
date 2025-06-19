# 🏋️☕ Cafe Management System

Welcome to the **Cafe Management System**! This project is a GUI-based application designed to streamline the operations of a cafe by providing an easy-to-use interface for menu browsing, order placement, and order management.

## 🌐 Key Features

### 1. **🔧 Graphical User Interface (GUI)**

* A welcoming and user-friendly design.
* The main interface displays the title **"WELCOME TO OUR CAFE"**.
* A navigation bar to access the menu or begin placing orders.

### 2. **🍽️ Menu Management**

* Separate "Menu" window displaying available items and their respective prices.
* Predefined menu items for quick and easy browsing.

### 3. **🚪 Order Management**

* Input item names and quantities to place orders.
* Automatic calculation of total price for each item based on quantity.
* Dynamic display of the running total for the order.

### 4. **📊 Database Integration**

* Connects to a PostgreSQL database for order management.
* Automatically creates an `orders` table if it doesn’t already exist.
* Saves detailed order information, including item name, quantity, price, and total price.

### 5. **🔄 Interactive Features**

* **Confirm Item:** Add an item to the order and update the total cost.
* **Add Another Item:** Continue adding items to the order.
* **Cancel Order:** Reset the order and clear all data from the GUI.
* Feedback messages notify users of actions (e.g., confirming items or alerting when an item is unavailable).

### 6. **🛏️ Dynamic Window Management**

* Separate windows for the "Menu" and "Order" interfaces to ensure better organization.

## 💡 Technical Details

### Frontend

* Built using Python’s **Tkinter** library.
* Layouts designed with frames, labels, buttons, and entry fields.
* Carefully chosen colors and fonts for a visually appealing experience.

### Backend

* **PostgreSQL** database used to store order details.
* SQL commands executed using the **psycopg2** library.

### Menu Items

* Hardcoded in a Python dictionary with item names and corresponding prices.

### Order Handling

* Validates user input to ensure items exist in the menu.
* Stores order data both in memory and in the database.

## 💡 How It Works

1. **View the Menu:**

   * Navigate to the "Menu" window to see available items and their prices.
2. **Place an Order:**

   * Enter the item name and quantity.
   * Confirm the item to add it to your order.
   * Continue adding items or finalize the order.
3. **Manage Orders:**

   * Reset or cancel the order if needed.
   * View a dynamically updated total cost.

## 🎨 Project Outcome

Here is a snapshot of the project in action:
![Cafe Management System Interface](https://github.com/user-attachments/assets/1eef43c3-228c-412b-bf89-4cf3e36b6a74)

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* PostgreSQL database
* Required Python libraries:

  * `tkinter`
  * `psycopg2`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/cafe-management-system.git
   ```
2. Navigate to the project directory:

   ```bash
   cd cafe-management-system
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Configure the database connection in the script.

### Running the Application

Start the application using:

```bash
python main.py
```

## 🌟 Contribution Guidelines

We welcome contributions! Feel free to open issues or submit pull requests to improve the application.

## 🔒 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🎉 Acknowledgments

* Special thanks to the developers and maintainers of **Tkinter** and **psycopg2**.
* Thanks to the open-source community for inspiring this project.

---

Enjoy managing your cafe effortlessly with the **Cafe Management System**! 🍵
