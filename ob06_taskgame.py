# Задание: Разработать консольную игру "Битва героев" на Python с использованием классов и разработать план проекта по этапам/или создать kanban доску для работы над данным проектом
# Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками. Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
# Требования:
# 	1	Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# 	2	Игра должна быть реализована как консольное приложение.
# Классы:
# Класс Hero:
# 	•	Атрибуты:
# 	•	Имя (name)
# 	•	Здоровье (health), начальное значение 100
# 	•	Сила удара (attack_power), начальное значение 20
# 	•	Методы:
# 	•	attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# 	•	is_alive(): возвращает True, если здоровье героя больше 0, иначе False
# Класс Game:
# 	•	Атрибуты:
# 	•	Игрок (player), экземпляр класса Hero
# 	•	Компьютер (computer), экземпляр класса Hero
# 	•	Методы:
# 	•	start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        if not isinstance(other, Hero):
            raise ValueError("Цель должна быть экземпляром Hero")
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и делает {damage} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра начата!")
        print(f"{self.player.name} vs {self.computer.name}")

        while self.player.is_alive() and self.computer.is_alive():
            # Player's turn
            print("\nХод игрока:")
            self.player.attack(self.computer)
            print(f"{self.computer.name} оставшееся здоровье: {self.computer.health}")
            if not self.computer.is_alive():
                print(f"\n{self.computer.name} побеждён! {self.player.name} победил!")
                break

            # Computer's turn
            print("\nХод ИИ соперника:")
            self.computer.attack(self.player)
            print(f"{self.player.name} оставшееся здоровье: {self.player.health}")
            if not self.player.is_alive():
                print(f"\n{self.player.name} побеждён!{self.computer.name} победил!")
                break

if __name__ == "__main__":
    player_name = input("Введите имя своего героя: ")
    computer_name = "ИИ Герой"
    game = Game(player_name, computer_name)
    game.start()