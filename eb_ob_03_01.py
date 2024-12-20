# Задание
# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).


class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def make_sound(self):
        raise NotImplementedError("Подклассы должны реализовывать этот метод")

    def eat(self):
        return f"{self._name} кушает."

    def __str__(self):
        return f"Животное(Имя: {self._name}, Возраст: {self._age})"


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self._wing_span = wing_span

    def make_sound(self):
        return f"{self._name} щебечет."

    def fly(self):
        return f"{self._name} летит с размахом крыльев {self._wing_span} м."


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self._fur_color = fur_color

    def make_sound(self):
        return f"{self._name} рычит."

    def run(self):
        return f"{self._name} бежит."


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self._scale_type = scale_type

    def make_sound(self):
        return f"{self._name} шипит."

    def crawl(self):
        return f"{self._name} ползает."


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


class Zoo:
    def __init__(self):
        self._animals = []
        self._staff = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self._animals.append(animal)
            print(f"{animal._name} добавлен в зоопарк.")
        else:
            print("Только животные могет быть добавлены")

    def add_staff(self, staff):
        self._staff.append(staff)
        print(f"{staff.get_name()} Добавлен в персонал зоопарка.")

    def list_animals(self):
        for animal in self._animals:
            print(animal)

    def list_staff(self):
        for staff in self._staff:
            print(staff)


class Staff:
    def __init__(self, name, position):
        self._name = name
        self._position = position

    def get_name(self):
        return self._name

    def __str__(self):
        return f"Персонал(Имя: {self._name}, На позиции: {self._position})"


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        return f"{self._name} is feeding {animal._name}."


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        return f"{self._name} is healing {animal._name}."


# Сохранение и загрузка данных о зоопарке
import pickle

def save_zoo(zoo, filename):
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)
    print("Данные зоопарка сохранены.")


def load_zoo(filename):
    try:
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
            print("Данные зоопарка загружены.")
            return zoo
    except FileNotFoundError:
        print("Не нашел сохраненных данных.")
        return Zoo()


# Пример использования
if __name__ == "__main__":
    # Создаем зоопарк
    zoo = Zoo()

    # Добавляем животных
    bird = Bird("Parrot", 2, 0.5)
    mammal = Mammal("Lion", 5, "Golden")
    reptile = Reptile("Snake", 3, "Scaly")

    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)

    # Добавляем сотрудников
    zookeeper = ZooKeeper("Alice")
    veterinarian = Veterinarian("Dr. Bob")

    zoo.add_staff(zookeeper)
    zoo.add_staff(veterinarian)

    # Демонстрируем полиморфизм
    animals = [bird, mammal, reptile]
    animal_sound(animals)

    # Сохраняем и загружаем данные
    save_zoo(zoo, "zoo_data.pkl")
    loaded_zoo = load_zoo("zoo_data.pkl")

    # Список животных и сотрудников после загрузки
    loaded_zoo.list_animals()
    loaded_zoo.list_staff()
