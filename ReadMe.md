# Skype Bot на Python

Этот бот отправляет сообщения в указанную группу Skype и тем самым бронирует парковочное место.

## Установка

1. Клонируйте репозиторий или скачайте файлы.
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Пропишите необходимые данные данные в ".env" файле.
```bash
SKYPE_USERNAME=your_username
SKYPE_PASSWORD=your_password
SKYPE_GROUP_ID=your_group_id
PARKING_LIST=1,2,3,4
```

## Запуск
``` bash
   python main.py