# User roles and credentials (for demo purposes)
users = {
    'admin': {'password': 'adminpass', 'role': 'Admin'},
    'user1': {'password': 'userpass', 'role': 'User'}
}

# Product class
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.product_id:<5} | {self.name:<15} | {self.category:<10} | ${self.price:<8} | Stock: {self.stock_quantity}"

# Inventory class
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("\n⚠️ Product ID already exists!\n")
        else:
            self.products[product.product_id] = product
            print("\n✅ Product added successfully!\n")

    def edit_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        product = self.products.get(product_id)
        if product:
            if name: product.name = name
            if category: product.category = category
            if price: product.price = price
            if stock_quantity: product.stock_quantity = stock_quantity
            print("\n✅ Product updated successfully!\n")
        else:
            print("\n⚠️ Product not found!\n")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("\n✅ Product deleted successfully!\n")
        else:
            print("\n⚠️ Product not found!\n")

    def view_products(self):
        if not self.products:
            print("\n📦 No products available.\n")
            return
        print("\n📦 Inventory:\n")
        print(f"{'ID':<5} | {'Name':<15} | {'Category':<10} | {'Price':<8} | {'Stock'}")
        print("-" * 50)
        for product in self.products.values():
            print(product)

    def search_product(self, keyword):
        try:
            if keyword.isdigit():  # Check if the keyword is numeric (ID search)
                product_id = int(keyword)
                product = self.products.get(product_id)
                if product:
                    print("\n🔍 Search Results:\n")
                    print(product)
                else:
                    print("\n🔍 No products found with the given ID.\n")
            else:  # Perform name-based search
                found = [product for product in self.products.values() if keyword.lower() in product.name.lower()]
                if not found:
                    print("\n🔍 No products found with the given name.\n")
                else:
                    print("\n🔍 Search Results:\n")
                    for product in found:
                        print(product)
        except Exception as e:
            print(f"\n❌ Error: {e}\n")

    def filter_by_stock(self, threshold):
        filtered = [product for product in self.products.values() if product.stock_quantity <= threshold]
        if not filtered:
            print("\n🔻 No products below threshold.\n")
        else:
            print("\n🔻 Low Stock Products:\n")
            for product in filtered:
                print(product)

# Login function
def login():
    username = input("👤 Username: ")
    password = input("🔑 Password: ")
    user = users.get(username)
    if user and user['password'] == password:
        print(f"\n✅ Login successful! Welcome, {username}!\n")
        return user['role']
    else:
        print("\n❌ Invalid credentials.\n")
        return None

# Main Program
def main():
    print("=" * 50)
    print("💼 Welcome to the Inventory Management System (IMS) 💼")
    print("=" * 50)

    inventory = Inventory()

    role = None
    while not role:
        role = login()

    while True:
        if role == "Admin":
            print("\n🔧 Admin Menu")
            print("1. Add Product")
            print("2. Edit Product")
            print("3. Delete Product")
            print("4. View Products")
            print("5. Search Products")
            print("6. Filter by Stock")
            print("7. Exit")
            choice = input("\nEnter your choice: ")

            match choice:
                case "1":
                    try:
                        product_id = int(input("Product ID: "))
                        name = input("Name: ")
                        category = input("Category: ")
                        price = float(input("Price: "))
                        stock_quantity = int(input("Stock Quantity: "))
                        inventory.add_product(Product(product_id, name, category, price, stock_quantity))
                    except Exception as e:
                        print(f"\n❌ Error: {e}\n")

                case "2":
                    try:
                        product_id = int(input("Product ID to edit: "))
                        name = input("New Name (leave blank to skip): ") or None
                        category = input("New Category (leave blank to skip): ") or None
                        price = input("New Price (leave blank to skip): ")
                        stock_quantity = input("New Stock Quantity (leave blank to skip): ")
                        inventory.edit_product(product_id, name, category, float(price) if price else None, int(stock_quantity) if stock_quantity else None)
                    except Exception as e:
                        print(f"\n❌ Error: {e}\n")

                case "3":
                    try:
                        product_id = int(input("Product ID to delete: "))
                        inventory.delete_product(product_id)
                    except Exception as e:
                        print(f"\n❌ Error: {e}\n")

                case "4":
                    inventory.view_products()

                case "5":
                    keyword = input("Enter product name or ID to search: ")
                    inventory.search_product(keyword)

                case "6":
                    try:
                        threshold = int(input("Enter stock threshold: "))
                        inventory.filter_by_stock(threshold)
                    except Exception as e:
                        print(f"\n❌ Error: {e}\n")

                case "7":
                    print("\n👋 Exiting IMS. Goodbye!")
                    break

                case _:
                    print("\n❌ Invalid choice. Please try again.\n")

        elif role == "User":
            print("\n👤 User Menu")
            print("1. View Products")
            print("2. Search Products")
            print("3. Exit")
            choice = input("\nEnter your choice: ")

            match choice:
                case "1":
                    inventory.view_products()

                case "2":
                    keyword = input("Enter product name or ID to search: ")
                    inventory.search_product(keyword)

                case "3":
                    print("\n👋 Exiting IMS. Goodbye!")
                    break

                case _:
                    print("\n❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
