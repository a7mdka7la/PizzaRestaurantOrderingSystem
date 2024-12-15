## Current components of the personnel computer ordered by level of technical familiarity

## 1. Singleton Pattern
### Description:
The Singleton Centralizes the control of an object and makes sure that there is only one instance of the class in the system.

### Application:
We implemented the Singleton design pattern in the `InventoryManager` class to created only a single instance in the whole system.

### Before Applying the Pattern:
When we wanted to make a check or change in inventory we had to create a new instance of `InventoryManager` and thus we had inconsistent system and data.

### Improvements:
– Efficient storage of stock in a central base of operation for a business.
In this context it helps to avoid multiple instances of the object.
- It sustains consistency of inventory state.


### Code Snippet:
```python
class InventoryManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
```

---

## 2. Decorator Pattern
### Description:
The Decorator pattern deals with adding more functionalities or tasks to the objects at runtime without modifying them.

### Application:
Thin topping layers were achieved by the use of Decorator pattern. Every topping such as `Cheese`, `Olives` and `Mushrooms` is a layer implemented as a decorator class.

### Before Applying the Pattern:
The pizza class had one method for each combination of pizza-topping, the end result was code redundancy, and poor organization.

### Improvements:
- Dynamically adds toppings.
- Reduces complexity.
One of the component objectives this improves is flexibility and scalability of an organization.


### Code Snippet:
```python
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()
```

---

## 3. Strategy Pattern
### Description:
The Strategy pattern identifies an interface for a family of algorithms, embodies each of them, and allows them to be substituted for one another.

### Application:
We tested our implementation of the Strategy pattern for the payment methods to provide flexibility in the choice of payment strategies.

### Before Applying the Pattern:
In terms of payment logic, it was a hard coded in the main function and thus expansion in the future was not very possible.

### Improvements:
- Reduction of payment procedures.
It has affordable cost than using third party provider and Improved extensibility for adding new payment method.

### Code Snippet:
```python
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using PayPal.")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using Credit Card.")
```

---

## Meaning of Over-Engineering
### Description:
Over design is a process where a system or component is provided with more capacity or/and numbers of features than are actually necessary at the present time.

### Example in the Pizza Restaurant System:
Ungrounded design patterns like creating a Factory pattern only for making pizzas would only give the system a new layer of complications.


### Code Snippet (Over-Engineered Example):
```python
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "Margherita":
            return Margherita()
        elif pizza_type == "Pepperoni":
            return Pepperoni()
        else:
            raise ValueError("Invalid Pizza Type")
```

### Why This is Over-Engineering:
The preparation of pizzas is an easy process as follows.
Direct instantiation of pizzas is much more expressive and shorter.

In the designing of the pizza ordering system, we did not over-complicate things as this was a way of achieving optimal flexibility.

