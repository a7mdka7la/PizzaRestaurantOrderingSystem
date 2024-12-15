from abc import ABC, abstractmethod

# Singleton-style inventory tracker (probably overkill but works for now)
class InventoryManager:
    _instance = None
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return dict(self._inventory)  # Just to avoid accidental modifications


# Abstract base class for pizzas
class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


# Basic pizza types
class Margherita(Pizza):
    def get_description(self):
        return "Margherita"

    def get_cost(self):
        return 5.0


class Pepperoni(Pizza):
    def get_description(self):
        return "Pepperoni"

    def get_cost(self):
        return 6.0


# Topping decorator base class
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()


# Specific topping decorators
class Cheese(ToppingDecorator):
    def get_description(self):
        return f"{self.pizza.get_description()}, Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + 1.0


class Olives(ToppingDecorator):
    def get_description(self):
        return f"{self.pizza.get_description()}, Olives"

    def get_cost(self):
        return self.pizza.get_cost() + 0.5


class Mushrooms(ToppingDecorator):
    def get_description(self):
        return f"{self.pizza.get_description()}, Mushrooms"

    def get_cost(self):
        return self.pizza.get_cost() + 0.7


# Payment options (could be expanded later)
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using PayPal. Payment Successful!")


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using Credit Card. Payment Successful!")


# Main function to drive the application
def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")

    while True:
        print("\nChoose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => Exit")
        pizza_choice = input("Enter the number of your choice: ")
        
        if pizza_choice == '0':
            print("Thanks for visiting! See you next time!")
            break

        # Select pizza based on choice
        if pizza_choice == "1" and inventory_manager.check_and_decrement("Margherita"):
            pizza = Margherita()
        elif pizza_choice == "2" and inventory_manager.check_and_decrement("Pepperoni"):
            pizza = Pepperoni()
        else:
            print("Pizza unavailable or out of stock!")
            continue

        # Add toppings until the user finishes
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == "1" and inventory_manager.check_and_decrement("Cheese"):
                pizza = Cheese(pizza)
            elif topping_choice == "2" and inventory_manager.check_and_decrement("Olives"):
                pizza = Olives(pizza)
            elif topping_choice == "3" and inventory_manager.check_and_decrement("Mushrooms"):
                pizza = Mushrooms(pizza)
            elif topping_choice == "4":
                break
            else:
                print("Topping unavailable or out of stock!")

        # Show final order summary
        print("\nYour order summary:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        # Handle payment
        print("\nChoose payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")

        if payment_choice == "1":
            payment_method = PayPal()
        elif payment_choice == "2":
            payment_method = CreditCard()
        else:
            print("Invalid payment method! Please try again.")
            continue

        payment_method.pay(pizza.get_cost())
        
        print("\nUpdated Inventory:")
        print(inventory_manager.get_inventory())


if __name__ == "__main__":
    main()