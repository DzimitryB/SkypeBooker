from dotenv import load_dotenv
import os
from skpy import Skype

# Загружаем переменные из .env
load_dotenv()

USERNAME = os.getenv("SKYPE_USERNAME") or "your_skype_username"
PASSWORD = os.getenv("SKYPE_PASSWORD") or "your_skype_password"

# Проверяем, загружены ли переменные
if not USERNAME or not PASSWORD:
    raise ValueError("Не удалось загрузить учетные данные Skype.")

# print(f"Username: {USERNAME[:3]}, Password: {PASSWORD[:3]}")
# Авторизация
try:
    sk = Skype(USERNAME, PASSWORD)
    print("Успешный вход в Skype!")
except Exception as e:
    print(f"Ошибка аутентификации: {e}")
    exit()

# Получаем список всех недавних чатов
try:
    for chat_id, chat in sk.chats.recent().items():
        chat_name = chat.topic if hasattr(chat, "topic") and chat.topic else chat_id
        print(f"Чат ID: {chat_id} | Название: {chat_name}")
except Exception as e:
    print(f"Ошибка при получении чатов: {e}")