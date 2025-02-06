import os
from dotenv import load_dotenv
from skpy import Skype

# Загружаем переменные из .env
load_dotenv()

USERNAME = os.getenv("SKYPE_USERNAME")
PASSWORD = os.getenv("SKYPE_PASSWORD")
GROUP_ID = os.getenv("SKYPE_GROUP_ID")

MESSAGE = "Привет, это автосообщение от бота!"

def send_message():
    try:
        skype = Skype(USERNAME, PASSWORD)  # Авторизация
        chat = skype.chats[GROUP_ID]  # Подключение к группе
        chat.sendMsg(MESSAGE)  # Отправка сообщения
        print("Сообщение отправлено!")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    send_message()