class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_price(self, item):
        return self.items.get(item, None)

    def update_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price


# Создаем несколько магазинов
store1 = Store("Магазин 1", "Улица Ленина, 15")
store2 = Store("Магазин 2", "Улица Мира, 22")
store3 = Store("Магазин 3", "Улица Пушкина, 38")