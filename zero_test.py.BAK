import datetime
import time
import threading
import telebot
import random  # Импортируем random для случайного выбора

# Создаем экземпляр бота
bot = telebot.TeleBot('7782655648:AAHWm_EK-Jp-WA3rekHMvsuGGowmHYm0kMw')

# Список фактов
facts_list = [
    "**Вода на Земле может быть старше самой Солнечной системы**: Исследования показывают, что от 30% до 50% воды в наших океанах возможно присутствовала в межзвездном пространстве еще до формирования Солнечной системы около 4,6 миллиарда лет назад.",
    "**Горячая вода замерзает быстрее холодной**: Это явление известно как эффект Мпемба. Под определенными условиями горячая вода может замерзать быстрее, чем холодная, хотя ученые до сих пор полностью не разгадали механизм этого процесса.",
    "**Больше воды в атмосфере, чем во всех реках мира**: Объем водяного пара в атмосфере Земли в любой момент времени превышает объем воды во всех реках мира вместе взятых. Это подчеркивает важную роль атмосферы в гидрологическом цикле, перераспределяя воду по планете."
]

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Как дела?")
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

    reminder_thread = threading.Thread(target=send_power, args=(message.chat.id,))
    reminder_thread.start()

# Обработчик команды /fact
@bot.message_handler(commands=['fact'])
def fact_message(message):
    if facts_list:  # Проверяем, что список фактов не пустой
        random_fact = random.choice(facts_list)
        bot.reply_to(message, f'Лови факт о воде:\n{random_fact}')
    else:
        bot.reply_to(message, "К сожалению, факты закончились. Попробуйте позже!")

# Напомяналка про воду
def send_reminders(chat_id):
    first_rem = "09:00"
    second_rem = "14:00"
    end_rem = "18:00"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Напоминание - выпей стакан воды")
            time.sleep(61)
        time.sleep(1)

# Напомяналка про сон
def send_power(chat_id):
    wakeup_rem = "07:00"
    sleep_rem = "21:48"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == wakeup_rem:
            bot.send_message(chat_id, "Просыпайся, хватит спать")
            time.sleep(61)
        if now == sleep_rem:
            bot.send_message(chat_id, "Пора спать")
            time.sleep(61)
        time.sleep(1)

# Запускаем бота
if __name__ == '__main__':
    print("Запущен!")
    bot.polling(none_stop=True)