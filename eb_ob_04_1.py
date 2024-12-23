# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
#
# Цель: Цель этого домашнего задание - закрепить понимание и навыки применения принципа открытости/закрытости (Open/Closed Principle), одного из пяти SOLID принципов объектно-ориентированного программирования. Принцип гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
#
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами. Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.
#
# Исходные данные:
#
# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
# Шаг 1: Создайте абстрактный класс для оружия
#
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
# Шаг 2: Реализуйте конкретные типы оружия
#
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow. Каждый из этих классов реализует метод attack() своим уникальным способом.
# Шаг 3: Модифицируйте класс Fighter
#
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
# Добавьте метод change_weapon(), который позволяет изменить оружие бойца.
# Шаг 4: Реализация боя
#
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
#
# Код должен быть написан на Python.
# Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# Программа должна выводить результат боя в консоль.

from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self, monster):
        pass

# Конкретные типы оружия
class Sword(Weapon):
    def attack(self, monster):
        damage = 50
        print("Меч наносит сильный рубящий удар!")
        monster.take_damage(damage)

class Bow(Weapon):
    def attack(self, monster):
        damage = 30
        print("Лук выпускает стрелу с точным попаданием!")
        monster.take_damage(damage)

class MagicStaff(Weapon):
    def attack(self, monster):
        damage = 40
        print("Магический посох испускает мощное заклинание!")
        monster.take_damage(damage)

# Класс, представляющий бойца
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def attack(self, monster):
        print(f"{self.name} атакует!")
        self.weapon.attack(monster)

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} сменил оружие.")

# Класс, представляющий монстра
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")
        else:
            print(f"{self.name} побежден!")

# Пример использования
if __name__ == "__main__":
    # Создаем оружие
    sword = Sword()
    bow = Bow()
    staff = MagicStaff()

    # Создаем бойца и монстра
    fighter = Fighter("Рыцарь", sword)
    monster = Monster("Орк", 100)

    # Боец атакует с использованием меча
    print("Боец выбирает меч.")
    fighter.attack(monster)

    # Боец меняет оружие на лук
    print("\nБоец выбирает лук.")
    fighter.change_weapon(bow)
    monster = Monster("Тролль", 80)  # Новый монстр
    fighter.attack(monster)

    # Боец меняет оружие на магический посох
    print("\nБоец выбирает магический посох.")
    fighter.change_weapon(staff)
    monster = Monster("Дракон", 120)  # Новый монстр
    fighter.attack(monster)