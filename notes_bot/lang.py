from typing import Any, Literal

# noinspection PyPackageRequirements
from telebot.types import BotCommand

import config
from notes_bot.request import request


def end(lang: str):
    def closure_ru(num_diff: int):
        num_diff = str(num_diff)
        if (
            num_diff[-2:] in ("11", "12", "13", "14")
            or num_diff[-1] == "0"
            or num_diff[-1] in ("5", "6", "7", "8", "9")
        ):
            return "дней"
        elif num_diff[-1] in ("2", "3", "4"):
            return "дня"
        elif num_diff[-1] == "1":
            return "день"

    def closure_en(num_diff: int):
        return "day" if num_diff == 1 else "days"

    if lang == "ru":
        return closure_ru
    else:
        return closure_en


translation = {
    "func": {
        "deldate": {
            "ru": lambda x: f"<b>{x} {end('ru')(x)} до удаления</b>",
            "en": lambda x: f"<b>{x} {end('en')(x)} before delete</b>",
        },
    },
    "arrays": {
        "relative_date_list": {
            "ru": (
                "Сегодня",
                "Завтра",
                "Послезавтра",
                "Вчера",
                "Позавчера",
                "Через",
                "назад",
                end("ru"),
            ),
            "en": (
                "Today",
                "Tomorrow",
                "Day after tomorrow",
                "Yesterday",
                "Day before yesterday",
                "After",
                "ago",
                end("en"),
            ),
        },
        "account": {
            "ru": (
                "Событий в день",
                "Символов в день",
                "Событий в месяц",
                "Символов в месяц",
                "Событий в год",
                "Символов в год",
                "Событий всего",
                "Символов всего",
            ),
            "en": (
                "Events per day",
                "Symbols per day",
                "Events per month",
                "Symbols per month",
                "Events per year",
                "Symbols per year",
                "Total events",
                "Total symbols",
            ),
        },
        "months_list": {
            "ru": (
                (("Январь", 1), ("Февраль", 2), ("Март", 3)),
                (("Апрель", 4), ("Май", 5), ("Июнь", 6)),
                (("Июль", 7), ("Август", 8), ("Сентябрь", 9)),
                (("Октябрь", 10), ("Ноябрь", 11), ("Декабрь", 12)),
            ),
            "en": (
                (("January", 1), ("February", 2), ("March", 3)),
                (("April", 4), ("May", 5), ("June", 6)),
                (("July", 7), ("August", 8), ("September", 9)),
                (("October", 10), ("November", 11), ("December", 12)),
            ),
        },
        "week_days_list": {
            "ru": ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"),
            "en": ("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"),
        },
        "week_days_list_full": {
            "ru": (
                "Понедельник",
                "Вторник",
                "Среда",
                "Четверг",
                "Пятница",
                "Суббота",
                "Воскресенье",
            ),
            "en": (
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ),
        },
        "months_name": {
            "ru": (
                "Январь",
                "Февраль",
                "Март",
                "Апрель",
                "Май",
                "Июнь",
                "Июль",
                "Август",
                "Сентябрь",
                "Октябрь",
                "Ноябрь",
                "Декабрь",
            ),
            "en": (
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ),
        },
        "months_name2": {
            "ru": (
                "Января",
                "Февраля",
                "Марта",
                "Апреля",
                "Мая",
                "Июня",
                "Июля",
                "Августа",
                "Сентября",
                "Октября",
                "Ноября",
                "Декабря",
            ),
            "en": (
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ),
        },
    },
    "text": {
        "page": {
            "ru": "Страница",
            "en": "Page",
        },
        "add_bot_to_group": {
            "ru": "Добавить бота в группу",
            "en": "Add bot to group",
        },
        "restore_to_default": {
            "ru": "Настройки по умолчанию",
            "en": "Set default settings",
        },
        "migrate": {
            "ru": """
Группа (<code>{from_chat_id}</code>) обновилась до супергруппы (<code>{to_chat_id}</code>).
<b>Из-за особенностей телеграма все предыдущие сообщения бота в этой группе устарели и больше не могут быть использованы для взаимодействий с вашим аккаунтом.
Вызовите новые сообщения с помощью команд бота.</b>
""",
            "en": """
The group (<code>{from_chat_id}</code>) migrate into a supergroup (<code>{to_chat_id}</code>).
<b>Due to the nature of Telegram, all previous bot messages in this group are outdated and can no longer be used to interact with your account.
Call up new messages using bot commands.</b>
""",
        },
        "account_has_been_deleted": {
            "ru": "Ваш аккаунт удалён.",
            "en": "Your account has been deleted.",
        },
        "recover": {
            "ru": "Восстановить",
            "en": "Recover",
        },
        "leap": {
            "ru": "Високосный",
            "en": "leap",
        },
        "not_leap": {
            "ru": "Невисокосный",
            "en": "non-leap",
        },
        "trash_bin": {
            "ru": "В корзину",
            "en": "To trash bin",
        },
        "delete_permanently": {
            "ru": "Удалить навсегда",
            "en": "Delete permanently",
        },
        "changes_saved": {
            "ru": "Изменения сохранены",
            "en": "Changes saved",
        },
        "event_about_info": {
            "ru": (
                "Информация о событии",
                "длинна текста",
                "время добавления",
                "время последних изменений",
            ),
            "en": (
                "Information about event",
                "text length",
                "time added",
                "time of last changes",
            ),
        },
        "clean_bin": {
            "ru": "Очистить корзину",
            "en": "Clear basket",
        },
        "bin_is_emptied": {
            "ru": "Корзина очищена",
            "en": "Bin is emptied",
        },
        "send_event_text": {
            "ru": "Отправьте текст события",
            "en": "Send the text of the event",
        },
        "send_group_name": {
            "ru": "Отправьте название группы",
            "en": "Send the name of the group",
        },
        "recurring_events": {
            "ru": "Повторяющиеся события",
            "en": "Recurring events",
        },
        "week_events": {
            "ru": "События в ближайшие 7 дней",
            "en": "Events in the next 7 days",
        },
        "are_you_sure_edit": {
            "ru": "Вы точно хотите изменить тест события на",
            "en": "Are you sure you want to change the event text to",
        },
        "edit_username": {
            "ru": "Изменить имя пользователя",
            "en": "Change username",
        },
        "edit_password": {
            "ru": "Изменить пароль",
            "en": "Change password",
        },
        "logout": {
            "ru": "Выйти",
            "en": "Logout",
        },
        "leave_group": {
            "ru": "Выйти из группы",
            "en": "Leave the group",
        },
        "create_group": {
            "ru": """
👥 Группы

Отправьте имя группы
""",
            "en": """
👥 Groups

Send group name
""",
        },
        "change_group_name": {
            "ru": "Изменить название группы",
            "en": "Change group name",
        },
        "delete_group": {
            "ru": "Удалить группу",
            "en": "Delete group",
        },
        "remove_bot_from_group": {
            "ru": "Удалить бота из группы",
            "en": "Remove a bot from a group",
        },
        "meters_per_second": {
            "ru": "м/с",
            "en": "m/s",
        },
        "get_premium": {
            "ru": "Получить Premium",
            "en": "Get Premium",
        },
        "status": {
            "-1": {
                "ru": "бан",
                "en": "ban",
            },
            "0": {
                "ru": "обычный",
                "en": "normal",
            },
            "1": {
                "ru": "премиум",
                "en": "premium",
            },
            "2": {
                "ru": "админ",
                "en": "admin",
            },
        },
        "export_group": {
            "ru": "Экспортировать данные группы",
            "en": "Export group data",
        },
        "event_history": {
            "ru": (
                "История события",
                "Вы не изменяли эту заметку",
                {
                    "text": "Изменение текста",
                    "statuses": "Изменение статуса",
                    "date": "Изменение даты",
                    "delete": "Удаление",
                    "recover": "Восстановление",
                },
            ),
            "en": (
                "Event history",
                "You didn't change this note",
                {
                    "text": "Change text",
                    "statuses": "Status change",
                    "date": "Date change",
                    "delete": "Delete",
                    "recover": "Recovery",
                },
            ),
        },
        "search_placeholder": {
            "ru": """
Ответьте на это сообщение с новым поисковым запросом.
`<code>.</code>` - искать всё
""",
            "en": """
Reply to this message with a new search query.
`<code>.</code>` - search all
""",
        },
        "search_filters": {
            "ru": {
                "db": ("До даты", "<"),
                "dd": ("В течении даты", "="),
                "da": ("После даты", ">"),
                "tc": ("Совпадение статуса", "="),
                "ta": ("Примерное совпадение статуса", "≈"),
                "tn": ("Не содержит статуса", "≠"),
            },
            "en": {
                "db": ("Before date", "<"),
                "dd": ("During date", "="),
                "da": ("After date", ">"),
                "tc": ("Status Match", "="),
                "ta": ("Approximate status match", "≈"),
                "tn": ("Not status match", "≠"),
            },
        },
        "search_filters_clue": {
            "ru": (
                "Нажмите на {} чтобы добавить фильтр",
                "Нажмите на кнопки ниже чтобы удалить фильтр",
            ),
            "en": (
                "Click on {} to add a filter",
                "Click on the buttons below to remove the filter",
            ),
        },
        "search_filter_clue": {
            "ru": (
                "Выберите тип фильтра",
                "Выберите дату для фильтра",
                "Выберите статус для фильтра",
            ),
            "en": (
                "Select filter type",
                "Select date for filter",
                "Select status for filter",
            ),
        },
        "bool": {
            "yes": {
                "ru": "Да",
                "en": "Yes",
            },
            "no": {
                "ru": "Нет",
                "en": "No",
            },
        },
        "lang_flag": {
            "ru": "",
            "en": "",
        },
        "saved": {
            "ru": "Сохранено",
            "en": "Saved",
        },
    },
    "messages": {
        "start": {
            "ru": """
Приветствую вас! Я - ваш личный календарь-помощник.
Здесь вы можете легко создавать события и заметки, доступ к которым будет из календаря. Используйте специальные эмодзи, чтобы добавить эффекты или сделать поиск еще удобнее!

📅 Календарь: Пользуйтесь удобным календарём и легко перемещайтесь между днями и месяцами.

🔍 Поиск: Ищите события по тексту и используйте удобные фильтры, чтобы ни одна важная заметка не ускользнула от вашего внимания!

🔔 Уведомления: Никогда не пропустите важные моменты! Настройте уведомления на определенное время или отключите их, когда вам удобно.

☁️ Погода: Хотите знать прогноз погоды в вашем городе? Просто спросите меня, и я предоставлю вам актуальные данные.

👑 Преимущества премиум-пользователей: Лимиты увеличены, а также доступна удобная мусорная корзина для удалённых событий.

Пользуйтесь всеми преимуществами бота, чтобы упорядочить свою жизнь и не упустить ни одного важного момента! Если у вас возникли вопросы, введите команду /help. Приятного использования! 🌟
""",
            "en": """
Greetings! I am your personal calendar assistant.
Here you can easily create events and notes that can be accessed from the calendar. Just use special emoji to add effects or make your search even more convenient!

📅 Calendar: Use a convenient calendar and easily move between days and months.

🔍 Search: Search for events by text and use convenient filters, so that not a single important event will escape your notice!

🔔 Notifications: Never miss important moments! Set notification for a specific time or turn them off at your convenience.

☁️ Weather: Want to know the weather forecast for your city? Just ask me and I will provide you with up-to-date data.

👑 Premium user benefits: Limits have been increased and a handy recycle bin is available for events that have been removed.

Use all the advantages of the bot to streamline your life and not miss a single important moment! If you have any questions, enter the /help command. Happy using! 🌟
""",
        },
        "settings": {
            "ru": """⚙️ Настройки

[<u>Язык</u>]
<b>{lang}</b>

[<u>Уменьшать ссылки</u>]*
<b>{sub_urls}</b> <i>(Да рекомендуется)</i>

[<u>Город</u>]**
<b>{city}</b> <i>(London по умолчанию)</i>

[<u>Часовой пояс</u>]
<b>{timezone}</b> <i>(0 по умолчанию)</i> У вас сейчас <b>{timezone_question}</b>?

[<u>Уведомления</u>](🔕→🔔→📆)
<b>{notification_type} {notification_time}</b> <i>(🔕 по умолчанию)</i>

[<u>Тема</u>]***
<b>{theme}</b> <i>(⬜ по умолчанию)</i>

*(<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
>www.youtube.com</a> <i>вместо полной ссылки</i>)
**<i>Ответьте на это сообщение с названием города</i> <b>(Несохраненные настройки будут сброшены)</b>
***<i>Изменяет тёмные эмодзи на светлые</i>""",
            "en": """⚙️ Settings

[<u>Language</u>]
<b>{lang}</b>

[<u>Minify links</u>]
<b>{sub_urls}</b> <i>(Yes recommended)</i>

[<u>City</u>]
<b>{city}</b> <i>(London by default)</i>

[<u>Timezone</u>]
<b>{timezone}</b> <i>(0 by default)</i> Do you have <b>{timezone_question}</b> now?

[<u>Notifications</u>](🔕→🔔→📆)
<b>{notification_type} {notification_time}</b> <i>(🔕 by default)</i>

[<u>Theme</u>]***
<b>{theme}</b> <i>(⬜ by default)</i>

*(<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
>www.youtube.com</a> <i>instead of full link</i>)
**<i>Reply to this message with a city name</i> <b>(Unsaved settings will be reset)</b>
***<i>Changes dark emojis to light ones</i>""",
        },
        "group": {
            "ru": """
👥 Группа

id: `<code>{}</code>`
name: `<code>{}</code>`
""",
            "en": """
👥 Group

id: `<code>{}</code>`
name: `<code>{}</code>`
""",
        },
        "groups": {
            "ru": (
                "Создать группу",
                """
👥 Группы

У вас групп: {}

{}
""",
                """
{page}) Название: `<code>{name}</code>`
     id: `<code>{group_id}</code>`
     Статус: `<code>{status}</code>`
     Вступил: `<code>{entry_date}</code>`
     chat_id: `<code>{chat_id}</code>`
""",
                ("Все", "Участник", "Модератор", "Администратор"),
            ),
            "en": (
                "Create group",
                """
👥 Groups

You have groups: {}

{}
""",
                """
{page}) name: `<code>{name}</code>`
     id: `<code>{group_id}</code>`
     status: `<code>{status}</code>`
     entry_date: `<code>{entry_date}</code>`
     chat_id: `<code>{chat_id}</code>`
""",
                ("All", "Member", "Moderator", "Admin"),
            ),
        },
        "account": {
            "ru": """
👤 Аккаунт

<pre><code class='language-yaml'>id:       {}
chat_id:  {}
username: {}
reg_date: {}</code></pre>
""",
            "en": """
👤 Account

<pre><code class='language-yaml'>id:       {}
chat_id:  {}
username: {}
reg_date: {}</code></pre>
""",
        },
        "help": {
            "title": {
                "ru": "📚 Помощь",
                "en": "📚 Help",
            },
            "page main": {
                "ru": [
                    """
Добро пожаловать в раздел помощи.
Ниже вы можете выбрать кнопку с темой, чтобы прочитать подробнее.
Кнопки с текстом помечаются эмодзи 📄. Папка для кнопок помечается 📁. Вернуться назад из папки можно нажав  🔙.
""",
                    [
                        [{k.ljust(60, config.ts): v}]
                        for k, v in {
                            "📄 События": "mnh Events",
                            "📄 Статусы": "mnh Statuses",
                            "📄 Лимиты": "mnh Limits",
                            "📂 Виды сообщений": "mnh page messages",
                            "📂 Команды": "mnh page commands",
                            "🗞 О боте": "mnh page about",
                            "🔙": "mnm",
                        }.items()
                    ],
                ],
                "en": [
                    """
Welcome to the help section.
Below you can select the topic button to read more.
Buttons with text are marked with a smiley 📄. The button folder is marked with 📁. You can go back from a folder by pressing 🔙.
""",
                    [
                        [{k.ljust(60, config.ts): v}]
                        for k, v in {
                            "📄 Events": "mnh Events",
                            "📄 Statuses": "mnh Statuses",
                            "📄 Limits": "mnh Limits",
                            "📂 Types of messages": "mnh page messages",
                            "📂 Commands": "mnh page commands",
                            "🗞 About bot": "mnh page about",
                            "🔙": "mnm",
                        }.items()
                    ],
                ],
            },
            "page messages": {
                "ru": [
                    """
<b><u>Виды сообщений</u></b>

В боте есть разные виды сообщений, каждый из которых имеет свои особенности и функции.
Выберите кнопку с темой, чтобы прочитать подробнее.
""",
                    [
                        [{k.ljust(60, config.ts): v}]
                        for k, v in {
                            "📄 Календарь": "mnh Calendar",
                            "📄 1 день": "mnh 1_day",
                            "📄 7 дней": "mnh 7_days",
                            "📄 Настройки": "mnh Settings",
                            "📄 Корзина": "mnh Basket",
                            "📄 Поиск": "mnh Search",
                            "📄 Уведомления": "mnh Notifications",
                            "🔙": "mnh page main",
                        }.items()
                    ],
                ],
                "en": [
                    """
<b><u>Types of messages</u></b>

The bot has different types of messages, each of which has its own characteristics and functions.
Select a topic button to read more.
""",
                    [
                        [{k.ljust(60, config.ts): v}]
                        for k, v in {
                            "📄 Calendar": "mnh Calendar",
                            "📄 1 day": "mnh 1_day",
                            "📄 7 days": "mnh 7_days",
                            "📄 Settings": "mnh Settings",
                            "📄 Basket": "mnh Basket",
                            "📄 Search": "mnh Search",
                            "📄 Notifications": "mnh Notifications",
                            "🔙": "mnh page main",
                        }.items()
                    ],
                ],
            },
            "page commands": {
                "ru": [
                    """
<u><b>Команды бота</b></u>

/start - Старт
/menu - Меню
/calendar - Календарь
/today - События на сегодня
/weather {city} - Погода сейчас
/forecast {city} - Прогноз погоды
/week_event_list - Список событий на ближайшие 7 дней
/dice - Кинуть кубик
/export - Сохранить мои события в csv
/help - Помощь
/settings - Настройки
/logout - Выйти из аккаунта
/search {...} - Поиск
/id - Получить свой Telegram id
/open - Шорткаты для открытия сообщений
/commands - Этот список
""",
                    [
                        [{k.ljust(60, config.ts): v}]
                        for k, v in {
                            "📄 /open": "mnh CommandOpen",
                            "🔙": "mnh page main",
                        }.items()
                    ],
                ],
                "en": [
                    """
<u><b>Bot commands</b></u>

/start - Start
/menu - Menu
/calendar - Calendar
/today - Events for today
/weather {city} - Weather now
/forecast {city} - Weather forecast
/week_event_list - List of events for the next 7 days
/dice - Roll a die
/export - Save my events to csv
/help - Help
/settings - Settings
/logout - Logout
/search {...} - Search
/id - Get your Telegram id
/open - Shortcuts for opening messages
/commands - This list
""",
                    [
                        [{k.ljust(60, config.ts): v}]
                        for k, v in {
                            "📄 /open": "mnh CommandOpen",
                            "🔙": "mnh page main",
                        }.items()
                    ],
                ],
            },
            "page about": {
                "ru": [
                    """
<u><b>О боте</b></u>

▪️ .
""",
                    [
                        [{k.ljust(60, config.ts): v}]
                        for k, v in {
                            "📄 Новости бота": "mnh BotNews",
                            "📄 Версия бота": "mnh BotVersion",
                            "🔙": "mnh page main",
                        }.items()
                    ],
                ],
                "en": [
                    """
<u><b>About bot</b></u>

▪️ .
""",
                    [
                        [{k.ljust(60, config.ts): v}]
                        for k, v in {
                            "📄 Bot news": "mnh BotNews",
                            "📄 Bot version": "mnh BotVersion",
                            "🔙": "mnh page main",
                        }.items()
                    ],
                ],
            },
            "Events": {
                "ru": """
<u><b>События</b></u>

Событие - это текстовая заметка на определенную дату. Каждое событие помечается уникальным номером (id) и может иметь свой статус. По умолчанию статус устанавливается как "⬜". Статус можно изменить с помощью кнопки "🏷" в сообщении на день.

В сообщении на день есть кнопки для изменения или удаления событий. Если событий в сообщении несколько, то такие кнопки предлагают выбрать конкретное. <b>Если событие одно, то кнопки сразу выбирают его.</b>

Вот обозначения кнопок в сообщении для одного события:
📝 - Редактировать текст
🏷 - Изменить теги
🗑 - Удалить
📋 - Просмотр в аккуратном виде
*️⃣ -
📅 - Изменить дату
ℹ️ - Просмотр информации
🗄 - Просмотр истории изменений
🖼 -
""",
                "en": """
<u><b>Events</b></u>

An event is a textual note for a specific date. Each event is marked with a unique identifier (id) and can have its own status. By default, the status is set to "⬜". The status can be changed using the "🏷" button in the message for a day.

The message for the day has buttons for changing or deleting events. If there are several events in the message, then such buttons offer to select a specific one. <b>If there is only one event, then the buttons select it immediately.</b>

Here are the button labels in the message for one event:
📝 - Edit text
🏷 - Change tags
🗑 - Delete
📋 - View neatly
*️⃣ -
📅 - Change date
ℹ️ - View information
🗄 - View change history
🖼 -
""",
            },
            "Statuses": {
                "ru": """
<u><b>Статусы</b></u>

Статус - это один или несколько эмодзи для пометки события или добавления разных эффектов.
Статусы разделяются на три группы: "Важность", "Разное" и "Эффекты".

Важность
└─ Статусы для пометки важности или готовности события.

Разное
└─ Разные статусы.

Эффекты
└─ Статусы, добавляющие эффекты к событиям.


Статусы "🗒" (Список) и "🧮" (Нумерованный список) размечают каждую строку своими эмодзи.
Если поставить "-- " перед строкой, то на этой строке такая разметка применяться не будет.

<b>Событие может иметь максимум 5 статусов.</b>

<b>Эффекты на статусах применяются только на отображении событий в сообщении.</b> Сам текст события не меняется.
""",
                "en": """
<u><b>Statuses</b></u>

Status - this is one or several emojis used to mark an event or add different effects.
Statuses are divided into three groups: "Importance," "Miscellaneous," and "Effects."

Importance
└─ Statuses for marking the importance or readiness of an event.

Miscellaneous
└─ Miscellaneous statuses.

Effects
└─ Statuses that add effects to the events.

The statuses "🗒" (List) and "🧮" (Numbered list) annotate each line with their emojis.
If you put "--" in front of a line, then this markup do not apply on this line.

<b>An event can have a maximum of 5 statuses.</b>

<b>Effects on statuses are applied only on the display of events in the message.</b> The text of the event itself does not change.
""",
            },
            "Limits": {
                "ru": """
<u><b>Лимиты</b></u>

Для разных типов пользователей существуют различные лимиты на использование бота. Лимиты могут касаться как количества событий, так и количества символов.

По умолчанию у обычного пользователя доступны следующие лимиты:

<b>20</b> событий в день,
<b>4000</b> символов в день,
<b>75</b> событий в месяц,
<b>10000</b> символов в месяц,
<b>500</b> событий в год,
<b>80000</b> символов в год.
Максимальный <b>общий</b> лимит для обычного пользователя составляет <b>500</b> событий и <b>100000</b> символов.

Если вы превысите лимиты, вы не сможете добавлять новые события и добавлять новый текст к событиям. Чтобы освободить место под новые события, вы можете удалять старые события или сократить их текст.
""",
                "en": """
<u><b>Limits</b></u>

For different types of users, there are different limits on using the bot. These limits may apply to both the number of events and the number of characters.

By default, regular users have the following limits:

<b>20</b> events per day
<b>4000</b> characters per day
<b>75</b> events per month
<b>10000</b> characters per month
<b>500</b> events per year
<b>80000</b> characters per year
The maximum <b>general</b> limit for a normal user is <b>500</b> events and <b>100000</b> characters.

If you exceed the limits, you will not be able to add new events and add new text to events. To make a room for new events, you can delete old events or shorten their text.
""",
            },
            "Calendar": {
                "ru": """
<u>Виды сообщений > <b>Календарь</b></u>

Вы можете выбрать дату, нажав на кнопку с номером дня.
Кнопками внизу вы можете выбрать год и месяц.
Кнопкой "⟳" можно вернуться к текущей дате и выбрать текущий день.

При нажатии кнопки с датой в первом ряду вы попадете в список месяцев.
Там вы сможете выбрать месяц выбранного года.

В календаре существуют специальные обозначения для дней с событиями или с сегодняшним числом.
Вот значения символов обозначений:
"#" - Сегодняшний номер дня (отображается в любых месяцах).
"*" - В этот день есть события.
"!" - В этот день или в этот день другого года есть событие с повторяющимся статусом. Например, день рождения "🎉" или праздник "🎊".
""",
                "en": """
<u>Types of messages > <b>Calendar</b></u>

You can select a date by clicking on the day number button.
You can select the year and month using the buttons below.
With the "⟳" button, you can return to the current date and select the current day.

When you click on a date button in the first row, you will see the list of months.
There, you can choose a month within the selected year.

In the calendar, there are special symbols to indicate days with events or today's date.
Here are the meanings of the symbol notations:
"#" - Today's date (displayed in any month).
"*" - Events are scheduled for this day.
"!" - This day or the same date in a different year has a recurring event status. For example, a birthday "🎉" or a holiday "🎊".
""",
            },
            "1_day": {
                "ru": """
<u>Виды сообщений > <b>1 день</b></u>

Сообщение отображает события на один день.

Перед самим текстом события размещается строка с информацией о событии.
Например: <pre>1.3.⬜</pre>
Тут 1 это порядковый номер события в сообщении, 3 это id события, а ⬜ это статусы, перечисленные через запятую.

Если событий на эту дату становится больше 10, то остальные события размещаются на других страницах. Максимум 10 событий на одну страницу. Кнопки переключения страниц появляются под кнопками управления и пронумерованы номерами страниц.

Порядок расположения событий в сообщении можно изменить в настройках. По умолчанию события располагаются по возрастанию id (от малого к большему).

Кнопки управления:
➕ - Добавить событие.
📝 - Редактировать текст события.
🏷 - Изменить статус события.
🗑 - Удалить событие.
🔙 - Назад.
  &lt;   - Перелистнуть на один день назад.
  >   - Перелистнуть на один день вперёд.
🔄 - Обновить сообщение.
Если у вас есть события с повторяющимися статусами на этот день, то ниже основной клавиатуры и кнопок страниц появится кнопка "📅" для просмотра списка таких событий. Кнопка "↖️" позволяет открыть сообщение на дату этого события.

Для вызова сообщения, вы можете нажать кнопку в календаре или использовать команду /today.
""",
                "en": """
<u>Types of messages > <b>1 day</b></u>

The message displays events for a single day.

The line with information about the event is situated one line higher than the text of the event.
For example: <pre>1.3.⬜</pre>
Here 1 is the index number of the events in the message, 3 is the event id, and ⬜ are the statuses separated by commas.

If the number of events for this date exceeds 10, the remaining events are placed on other pages. There cannot be more than 10 events on one page. Page navigation buttons are displayed below the control buttons and are numbered accordingly.

The order of events in the message can be changed in the settings. By default, events are arranged in ascending order of their id (from small to large).

Control buttons:
➕ - Add an event.
📝 - Edit the event text.
🏷 - Change the event status.
🗑 - Delete an event.
🔙 - Go back.
  &lt;   - Navigate one day back.
  >   - Navigate one day forward.
🔄 - Refresh the message.
If you have events with recurring statuses on this day, below the main keyboard and page navigation buttons there will be a "📅" button to view a list of such events. The "↖️" button allows you to open the message for the date of that event.

To access the message, you can press the button in the calendar or use the command /today.
""",
            },
            "7_days": {
                "ru": """
<u>Виды сообщений > <b>7 дней</b></u>

Отображает события на ближайшие 7 дней.

Вызывается командой /week_event_list.
""",
                "en": """
<u>Types of messages > <b>7 days</b></u>

Displays events for the next 7 days.

Called by the command /week_event_list.
""",
            },
            "Settings": {
                "ru": """
<u>Виды сообщений > <b>Настройки</b></u>

Вызываются командой /settings.
Сообщение позволяет изменить настройки пользователя.

Чтобы изменить город, нужно ответить на сообщение с настройками от бота с названием города.
Город используется для запроса текущей погоды (/weather) и прогноза погоды (/forecast).

Часовой пояс используется для определения времени у пользователя.
""",
                "en": """
<u>Types of messages > <b>Settings</b></u>

Called by the command /settings.
This message allows users to modify their settings.

To change the city, you need to reply to the bots message containing the city name settings.
The city is used for requesting the current weather (/weather) and weather forecast (/forecast).

The time zone is used to determine the user's local time.
""",
            },
            "Basket": {
                "ru": """
<u>Виды сообщений > <b>Корзина</b></u>

Обычные пользователи могут только удалить своё событие навсегда.
Премиум-пользователям дополнительно доступна возможность переместить событие в корзину.
<b>События в корзине хранятся не более 30 дней!</b>

В корзине есть возможность восстановить событие на прежнюю дату.
""",
                "en": """
<u>Types of messages > <b>Basket</b></u>

Regular users can only delete their event permanently.
Premium users additionally have the option to move the event to the trash.
<b>Events in the trash are stored for no more than 30 days!</b>

In the trash basket, there is an option to restore the event to its original date.
""",
            },
            "Search": {
                "ru": """
<u>Виды сообщений > <b>Поиск</b></u>

Вы можете искать события, написав боту сообщение по следующему шаблону:
#&lt;поисковый запрос> или /search &lt;поисковый запрос>

<b>Обратите внимание, регистр поискового запроса важен!</b>

Бот ищет по вхождению слова в текст, дату и статус.
Он выдаёт все события, в которых есть совпадения.

Например, запрос <code>#03.05. Музыка</code> выдаст все события, в которых дата 3 мая и они содержат слово "Музыка".

# TODO Планируется расширение возможностей поисковых запросов.
""",
                "en": """
<u>Types of messages > <b>Search</b></u>

You can search for events by sending a message to the bot using the following template:
#&lt;search query> or /search &lt;search query>

<b>Please note that the search query is case-sensitive!</b>

The bot looks for occurrences of the word in the text, date and status.
It returns all events that have matches.

For example, the request <code>#03.05. Music</code> will return all events that have the date 3rd May and contain the word "Music".

# TODO Expanding the capabilities of search queries is planned.
""",
            },
            "Notifications": {
                "ru": """
<u>Виды сообщений > <b>Уведомления</b></u>

По умолчанию уведомления отключены.
Вы можете включить и изменить время уведомлений в настройках (/settings).
Бот уведомляет о важных "🟥" событиях, событиях с повторяющимся статусом ("📬", "📅", "🗞", "📆") и событиях со статусом "🔔".
""",
                "en": """
<u>Types of messages > <b>Notifications</b></u>

Notifications are disabled by default.
You can enable and customize the notification time in the settings (/settings).
The bot notifies about important "🟥" events, events with recurring status ("📬", "📅", "🗞", "📆"), and events with the status "🔔".
""",
            },
            "BotNews": {
                "ru": """
<u><b>Новости бота</b></u>

▪️ .
""",
                "en": """
<u><b>Bot News</b></u>

▪️ .
""",
            },
            "BotVersion": {
                "ru": f"""
<b>Версия бота</b>

<pre><code class='language-версия'>{config.__version__}{config.string_branch}</code></pre>
""",
                "en": f"""
<b>Bot Version</b>

<pre><code class='language-version'>{config.__version__}{config.string_branch}</code></pre>
""",
            },
            "CommandOpen": {
                "ru": """
<u>Команды бота > <b>/open</b></u>

<b>Daily message</b>
/open_today[_page_&lt;page&gt;]
/open_now[_page_&lt;page&gt;]

<b>Monthly/Yearly calendar message</b>
/open_calendar
/open_calendar_year

<b>Help message</b>
/open_help

<b>Open</b>
/open[_&lt;year&gt;[_&lt;month&gt;[_&lt;day&gt;[_page_&lt;page&gt;]]]]
""",
                "en": """
<u>Bot commands > <b>/open</b></u>

<b>Daily message</b>
/open_today[_page_&lt;page&gt;]
/open_now[_page_&lt;page&gt;]

<b>Monthly calendar message</b>
/open_calendar

<b>Yearly calendar message</b>
/open_calendar_year

<b>Help message</b>
/open_help

<b>Open</b>
/open[_&lt;year&gt;[_&lt;month&gt;[_&lt;day&gt;[_page_&lt;page&gt;]]]]
""",
            },
        },
        "weather": {
            "ru": """{} {} <u>{}</u>
Местное время <b>{}</b>
Измерения от ⠀<b>{}</b>
<b>{}°C</b>, ощущается как <b>{}°C</b>.
Ветер 💨 <b>{} м/с</b>, направление {} (<b>{}°</b>)
Восход <b>{}</b>
Закат⠀ <b>{}</b>
Видимость <b>{}</b>м""",
            "en": """{} {} <u>{}</u>
Local time <b>{}</b>
Measurements from⠀<b>{}</b>
<b>{}°C</b>, feels like <b>{}°C</b>.
Wind 💨 <b>{} m/s</b>, direction {} (<b>{}°</b>)
Sunrise <b>{}</b>
Sunset⠀<b>{}</b>
Visibility <b>{}</b>m""",
        },
        "search": {
            "ru": "Поиск",
            "en": "Search",
        },
        "basket": {
            "ru": "Корзина",
            "en": "Basket",
        },
        "reminder": {
            "ru": "Напоминание",
            "en": "Notification",
        },
        "menu": {
            "ru": (
                "Меню",
                "Помощь",
                "Календарь",
                "Аккаунт",
                "Группы",
                "7 дней",
                "Уведомления",
                "Поиск",
                "Настройки",
                "Корзина",
                "Группа",
            ),
            "en": (
                "Menu",
                "Help",
                "Calendar",
                "Account",
                "Groups",
                "7 days",
                "Notifications",
                "Search",
                "Settings",
                "Bin",
                "Group",
            ),
        },
        "limit": {
            "ru": "Лимит на",
            "en": "Limit for",
        },
        "frequently_used_dates": {
            "ru": "Нажмите чтобы закрепить",
            "en": "Press for pin",
        },
    },
    "buttons": {
        "commands": {
            "not_login": {
                "user": {
                    "ru": [
                        BotCommand("start", "Старт"),
                        BotCommand("login", "<username> <password>"),
                        BotCommand("signup", "<email> <username> <password>"),
                    ],
                    "en": [
                        BotCommand("start", "Start"),
                        BotCommand("login", "<username> <password>"),
                        BotCommand("signup", "<email> <username> <password>"),
                    ],
                },
                "member": {
                    "ru": [
                        BotCommand("start", "Старт"),
                    ],
                    "en": [
                        BotCommand("start", "Start"),
                    ],
                },
            },
            "-1": {
                "user": {
                    "ru": [
                        BotCommand("_", "Вы забанены"),
                    ],
                    "en": [
                        BotCommand("_", "You are banned"),
                    ],
                },
                "member": {
                    "ru": [
                        BotCommand("_", "Вы забанены"),
                    ],
                    "en": [
                        BotCommand("_", "You are banned"),
                    ],
                },
            },
            "0": {
                "user": {
                    "ru": [
                        BotCommand("start", "Старт"),
                        BotCommand("menu", "Меню"),
                        BotCommand("calendar", "Календарь"),
                        BotCommand("today", "Вызвать сообщение с сегодняшним днём"),
                        BotCommand("weather", "{city} Погода"),
                        BotCommand("forecast", "{city} Прогноз погоды на 5 дней"),
                        BotCommand("week_event_list", "События в ближайшие 7 дней"),
                        BotCommand("dice", "Кинуть кубик"),
                        BotCommand(
                            "export",
                            "{format} Сохранить мои данные в формат. (csv, xml, json, jsonl)",
                        ),
                        BotCommand("help", "Помощь"),
                        BotCommand("settings", "Настройки"),
                        BotCommand("account", "Аккаунт"),
                        BotCommand("groups", "Группы"),
                        BotCommand("logout", "Выйти из аккаунта"),
                    ],
                    "en": [
                        BotCommand("start", "Start"),
                        BotCommand("menu", "Menu"),
                        BotCommand("calendar", "Calendar"),
                        BotCommand("today", "Today's message"),
                        BotCommand("weather", "{city} Weather"),
                        BotCommand("forecast", "{city} Weather forecast for 5 days"),
                        BotCommand("week_event_list", "Weekly events"),
                        BotCommand("dice", "Roll the dice (randomizer)"),
                        BotCommand(
                            "export",
                            "{format} Save my data in format. (csv, xml, json, jsonl)",
                        ),
                        BotCommand("help", "Help"),
                        BotCommand("settings", "Settings"),
                        BotCommand("account", "Account"),
                        BotCommand("groups", "Groups"),
                        BotCommand("logout", "Logout"),
                    ],
                },
                "member": {
                    "ru": [
                        BotCommand("start", "Старт"),
                        BotCommand("menu", "Меню"),
                        BotCommand("calendar", "Календарь"),
                        BotCommand("today", "Вызвать сообщение с сегодняшним днём"),
                        BotCommand("weather", "{city} Погода"),
                        BotCommand("forecast", "{city} Прогноз погоды на 5 дней"),
                        BotCommand("week_event_list", "События в ближайшие 7 дней"),
                        BotCommand("dice", "Кинуть кубик"),
                        BotCommand(
                            "export",
                            "{format} Сохранить мои данные в формат. (csv, xml, json, jsonl)",
                        ),
                        BotCommand("help", "Помощь"),
                        BotCommand("settings", "Настройки"),
                    ],
                    "en": [
                        BotCommand("start", "Start"),
                        BotCommand("menu", "Menu"),
                        BotCommand("calendar", "Calendar"),
                        BotCommand("today", "Today's message"),
                        BotCommand("weather", "{city} Weather"),
                        BotCommand("forecast", "{city} Weather forecast for 5 days"),
                        BotCommand("week_event_list", "Weekly events"),
                        BotCommand("dice", "Roll the dice (randomizer)"),
                        BotCommand(
                            "export",
                            "{format} Save my data in format. (csv, xml, json, jsonl)",
                        ),
                        BotCommand("help", "Help"),
                        BotCommand("settings", "Settings"),
                    ],
                },
            },
            "1": {
                "user": {
                    "ru": [
                        BotCommand("start", "Старт"),
                        BotCommand("menu", "Меню"),
                        BotCommand("calendar", "Календарь"),
                        BotCommand("today", "Вызвать сообщение с сегодняшним днём"),
                        BotCommand("weather", "{city} Погода"),
                        BotCommand("forecast", "{city} Прогноз погоды на 5 дней"),
                        BotCommand("week_event_list", "События в ближайшие 7 дней"),
                        BotCommand("dice", "Кинуть кубик"),
                        BotCommand(
                            "export",
                            "{format} Сохранить мои данные в формат. (csv, xml, json, jsonl)",
                        ),
                        BotCommand("help", "Помощь"),
                        BotCommand("settings", "Настройки"),
                        BotCommand("account", "Аккаунт"),
                        BotCommand("groups", "Группы"),
                        BotCommand("logout", "Выйти из аккаунта"),
                    ],
                    "en": [
                        BotCommand("start", "Start"),
                        BotCommand("menu", "Menu"),
                        BotCommand("calendar", "Calendar"),
                        BotCommand("today", "Today's message"),
                        BotCommand("weather", "{city} Weather"),
                        BotCommand("forecast", "{city} Weather forecast for 5 days"),
                        BotCommand("week_event_list", "Weekly events"),
                        BotCommand("dice", "Roll the dice (randomizer)"),
                        BotCommand(
                            "export",
                            "{format} Save my data in format. (csv, xml, json, jsonl)",
                        ),
                        BotCommand("help", "Help"),
                        BotCommand("settings", "Settings"),
                        BotCommand("account", "Account"),
                        BotCommand("groups", "Groups"),
                        BotCommand("logout", "Logout"),
                    ],
                },
                "member": {
                    "ru": [
                        BotCommand("start", "Старт"),
                        BotCommand("menu", "Меню"),
                        BotCommand("calendar", "Календарь"),
                        BotCommand("today", "Вызвать сообщение с сегодняшним днём"),
                        BotCommand("weather", "{city} Погода"),
                        BotCommand("forecast", "{city} Прогноз погоды на 5 дней"),
                        BotCommand("week_event_list", "События в ближайшие 7 дней"),
                        BotCommand("dice", "Кинуть кубик"),
                        BotCommand(
                            "export",
                            "{format} Сохранить мои данные в формат. (csv, xml, json, jsonl)",
                        ),
                        BotCommand("help", "Помощь"),
                        BotCommand("settings", "Настройки"),
                    ],
                    "en": [
                        BotCommand("start", "Start"),
                        BotCommand("menu", "Menu"),
                        BotCommand("calendar", "Calendar"),
                        BotCommand("today", "Today's message"),
                        BotCommand("weather", "{city} Weather"),
                        BotCommand("forecast", "{city} Weather forecast for 5 days"),
                        BotCommand("week_event_list", "Weekly events"),
                        BotCommand("dice", "Roll the dice (randomizer)"),
                        BotCommand(
                            "export",
                            "{format} Save my data in format. (csv, xml, json, jsonl)",
                        ),
                        BotCommand("help", "Help"),
                        BotCommand("settings", "Settings"),
                    ],
                },
            },
            "2": {
                "user": {
                    "ru": [
                        BotCommand("start", "Старт"),
                        BotCommand("menu", "Меню"),
                        BotCommand("calendar", "Календарь"),
                        BotCommand("today", "Вызвать сообщение с сегодняшним днём"),
                        BotCommand("weather", "{city} Погода"),
                        BotCommand("forecast", "{city} Прогноз погоды на 5 дней"),
                        BotCommand("week_event_list", "События в ближайшие 7 дней"),
                        BotCommand("dice", "Кинуть кубик"),
                        BotCommand(
                            "export",
                            "{format} Сохранить мои данные в формат. (csv, xml, json, jsonl)",
                        ),
                        BotCommand("help", "Помощь"),
                        BotCommand("settings", "Настройки"),
                        BotCommand("account", "Аккаунт"),
                        BotCommand("groups", "Группы"),
                        BotCommand("commands", "Список команд"),
                        BotCommand("logout", "Выйти из аккаунта"),
                    ],
                    "en": [
                        BotCommand("start", "Start"),
                        BotCommand("menu", "Menu"),
                        BotCommand("calendar", "Calendar"),
                        BotCommand("today", "Today's message"),
                        BotCommand("weather", "{city} Weather"),
                        BotCommand("forecast", "{city} Weather forecast for 5 days"),
                        BotCommand("week_event_list", "Weekly events"),
                        BotCommand("dice", "Roll the dice (randomizer)"),
                        BotCommand(
                            "export",
                            "{format} Save my data in format. (csv, xml, json, jsonl)",
                        ),
                        BotCommand("help", "Help"),
                        BotCommand("settings", "Settings"),
                        BotCommand("account", "Account"),
                        BotCommand("groups", "Groups"),
                        BotCommand("commands", "Command list"),
                        BotCommand("logout", "Logout"),
                    ],
                },
                "member": {
                    "ru": [
                        BotCommand("start", "Старт"),
                        BotCommand("menu", "Меню"),
                        BotCommand("calendar", "Календарь"),
                        BotCommand("today", "Вызвать сообщение с сегодняшним днём"),
                        BotCommand("weather", "{city} Погода"),
                        BotCommand("forecast", "{city} Прогноз погоды на 5 дней"),
                        BotCommand("week_event_list", "События в ближайшие 7 дней"),
                        BotCommand("dice", "Кинуть кубик"),
                        BotCommand(
                            "export",
                            "{format} Сохранить мои данные в формат. (csv, xml, json, jsonl)",
                        ),
                        BotCommand("help", "Помощь"),
                        BotCommand("settings", "Настройки"),
                        BotCommand("commands", "Список команд"),
                    ],
                    "en": [
                        BotCommand("start", "Start"),
                        BotCommand("menu", "Menu"),
                        BotCommand("calendar", "Calendar"),
                        BotCommand("today", "Today's message"),
                        BotCommand("weather", "{city} Weather"),
                        BotCommand("forecast", "{city} Weather forecast for 5 days"),
                        BotCommand("week_event_list", "Weekly events"),
                        BotCommand("dice", "Roll the dice (randomizer)"),
                        BotCommand(
                            "export",
                            "{format} Save my data in format. (csv, xml, json, jsonl)",
                        ),
                        BotCommand("help", "Help"),
                        BotCommand("settings", "Settings"),
                        BotCommand("commands", "Command list"),
                    ],
                },
            },
        },
        "select_status": {
            "folders": {
                "ru": (
                    (("🗂 Важность", "1"),),
                    (("🗂 Разное", "2"),),
                    (
                        ("🗂 Эффекты", "3"),
                        ("🗂 Кастомные", "4"),
                    ),
                ),
                "en": (
                    (("🗂 Importance", "1"),),
                    (("🗂 Miscellaneous", "2"),),
                    (
                        ("🗂 Effects", "3"),
                        ("🗂 Custom", "4"),
                    ),
                ),
            },
            "1": {
                "ru": (
                    (
                        "⬜ Без статуса",
                        "✅ Сделано",
                    ),
                    (
                        "🟥 Важно",
                        "🟨 Сделано не полностью",
                    ),
                    (
                        "⭐️ Важно",
                        "🤨 Не уверен",
                    ),
                    (
                        "🟧 Важно но не так",
                        "💡 Идея",
                    ),
                ),
                "en": (
                    (
                        "⬜ No Status",
                        "✅ Done",
                    ),
                    (
                        "🟥 Important",
                        "🟨 Not completely done",
                    ),
                    (
                        "⭐️ Important",
                        "🤨 Not sure",
                    ),
                    (
                        "🟧 Not so important",
                        "💡 Idea",
                    ),
                ),
            },
            "2": {
                "ru": (
                    (
                        "🎧 Музыка",
                        "📚 Книга",
                    ),
                    (
                        "🎬 Фильм",
                        "📺 Видео",
                    ),
                    (
                        "🖼 Фотография",
                        "🎮 Игра",
                    ),
                    (
                        "🎁 Подарок",
                        "❓ Вопрос",
                    ),
                    (
                        "🧾 Рецепт",
                        "📌 Закрепить",
                    ),
                    (
                        "🛒 План покупок",
                        "⏱ В процессе",
                    ),
                    (
                        "📋 План",
                        "🗺 Путешествия",
                    ),
                ),
                "en": (
                    (
                        "🎧 Music",
                        "📚 Book",
                    ),
                    (
                        "🎬 Movie",
                        "📺 Video",
                    ),
                    (
                        "🖼 Photography",
                        "🎮 Game",
                    ),
                    (
                        "🎁 Present",
                        "❓ Question",
                    ),
                    (
                        "🧾 Recipe",
                        "📌 Pin",
                    ),
                    (
                        "🛒 Shopping Plan",
                        "⏱ In Progress",
                    ),
                    (
                        "📋 Plan",
                        "🗺 Travel",
                    ),
                ),
            },
            "3": {
                "ru": (
                    (
                        "🗒 Список (ставит ▪️)",
                        "🧮 Порядковый список (1️⃣, 2️⃣ и т д)",
                    ),
                    (
                        "💻 Код⠀",
                        "🪞 Скрыто",
                        "💬 Цитата",
                    ),
                    (
                        "🎉 День рождения",
                        "🎊 Праздник",
                        "🪩 Один праздник",
                    ),
                    (
                        "🔗 Ссылка",
                        "⛓ Без сокращения ссылок",
                    ),
                    ("📆 Повторение каждый год",),
                    ("📅 Повторение каждый месяц",),
                    ("🗞 Повторение каждую неделю",),
                    ("📬 Повторение каждый день",),
                    ("🔕 Выключить уведомления",),
                ),
                "en": (
                    (
                        "🗒 List (puts ▪️)",
                        "🧮 Ordinal list (1️⃣, 2️⃣ etc)",
                    ),
                    (
                        "💻 Code",
                        "🪞 Hidden",
                        "💬 Quote",
                    ),
                    (
                        "🎉 Birthday",
                        "🎊 Holiday",
                        "🪩 One feast",
                    ),
                    (
                        "🔗 Link",
                        "⛓ No link shortening",
                    ),
                    ("📆 Repeat every year",),
                    ("📅 Repeat every month",),
                    ("🗞 Repeat every week",),
                    ("📬 Repeat every day",),
                    ("🔕 Turn off notifications",),
                ),
            },
            "4": {
                "ru": (
                    (
                        "💻py Python",
                        "💻cpp C++",
                        "💻c C",
                    ),
                    (
                        "💻cs C#",
                        "💻html HTML",
                        "💻css CSS",
                    ),
                    (
                        "💻js JavaScript",
                        "💻ts TypeScript",
                    ),
                    (
                        "💻java Java",
                        "💻swift Swift",
                        "💻kt Kotlin",
                    ),
                    (
                        "💻go Go",
                        "💻rs Rust",
                        "💻rb Ruby",
                    ),
                    (
                        "💻sql SQL",
                        "💻re RegExp",
                        "💻sh Shell | Bash",
                    ),
                    (
                        "💻yaml YAML",
                        "💻json JSON",
                        "💻xml XML",
                    ),
                    (
                        "💻toml TOML",
                        "💻ini INI",
                        "💻csv CSV",
                    ),
                    (
                        "💻ebnf EBNF",
                        "💻diff GIT DIFF",
                    ),
                ),
                "en": (
                    (
                        "💻py Python",
                        "💻cpp C++",
                        "💻c C",
                        "💻cs C#",
                    ),
                    (
                        "💻js JavaScript",
                        "💻html HTML",
                        "💻css CSS",
                        "💻ts TypeScript",
                    ),
                    (
                        "💻java Java",
                        "💻swift Swift",
                        "💻kt Kotlin",
                    ),
                    (
                        "💻go Go",
                        "💻rs Rust",
                        "💻rb Ruby",
                    ),
                    (
                        "💻sql SQL",
                        "💻re RegExp",
                        "💻sh Shell | Bash",
                    ),
                    (
                        "💻yaml YAML",
                        "💻json JSON",
                        "💻xml XML",
                    ),
                    (
                        "💻toml TOML",
                        "💻ini INI",
                        "💻csv CSV",
                    ),
                    (
                        "💻ebnf EBNF",
                        "💻diff GIT DIFF",
                    ),
                ),
            },
        },
    },
    "errors": {
        "success": {
            "ru": "Успешно",
            "en": "Success",
        },
        "failure": {
            "ru": "Неудача",
            "en": "Failure",
        },
        "email_is_taken": {
            "ru": "Этот адрес электронной почты уже занят",
            "en": "This email is already taken",
        },
        "wrong_username": {
            "ru": """
Неверное имя пользователя
Длина от 4 до 31 символов.
Только латинские буквы, цифры и подчёркивания.
Не начинать с цифры.
Не использовать подряд два подчёркивания.
""",
            "en": """
Wrong username
Length from 4 to 31 characters.
Use only Latin letters, numbers, and underscores.
Cannot start with a number.
Cannot have two underscores in a row.
""",
        },
        "wrong_email": {
            "ru": "Неправильный адрес электронной почты",
            "en": "Wrong email",
        },
        "incorrect_password": {
            "ru": "Неверный пароль",
            "en": "Incorrect password",
        },
        "password_too_easy": {
            "ru": "Пароль слишком лёгкий",
            "en": "The password is too easy",
        },
        "username_is_taken": {
            "ru": "Это имя пользователя занято",
            "en": "This username is taken",
        },
        "account_not_found": {
            "ru": "Аккаунт не найден",
            "en": "Account not found",
        },
        "not_enough_permissions": {
            "ru": "Недостаточно полномочий",
            "en": "Not enough permissions",
        },
        "forbidden_to_log_account_in_group": {
            "ru": "В группе нельзя войти в аккаунт",
            "en": "You can't log into your account in a group",
        },
        "forbidden_to_log_group": {
            "ru": "Эта телеграм группа не присоединена к группе пользователя",
            "en": "This telegram group is not connected to the user's group",
        },
        "already_connected_group": {
            "ru": "Эта телеграм группа уже присоединена к группе пользователя",
            "en": "This telegram group is already connected to the user's group",
        },
        "no_account": {
            "ru": """
Вы не вошли в аккаунт. Войдите
<code>/login </code>&lt;username&gt; &lt;password&gt;
или создайте аккаунт
<code>/signup </code>&lt;email&gt; &lt;username&gt; &lt;password&gt;
""",
            "en": """
You are not logged in to your account. Login
<code>/login </code>&lt;username&gt; &lt;password&gt;
or create an account
<code>/signup </code>&lt;email&gt; &lt;username&gt; &lt;password&gt;
""",
        },
        "many_attempts": {
            "ru": "Извините, слишком много обращений. Пожалуйста, повторите попытку через {} секунд.",
            "en": "Sorry, too many requests. Please try again in {} seconds.",
        },
        "many_attempts_weather": {
            "ru": "Погоду запрашивали слишком часто. Повторите через {} секунд.",
            "en": "The weather was requested too often. Retry in {} seconds.",
        },
        "error": {
            "ru": "Произошла ошибка",
            "en": "An error has occurred",
        },
        "file_is_too_big": {
            "ru": "Возникла ошибка. Возможно файл слишком большой 🫤",
            "en": "An error has occurred. Maybe the file is too big 🫤",
        },
        "export": {
            "ru": "Нельзя так часто экспортировать данные\n"
            "Подождите ещё <b>{t} минут</b>",
            "en": "You can't export data so often\nPlease wait <b>{t} minutes</b>",
        },
        "export_format": {
            "ru": "Неверный формат. Выбери из (csv, xml, json, jsonl)",
            "en": "Wrong format. Choose from (csv, xml, json, jsonl)",
        },
        "export_empty": {
            "ru": "В этой группе не было ни одного события",
            "en": "There were no events in this group.",
        },
        "deleted": {
            "ru": "Извините, вам эта команда не доступна",
            "en": "Sorry, this command is not available for you",
        },
        "no_events_to_interact": {
            "ru": "Нет событий для взаимодействия",
            "en": "No events to interact",
        },
        "already_on_this_page": {
            "ru": "Вы уже находитесь на этой странице",
            "en": "You are already on this page",
        },
        "status_already_posted": {
            "ru": "Статус уже стоит на событии",
            "en": "Status is already posted on event",
        },
        "more_5_statuses": {
            "ru": "Нельзя ставить больше 5 статусов",
            "en": "You can not put more than 5 statuses",
        },
        "message_is_too_long": {
            "ru": "Сообщение слишком большое",
            "en": "Message is too long",
        },
        "change_information_is_too_long": {
            "ru": "Информация об изменениях слишком длинная",
            "en": "The change information is too long",
        },
        "exceeded_limit": {
            "ru": "Вы превысили дневной лимит.\n"
            "Уменьшите количество символов или удалите не нужные события.",
            "en": "You have exceeded the daily limit.\n"
            "Reduce the number of characters or remove unnecessary events.",
        },
        "limit_exceeded": {
            "ru": "Превышен лимит",
            "en": "Limit exceeded",
        },
        "message_empty": {
            "ru": "🕸  Здесь пусто🕷  🕸",
            "en": "🕸  It's empty here🕷  🕸",
        },
        "request_empty": {
            "ru": "Запрос пустой :/",
            "en": "Request is empty :/",
        },
        "invalid_request": {
            "ru": "Ошибка в запросе",
            "en": "Error in request",
        },
        "nothing_found": {
            "ru": "🕸  Ничего не нашлось🕷  🕸",
            "en": "🕸  Nothing has found🕷  🕸",
        },
        "get_permission": {
            "ru": "Пожалуйста, выдайте боту <b>права удалять сообщения</b>, чтобы сохранять чат в чистоте",
            "en": "Please give the bot <b>permission to delete messages</b> to keep the chat clean",
        },
        "delete_messages_older_48_h": {
            "ru": "Из-за ограничений Telegram бот не может удалять сообщения <b>старше 48 часов</b>.",
            "en": "Due to Telegram restrictions, the bot cannot delete messages <b>older than 48 hours</b>.",
        },
        "weather_invalid_city_name": {
            "ru": "Ошибка. Несуществующее название города.\n"
            "Попробуйте ещё раз /weather {город}",
            "en": "Error. Invalid city name.\nTry again /weather {city}",
        },
        "forecast_invalid_city_name": {
            "ru": "Ошибка. Несуществующее название города.\n"
            "Попробуйте ещё раз /forecast {город}",
            "en": "Error. Invalid city name.\nTry again /forecast {city}",
        },
        "nodata": {
            "ru": "👀 На эту дату у вас нет событий",
            "en": "👀 You have no events for this date",
        },
        "invalid_date": {
            "ru": "Недействительная дата!",
            "en": "Invalid date!",
        },
        "settings": {
            "commit_changes": {
                "ru": "Вы не сохранили настройки! Нажмите 💾 чтобы сохранить",
                "en": "You have not saved your settings! Click 💾 to save",
            },
        },
        "bin": {
            "confirmation_of_purification": {
                "ru": "Вы действительно хотите безвозвратно удалить события в корзине? Нажмите повторно для удаления событий в корзине",
                "en": "Are you sure you want to permanently delete the events in your trash? Click again to delete the events in your trash",
            },
        },
        "event": {
            "commit_clear_history": {
                "ru": "Вы действительно хотите удалить историю изменений события? Нажмите повторно для удаления истории изменений",
                "en": "Are you sure you want to clear the event's change history? Click again to clear change history",
            },
        },
        "confirmation_of_deletion": {
            "event": {
                "ru": "Вы действительно хотите безвозвратно удалить событие? Нажмите повторно для удаления события",
                "en": "Are you sure you want to permanently delete the event? Click again to permanently delete the event",
            },
            "events": {
                "ru": "Вы действительно хотите безвозвратно удалить события? Нажмите повторно для удаления событий",
                "en": "Are you sure you want to permanently delete events? Click again to permanently delete events",
            },
        },
    },
    "select": {
        "status_to_event": {
            "ru": "Выберите статус для события:",
            "en": "Select a status for the event:",
        },
        "notification_date": {
            "ru": "Выберите дату уведомления",
            "en": "Select notification date",
        },
        "event_to_open": {
            "ru": "Выберите событие для открытия",
            "en": "Select an event to open",
        },
        "event": {
            "ru": "Выберите событие",
            "en": "Choose an event",
        },
        "events": {
            "ru": "Выберите события",
            "en": "Choose an events",
        },
        "date": {
            "ru": "Выберите дату",
            "en": "Select a date",
        },
        "new_date": {
            "ru": "Выберите новую дату для события",
            "en": "Select a new date for the event",
        },
        "what_do_with_event": {
            "ru": "Выберите, что сделать с событием",
            "en": "Choose what to do with the event",
        },
        "what_do_with_events": {
            "ru": "Выберите, что сделать с событиями",
            "en": "Choose what to do with the events",
        },
        "events_new_date": {
            "ru": "Выберите новую дату для этих событий",
            "en": "Please select a new date for these events",
        },
    },
}


def get_translate(target: str, lang_iso: str | None = None) -> str | Any:
    """
    Взять перевод из файла lang.py c нужным языком
    """
    result: dict = translation
    for key in target.split("."):
        result = result[key]

    lang_iso: str = lang_iso or (
        request.entity.settings.lang if request.entity else "en"
    )

    try:
        return result[lang_iso]
    except KeyError:
        return result["en"]


def get_theme_emoji(target: Literal["back", "add", "del"]) -> str:
    """
    back

    add
    """
    theme: int = request.entity.settings.theme
    match target:
        case "back":
            match theme:
                case 1:
                    return "⬅️"
                case _:
                    return "🔙"
        case "add":
            match theme:
                case 1:
                    return "🞣"
                case _:
                    return "➕"
        case "del":
            match theme:
                case 1:
                    return "✕"
                case _:
                    return "✖️"

    return ""
