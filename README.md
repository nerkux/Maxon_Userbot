# Maxon Userbot 🤖

**Maxon Userbot** — это простой и функциональный userbot на базе VKMax User Client, предназначенный для автоматизации задач в VKMax.

## 📌 Основные фукции

* Обработка команд через любой чат.
* Easy-to-make плагины.
* Расширяемая архитектура — пользователь может подключать собственные модули.

## ⚙️ Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/nerkux/Maxon_Userbot.git
cd Maxon_Userbot
```
2. Установите зависимости
```bash
pip install -r requirements.txt
```
3. Отредактируйте main.py\
Добавьте свой номер телефона в переменную 'sms_login_token'
```python
sms_login_token = await client.send_code('+7xxxxxxxxxx')
```
5. Запустите main.py
```bash
python3 main.py
```
