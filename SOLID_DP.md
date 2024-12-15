More that this, there are the SOLID Principles and Design Patterns, whereby the application that has been developed to address the pizza restaurant ordering system includes the following.

## 1. Singleton Patternt – InventoryManager

### SOLID Principles Addressed:
**S - Single Responsibility Principle:**
- **How:** It also makes the `InventoryManager` be the heavy-lifting regarding the inventory system while keeping none of the other classes managing it.

**O - Open/Closed Principle:**
- **How:** Despite this fact that the class is not open for extension, it is closed for modification because the structure of inventory and the logic that controls the access are centralized.

**Code Snippet:**
```python
class InventoryManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = objects.ContainerConfiguration(*args, **kwargs)
        return cls._instance
```

---

## 2. In this case, we have Topping Decorators under the Decorator Pattern.

### SOLID Principles Addressed:
**O - Open/Closed Principle:**
- **How:** New toppings can be added in the system without extending the existing classes which means the application is open for extension but closed for modification.

**L - Liskov Substitution Principle:**
- **How:** All topping decorators are independent classes of the base pizza class which can be substituted by each other.

**Code Snippet:**
```python
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.getdescription()

    def get_cost(self):
        return self.pizza.get_cost()
```

---

## 3. Payment Methods Strategy that will be implemented will be the strategy Pattern.

### SOLID Principles Addressed:
**O - Open/Closed Principle:**
- **How:** New payment methods may be introduced in the payment gateway, without affecting the prior developed logics.

**I - Interface Segregation Principle:**
- **How:** Each payment method forms the `PaymentMethod` interface to have focused interfaces.

**D - Dependency Inversion Principle:**
- **How:** As pointed out the application’s main dependency is actually the `PaymentMethod` abstraction and not these implementations.

**Code Snippet:**
```python
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using PayPal.")
```

