
class Sneakers:
    def __init__(self, brand, size, color, price, quantity, material, numberOfSales):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.material = material
        self.numberOfSales = numberOfSales

    def __str__(self):
        return f"{self.brand} ({self.color}, Size {self.size}): ${self.price}, Available: {self.quantity}"

class SportShoesStore:
    def __init__(self):
        self.inventory = []

    def add_sneakers(self, sneakers):
        self.inventory.append(sneakers)

    def sort_by_price(self):
        self.inventory.sort(key=lambda x: x.price)

    def sort_by_quantity(self):
        self.inventory.sort(key=lambda x: x.quantity, reverse=True)

    def top_sellers(self, n):
        top = sorted(self.inventory, key=lambda x: x.numberOfSales, reverse=True)[:n]
        return top

def main():
    store = SportShoesStore()
    sneaker1 = Sneakers("Nike", 10, "Red", 120, 65, "Leather", 140)
    sneaker2 = Sneakers("Adidas", 9, "Green", 90, 30, "Synthetic", 60)
    sneaker3 = Sneakers("Puma", 8, "White", 80, 40, "Mesh", 130)

    store.add_sneakers(sneaker1)
    store.add_sneakers(sneaker2)
    store.add_sneakers(sneaker3)

    print("Unsorted Inventory:") #інвентар магазину кросівок
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