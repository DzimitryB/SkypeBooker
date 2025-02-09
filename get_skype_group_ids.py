from dotenv import load_dotenv
import os
from skpy import Skype

# Загружаем переменные из .env
load_dotenv()

USERNAME = os.getenv("SKYPE_USERNAME")
PASSWORD = os.getenv("SKYPE_PASSWORD")


sk = Skype(USERNAME, PASSWORD)

# Получаем список всех недавних чатов
for chat in sk.chats.recent():
    if isinstance(chat, str):  # Если элемент — строковый ID
        chat_id = chat
        chat_name = chat  # В данном случае имя чата совпадает с его ID
    else:  # Если элемент — объект SkypeChat
        chat_id = chat.id
        chat_name = chat.topic or chat.userId

    print(f"Чат ID: {chat_id} | Название: {chat_name}")