import os
from dotenv import load_dotenv
from skpy import Skype
from datetime import datetime
import re

# Загружаем переменные из .env
load_dotenv()

USERNAME = os.getenv("SKYPE_USERNAME")
PASSWORD = os.getenv("SKYPE_PASSWORD")
GROUP_ID = os.getenv("SKYPE_GROUP_ID")

MESSAGE = "Привет, это автосообщение от бота!"

# Авторизация в Skype
sk = Skype(USERNAME, PASSWORD)

# # Получаем список всех недавних чатов
# for chat in sk.chats.recent():
#     if isinstance(chat, str):  # Если элемент — строковый ID
#         chat_id = chat
#         chat_name = chat  # В данном случае имя чата совпадает с его ID
#     else:  # Если элемент — объект SkypeChat
#         chat_id = chat.id
#         chat_name = chat.topic or chat.userId

#     print(f"Чат ID: {chat_id} | Название: {chat_name}")

# list of parking spaces
# parking_list = [138, 139, 167, 168, 169]
parking_list = list(map(int, os.getenv("PARKING_LIST", "").split(","))) if os.getenv("PARKING_LIST") else []

# Получаем группу по ID
chat = sk.chats[GROUP_ID]

# Получаем текущее время (сегодняшняя дата)
today = datetime.today()

# Функция для чтения сообщений, отправленных сегодня
def read_today_messages():
    print("Чтение сообщений за сегодня:")
    today_messages=[]
    for msg in chat.getMsgs():
        # Проверяем, что сообщение было отправлено сегодня
        msg_time = msg.time  # Время отправки сообщения
        if msg_time.year == today.year and msg_time.month == today.month and msg_time.day == today.day:
            # Если дата сообщения совпадает с сегодняшней, выводим
            today_messages.append(msg.content)
            print(f"{msg.userId}: {msg.content} (время: {msg_time})")
    return today_messages

def sort_lists(list1, list2):
    # Извлекаем числа из первого списка (только отдельные числа)
    list1_numbers = []
    for item in list1:
        if isinstance(item, (int, float)):  # Если элемент уже число, добавляем его
            list1_numbers.append(item)
        elif isinstance(item, str):  # Если элемент строка, ищем в ней числа
            numbers_in_string = re.findall(r'-?\d+\.?\d*', item)  # Находим все числа в строке
            list1_numbers.extend(map(float, numbers_in_string))  # Добавляем найденные числа

    # Получаем числа из второго списка (с номерами парковочных мест), которых нет в первом
    result = [num for num in list2 if num not in list1_numbers]
    return result

def send_message(message):
    try:
        print('GROUP_ID: ', GROUP_ID)
        chat.sendMsg(message)  # Отправка сообщения
        print("Сообщение отправлено!")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    # Чтение сообщений
    messages = read_today_messages()
    free_parking_list = sort_lists(messages, parking_list)
    if not free_parking_list[0]:
        send_message(free_parking_list[0])