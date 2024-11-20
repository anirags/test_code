# Script: Shopping Cart System

class ShoppingCart:
    def __init__(self):
        self.items = {}  # Stores items as {item_name: quantity}

    def add_item(self, item_name, quantity):
        """
        Adds an item to the cart with the specified quantity.
        """
        if quantity <= 0:
            print("Error: Quantity must be positive.")
            return
        
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        """
        Removes the specified quantity of an item from the cart.
        """
        if item_name not in self.items:
            print(f"Error: {item_name} is not in the cart.")
            return
        
        if quantity <= 0:
            print("Error: Quantity must be positive.")
            return
        
        if self.items[item_name] < quantity:
            print(f"Error: Cannot remove {quantity} {item_name}(s). Only {self.items[item_name]} in cart.")
            return

        self.items[item_name] -= quantity
        if self.items[item_name] == 0:
            del self.items[item_name]

    def view_cart(self):
        """
        Displays all items in the cart.
        """
        if not self.items:
            print("Your cart is empty.")
            return
        
        print("Items in your cart:")
        for item, quantity in self.items.items():
            print(f"- {item}: {quantity}")

    def calculate_total(self, price_list):
        """
        Calculates the total cost of items in the cart.
        """
        total = 0
        for item, quantity in self.items.items():
            if item in price_list:
                total += price_list[item] * quantity
            else:
                print(f"Warning: Price for {item} is not available.")
        
        return total


def main():
    """
    Main function to interact with the shopping cart system.
    """
    cart = ShoppingCart()
    price_list = {
        "apple": 1.0,
        "banana": 0.5,
        "orange": 0.75,
        "milk": 2.5
    }
    
    print("Welcome to the Shopping Cart System!")
    print("Available commands: add, remove, view, total, exit")

    while True:
        command = input("\nEnter a command: ").strip().lower()
        if command == "exit":
            print("Exiting the shopping cart system. Goodbye!")
            break
        
        if command == "add":
            item = input("Enter the item name: ").strip().lower()
            try:
                quantity = int(input("Enter the quantity: ").strip())
                cart.add_item(item, quantity)
            except ValueError:
                print("Error: Quantity must be an integer.")
        
        elif command == "remove":
            item = input("Enter the item name: ").strip().lower()
            try:
                quantity = int(input("Enter the quantity to remove: ").strip())
                cart.remove_item(item, quantity)
            except ValueError:
                print("Error: Quantity must be an integer.")
        
        elif command == "view":
            cart.view_cart()
        
        elif command == "total":
            total = cart.calculate_total(price_list)
            print(f"The total cost of your cart is: ${total:.2f}")
        
        else:
            print("Error: Unknown command. Please try again.")


if __name__ == "__main__":
    main()
