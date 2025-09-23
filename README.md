# 🧩 Telegram Mini App: Игра 2048

**Telegram Mini App** — реализация классической головоломки [2048](https://play2048.co/) в виде Telegram-бота с WebApp интерфейсом. Игроки могут играть прямо в чате Telegram, сохранять рекорды и соревноваться с другими пользователями.

---

## 🎮 Возможности

- ▶️ Игра в Telegram WebApp
- 🏆 Таблица рекордов (лучший счёт)
- 👤 Личный рекорд каждого пользователя
- 🔄 Сохранение прогресса в localStorage
- 📱 Адаптивный интерфейс под мобильные устройства
- 🔁 Возможность начать заново
- 🧹 Очистка рекорда по кнопке

---

## 🧰 Технологии

- **Python 3.9+**
- **[aiogram 3.x]** — для работы с Telegram Bot API
- **[FastAPI]** — backend и WebApp
- **[SQLAlchemy 2.x]** + **[aiosqlite]** — асинхронная работа с SQLite
- **[Jinja2]** — шаблонизация HTML
- **HTML/CSS/JS** — фронтенд игры
- **Nginx** — reverse proxy и HTTPS
- **systemd** — управление сервисом в production

---

## 📦 Установка и запуск (локально)

1. Клонируйте репозиторий:
```bash
   git clone https://github.com/hyd3-me/2048_miniApp.git source
```

2. Создайте виртуальное окружение и установите зависимости:
```bash
python3 -m venv env
source env/bin/activate
pip install -r source/requirements.txt
```

3. Создайте .env файл:
```code
BOT_TOKEN=your_telegram_bot_token
ADMIN_IDS=[your_telegram_id]
BASE_SITE=https://your-domain.com
```

## ☁️ Деплой на сервер (production) 

- Используется Nginx как reverse proxy
- Приложение запущено через systemd
- База данных: SQLite
- SSL-сертификат через Let's Encrypt
- Запуск от имени пользователя www-data

## 🧠 Структура проекта

.
├── app/                 # Основное приложение
│   ├── bot/             # Обработчики бота
│   ├── config/          # Конфиг
│   ├── database.py/     # Взаимодейтсвие с бд
│   ├── game/            # Логика игры и DAO
│   ├── static/          # JS/CSS/иконки
│   ├── templates/       # HTML-шаблоны
│   └── main.py          # FastAPI-приложение
├── data/                # Файл SQLite базы данных
├── .env                 # Переменные окружения
├── requirements.txt     # Зависимости
└── README.md