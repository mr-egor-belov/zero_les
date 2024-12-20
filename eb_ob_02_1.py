# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей,
# имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка
# (представь, что это просто список экземпляров User).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и
# модификации снаружи. Предоставь доступ к необходимым атрибутам через методы
# (например, get и set методы).

class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

# Методы для получения данных пользователя
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Метод для изменения имени пользователя
    def set_name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f"User(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"


class Admin(User):
    def __init__(self, user_id, name, admin_access_level='admin'):
        super().__init__(user_id, name, access_level=admin_access_level)
        self._admin_access_level = admin_access_level

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"User {user.get_name()} added successfully.")
        else:
            print("Error: Only instances of User can be added.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"User {user.get_name()} removed successfully.")
                return
        print(f"Error: User with ID {user_id} not found.")

    def __str__(self):
        return f"Admin(ID: {self._user_id}, Name: {self._name}, Access Level: {self._admin_access_level})"


# Пример использования
if __name__ == "__main__":
    # Создаем список пользователей
    user_list = []

    # Создаем обычных пользователей
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")

    # Добавляем пользователей в список
    user_list.append(user1)
    user_list.append(user2)

    # Создаем администратора
    admin = Admin(99, "Charlie")

    # Администратор добавляет нового пользователя
    user3 = User(3, "Eve")
    admin.add_user(user_list, user3)

    # Администратор удаляет пользователя
    admin.remove_user(user_list, 2)

    # Выводим всех пользователей
    for user in user_list:
        print(user)