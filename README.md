# Cafe-Management-system
This program is a GUI-based cafe management application built using Python's Tkinter library for the frontend and PostgreSQL as the backend database. The application allows users to view a menu, place orders, and manage those orders. Below is an overview of its functionality:

Key Features:
Graphical User Interface (GUI):

The main interface has a welcoming design, displaying the title "WELCOME TO OUR CAFE."

A navigation bar provides options to view the menu or start ordering.

Menu Management:

A separate "Menu" window lists available items with their respective prices.

The menu items are pre-defined in the application.

Order Management:

Users can input item names and quantities to place orders.

The application calculates the total price of each item based on its quantity.

A running total of the order is displayed dynamically.

Database Integration:

The app connects to a PostgreSQL database and creates an orders table if it does not already exist.

Each order is saved to the database with details like item name, quantity, price, and total price.

Interactive Features:

Confirm Item: Adds an item to the order and updates the total cost.

Add Another Item: Allows users to continue adding items to their order.

Cancel Order: Resets the order, clearing all data from the GUI.

Feedback and Notifications:

The app provides feedback messages, such as confirming the addition of items or notifying the user if an item is unavailable.

Dynamic Window Management:

The "Menu" and "Order" interfaces are separate windows for better organization.

Technical Details:
Frontend:

Tkinter is used for building the GUI.

Layouts are designed using frames, labels, buttons, and entry fields.

Colors and fonts are chosen to create a visually appealing experience.

Backend:

PostgreSQL is used for storing order details.

SQL commands are executed using the psycopg2 library.

Menu Items:

Hardcoded menu items with corresponding prices are stored in a Python dictionary.

Order Handling:

The program validates user input to check if items are available in the menu.

Data for each order is stored both in memory and in the database.
Here is the outcome of the project

![Screenshot from 2025-06-15 09-33-37](https://github.com/user-attachments/assets/1eef43c3-228c-412b-bf89-4cf3e36b6a74)
