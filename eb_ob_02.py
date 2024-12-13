class Store:
    def __init__(self, name, address):
        """
        Инициализация магазина.

        :param name: Название магазина
        :param address: Адрес магазина
        """
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавить товар в ассортимент.

        :param item_name: Название товара
        :param price: Цена товара
        """
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удалить товар из ассортимента.

        :param item_name: Название товара
        """
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Получить цену товара по его названию.

        :param item_name: Название товара
        :return: Цена товара или None, если товара нет
        """
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        """Обновить цену товара.

        :param item_name: Название товара
        :param new_price: Новая цена товара
        """
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        """Возвращает строковое представление магазина."""
        return f"{self.name} (Адрес: {self.address})"

# Создание объектов класса Store
store1 = Store("Фруктовый Рай", "ул. Ленина, 10")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store1.add_item("oranges", 0.8)

store2 = Store("Мясной Магазин", "ул. Гагарина, 15")
store2.add_item("beef", 5.0)
store2.add_item("chicken", 3.0)
store2.add_item("pork", 4.0)

store3 = Store("Молочные Продукты", "ул. Советская, 20")
store3.add_item("milk", 1.2)
store3.add_item("cheese", 2.5)
store3.add_item("butter", 1.8)

# Пример использования
print(store1)
print("Ассортимент:", store1.items)

print(store2)
print("Ассортимент:", store2.items)

print(store3)
print("Ассортимент:", store3.items)

# Обновление цены и удаление товара
store1.update_price("apples", 0.6)
store1.remove_item("bananas")
print("Обновленный ассортимент:", store1.items)
