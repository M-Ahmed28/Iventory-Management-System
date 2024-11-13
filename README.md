# Inventory Management System (IMS)

## Overview

The **Inventory Management System (IMS)** is a console-based application designed to help manage products and stock levels for a small business. It supports user authentication with two roles: **Admin** and **User**. The Admin has full access to manage products, while the User can only view and search the products.

## How to Use & Features

### Admin Login:
Admin will log in using the following credentials:

- **Username**: admin
- **Password**: adminpass

Once logged in, the Admin can manage products (add, edit, delete, view, search, filter by stock, and adjust stock).

### User Login:
Users will log in using the following credentials:

- **Username**: user1
- **Password**: userpass

Once logged in, Users can view and search for products only.

### Available Commands:

#### Admin Menu:
1. **Add Product**: Add a new product to the inventory.
2. **Edit Product**: Edit an existing product's details (name, category, price, stock).
3. **Delete Product**: Delete a product from the inventory.
4. **View Products**: View all products in the inventory.
5. **Search Products**: Search products by name or category.
6. **Filter by Stock**: Show products that are below a certain stock threshold.
7. **Adjust Stock (Restock/Reduce)**: Restock or reduce the stock for a specific product.
8. **Exit**: Exit the IMS system.

#### User Menu:
1. **View Products**: View all products in the inventory.
2. **Search Products**: Search for products by name or category.
3. **Exit**: Exit the IMS system.

### Example:


 #### Admin login:

👤 Username: admin
🔑 Password: adminpass
✅ Login successful! Welcome, admin!

🔧 Admin Menu
1. Add Product
2. Edit Product
3. Delete Product
4. View Products
5. Search Products
6. Filter by Stock
7. Adjust Stock (Restock/Reduce)
8. Exit
Enter your choice: 1

#### User login:


👤 Username: user1
🔑 Password: userpass
✅ Login successful! Welcome, user1!

#### User Menu:

👤 User Menu
1. View Products
2. Search Products
3. Exit
Enter your choice: 1

## Code Structure
ims.py: Main script that runs the IMS program.

Contains Product and Inventory classes to manage the products and their details.
Implements user authentication and menu-driven interface for Admin and User roles.
users: A dictionary containing demo user credentials:

Admin: admin / adminpass
User: user1 / userpass
Product class: Defines properties for a product like product_id, name, category, price, stock_quantity, and low_stock_threshold. It includes methods for restocking, reducing stock, and checking stock levels.

Inventory class: Manages a collection of products. Includes methods for adding, editing, deleting, viewing, searching, and filtering products based on stock.
