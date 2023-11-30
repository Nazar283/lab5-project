"""
Створити клас Sneakers (brand, size, color, price, quantity, material, numberOfSales, etc).
Додати клас SportShoesStore, який містить асортимент кросівок.
Реалізувати методи для сортування взуття за ціною і кількістю та можливість вивести топ
найпопулярніших кросівок.
"""


class Sneakers:
    """
    A class representing a pair of sneakers.
    """

    def __init__(self, brand, size, color, price, quantity, material, number_of_sales):
        self.__brand = brand
        self.__size = size
        self.__color = color
        self.price = price
        self.quantity = quantity
        self.__material = material
        self.number_of_sales = number_of_sales

    def __str__(self):
        return (f"{self.__brand} ({self.__color}, Size {self.__size}): ${self.price},"
                f" Available: {self.quantity}, Material: {self.__material},"
                f" Number of sales: {self.number_of_sales}")

    def sneakers_info(self):
        """
        Print information about the sneakers.
        """

        print(f"Brand: {self.__brand}")
        print(f"Color: {self.__color}")
        print(f"Size: {self.__size}")
        print(f"Price: {self.price}")
        print(f"Material: {self.__material}")


class SportShoesStore:
    """
    A class representing a sport shoes store.
    """

    def __init__(self):
        self.inventory = []

    def add_sneakers(self, sneakers):
        """
        Initialize a SportShoesStore instance.
        """

        self.inventory.append(sneakers)

    def sort_by_price(self):
        """
        Sort the inventory by the price of the sneakers.
        """

        self.inventory.sort(key=lambda x: x.price, reverse=True)

    def sort_by_quantity(self):
        """
        Sort the inventory by the quantity of the sneakers in reverse order.
        """

        self.inventory.sort(key=lambda x: x.quantity, reverse=True)

    def top_sellers(self, name):
        """
        Return the top N best-selling sneakers in the inventory.
        """

        top = sorted(self.inventory, key=lambda x: x.number_of_sales, reverse=True)[:name]
        return top


def main():
    """
    The main function that demonstrates the usage of the SportShoesStore and Sneakers classes.
    """

    store = SportShoesStore()
    sneaker1 = Sneakers("Nike", 10, "Red", 120, 65, "Leather", 140)
    sneaker2 = Sneakers("Adidas", 9, "Green", 90, 30, "Synthetic", 60)
    sneaker3 = Sneakers("Puma", 8, "White", 80, 40, "Mesh", 130)

    store.add_sneakers(sneaker1)
    store.add_sneakers(sneaker2)
    store.add_sneakers(sneaker3)

    print("Unsorted Inventory:")
    for sneaker in store.inventory:
        print(sneaker)

    store.sort_by_price()
    print("\nInventory Sorted by Price:")
    for sneaker in store.inventory:
        print(sneaker)

    store.sort_by_quantity()
    print("\nInventory Sorted by Quantity:")
    for sneaker in store.inventory:
        print(sneaker)

    top_sellers = store.top_sellers(2)
    print("\nTop 2 Best Sellers:")
    for sneaker in top_sellers:
        print(sneaker)


if __name__ == "__main__":
    main()
