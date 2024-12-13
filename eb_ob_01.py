from datetime import datetime

class Task:
    def __init__(self, description, deadline):
        """
        Инициализация задачи.

        :param description: Описание задачи
        :param deadline: Срок выполнения (строка в формате 'YYYY-MM-DD')
        """
        self.description = description
        self.deadline = datetime.strptime(deadline, '%Y-%m-%d')
        self.completed = False

    def mark_as_completed(self):
        """Отметить задачу как выполненную."""
        self.completed = True

    def __str__(self):
        """Возвращает строковое представление задачи."""
        status = 'Выполнено' if self.completed else 'Не выполнено'
        return f"{self.description} (Срок: {self.deadline.date()}, Статус: {status})"

class TaskManager:
    def __init__(self):
        """Инициализация менеджера задач."""
        self.tasks = []

    def add_task(self, description, deadline):
        """Добавить новую задачу.

        :param description: Описание задачи
        :param deadline: Срок выполнения (строка в формате 'YYYY-MM-DD')
        """
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_index):
        """Отметить задачу как выполненную.

        :param task_index: Индекс задачи в списке
        """
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Неверный индекс задачи.")

    def get_pending_tasks(self):
        """Получить список текущих (не выполненных) задач."""
        return [task for task in self.tasks if not task.completed]

    def display_tasks(self):
        """Вывод списка всех задач."""
        if not self.tasks:
            print("Список задач пуст.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    # Добавление задач
    manager.add_task("Купить продукты", "2024-12-15")
    manager.add_task("Сдать проект", "2024-12-20")

    # Отображение всех задач
    print("Все задачи:")
    manager.display_tasks()

    # Отметить первую задачу как выполненную
    manager.mark_task_as_completed(0)

    # Вывести текущие (не выполненные) задачи
    print("\nНе выполненные задачи:")
    for task in manager.get_pending_tasks():
        print(task)