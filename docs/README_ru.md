<table>
    <td><a href="/README.md">EN</a></td>
    <td><a href="/docs/README_ru.md">RU</a></td>
</table>

[![GitHub Actions Workflow Status](https://github.com/EgorKhabarov/TODO-bot/actions/workflows/tests.yml/badge.svg)](https://github.com/EgorKhabarov/TODO-bot/actions/workflows/tests.yml)

[![Telegram](https://egorkhabarov.github.io/resources/badges/Telegram.svg)](https://t.me/NotesAssistantBot)
[![UptimeRobot Status](https://img.shields.io/uptimerobot/status/m796658291-a3b1e18d0d9b2662434240e6)](https://uptimerobot.com/)

# NotesAssistant
### Бот для организации заметок в Telegram
Хранение, добавление, редактирование и удаление заметки по дате.
Можно пометить заметку с помощью эмодзи.
Удобный поиск по эмодзи статусам и датам.
Дни рождения и праздники помечаются на календаре (нужно поставить эмодзи статус).

# Инструкция по установке

### Установка

```shell
git clone https://github.com/EgorKhabarov/NotesAssistant
cd NotesAssistant
cp config.example.yaml config.yaml
pip install -r requirements.txt
```

### Настройка

Измените `config.yaml`

```.env
BOT_TOKEN: ""        # Telegram bot token from https://t.me/BotFather
WEATHER_API_KEY: ""  # Get it from https://home.openweathermap.org/api_keys
```

Set up a bot at [https://t.me/BotFather](https://t.me/BotFather)

`/mybots` -> `@your_bot_username`
```
Bot Settings -> Group Privacy -> disabled
Bot Settings -> Inline Mode   -> disabled
```

### Запуск
Только бота
```shell
python start_bot.py
```
Сервер
```shell
python -c "from server import app;app.run('0.0.0.0')"
```

### Получение прав админа

#### Получите свой telegram **chat_id**

Запустите бота и отправьте команду `/id`.
Добавьте полученный `chat_id` в `ADMIN_IDS` в `config.yaml` и перезагрузите бота.

> [!IMPORTANT]
> Добавляйте только chat_id личных аккаунтов (приватных чатов)!
> Любое взаимодействие любого участника группы в Telegram с ботом воспринимается как осуществляемое от имени группы.

### Настройка PythonAnywhere

- Создайте веб-сервер, используя последнюю доступную версию Python
- В категории `Code` изменить `Working directory` на путь до папки с `server.py`
- В категории `Security` изменить `Force HTTPS` на `Enabled`

### Docker

```shell
docker build -t NotesAssistant .
docker volume create NotesAssistantData
docker volume create NotesAssistantLogs
docker run -p 5000:5000 -v NotesAssistantData:/app/data -v NotesAssistantLogs:/app/logs --name NotesAssistantContainer NotesAssistant
```

---

# Команды

- [/start](#start)
- [/menu](#menu)
  - [/help](#help)
  - [/calendar](#calendar)
  - [account](#account)
  - [groups](#groups)
  - [/week_event_list](#week_event_list)
  - [notifications](#notifications)
  - [/settings](#settings)
  - [trash](#trash)
- [/calendar](#calendar)
- [/today](#today)
- [/week_event_list](#week_event_list)
- [/export](#export)


## start

Здоровается с пользователем.

| Кнопки               | Действия                                   |
|:---------------------|--------------------------------------------|
| <kbd>/menu</kbd>     | То же самое что команда `/menu`            |
| <kbd>/calendar</kbd> | То же самое что команда `/calendar`        |


## menu

Навигация по функциям бота.

| Кнопки                    | Действия                                          |
|:--------------------------|---------------------------------------------------|
| <kbd>📚 Помощь</kbd>      | То же самое что команда `/help`                   |
| <kbd>📆 Календарь</kbd>   | То же самое что команда `/calendar`               |
| <kbd>👤 Аккаунт</kbd>     | Личный кабинет и экспорт данных                   |
| <kbd>👥 Группы</kbd>      | Настройки групп                                   |
| <kbd>📆 7 дней</kbd>      | События в ближайшие 7 дней                        |
| <kbd>🔔 Уведомления</kbd> | Посмотреть события, которые попадут в уведомление |
| <kbd>⚙️ Настройки</kbd>   | То же самое что команда `/settings`               |
| <kbd>🗑 Корзина</kbd>     | Корзина с удалёнными событиями (premium)          |


## help

Даёт доступ к информации о возможностях бота.


## calendar

Календарь.

<table>
    <tr><th colspan="7">Январь (1.2000) (Високосный 🐲) (52-5)</th></tr>
    <tr><th>  Пн </th><th> Вт! </th><th> Ср </th><th> Чт </th><th> Пт </th><th> Сб </th><th> Вс </th></tr>
    <tr><th>     </th><th>     </th><th>    </th><th>    </th><th>    </th><th><img alt="#1" src="https://img.shields.io/badge/%231-blue"></th><th>  2 </th></tr>
    <tr><th>   3 </th><th><img alt="4!*" src="https://img.shields.io/badge/4!*-green"></th><th>  5 </th><th><img alt="6³" src="https://img.shields.io/badge/6³-green"></th><th>  7 </th><th>  8 </th><th>  9 </th></tr>
    <tr><th> 10! </th><th>  11 </th><th> 12 </th><th> 13 </th><th> 14 </th><th> 15 </th><th> 16 </th></tr>
    <tr><th>  17 </th><th>  18 </th><th> 19 </th><th> 20 </th><th> 21 </th><th> 22 </th><th> 23 </th></tr>
    <tr><th>  24 </th><th>  25 </th><th> 26 </th><th> 27 </th><th> 28 </th><th> 29 </th><th> 30 </th></tr>
    <tr><th>  31 </th><th>     </th><th>    </th><th>    </th><th>    </th><th>    </th><th>    </th></tr>
    <tr><th colspan="2"><<</th><th><</th><th>⟳</th><th>></th><th colspan="2">>></th></tr>
    <tr><th colspan="4">🔙</th><th colspan="3">🗂</th></tr>
</table>


### Обозначения

#### Первая кнопка

При нажатии появляется календарь на год.

| Обозначение     | Значение                                |
|:----------------|-----------------------------------------|
| Январь          | Названия месяца                         |
| (1.2000)        | Номера месяца и года                    |
| (Високосный 🐲) | Високосный ли год и животное этого года |
| (52-5)          | Номера первой и последней недели        |


#### Дни недели

При нажатии ничего не делают.
Текст на кнопке может оканчиваться на символ `!`.
Это означает, что на этом дне недели есть повторяющиеся события с промежутком в неделю ([подробнее про статусы](#Cтатусы-событий)).


#### Кнопка на день

При нажатии вызывает [сообщение на один день](#сообщение-на-один-день)

| Знак | Обозначение                                                                                                                 |
|:----:|-----------------------------------------------------------------------------------------------------------------------------|
| `#`  | Сегодняшний день                                                                                                            |
| `*`  | В этот день есть события<br>Если событий меньше 10 то будет состоять из значков степени,<br>обозначающих количество событий |
| `!`  | В этот день есть важное событие<br>Например со статусом день рождения `🎉` или праздник `🎊`                                |


#### Кнопки навигации

|     Знак      | Обозначение                                 |
|:-------------:|---------------------------------------------|
| <kbd><<</kbd> | Показать календарь на **один год назад**    |
| <kbd><</kbd>  | Показать календарь на **один месяц назад**  |
| <kbd>⟳</kbd>  | Показать календарь на **текущую дату**      |
| <kbd>></kbd>  | Показать календарь на **один месяц вперёд** |
| <kbd>>></kbd> | Показать календарь на **один год вперёд**   |

> [!TIP]
> При нажатии на <kbd>⟳</kbd> в календаре открывается сегодняшняя дата.


#### Colors

| Цвет                                                           | Обозначение             |
|----------------------------------------------------------------|-------------------------|
| <img alt="4!*" src="https://img.shields.io/badge/blue-blue">   | Сегодня                 |
| <img alt="4!*" src="https://img.shields.io/badge/green-green"> | В этот день есть записи |


## account

Здесь вы можете изменить имя пользователя и пароль или выйти из своей учетной записи.
Вы также можете просмотреть свои лимиты <kbd>📊</kbd>.


## groups

Вы можете подключить группу к своему аккаунту в боте.

<table>
    <tr><th><kbd>🔸Все</kbd></th><th><kbd>Участник</kbd></th><th><kbd>Модератор</kbd></th><th><kbd>Администратор</kbd></th></tr>
    <tr><th colspan="4"><kbd>&lt;Название вашей первой группы&gt;</kbd></th></tr>
    <tr><th colspan="2"><kbd>🔙</kbd></th><th colspan="2"><kbd>👥 Создать группу</kbd></th></tr>
</table>


## week_event_list

Сообщение с заметками в ближайшие 7 дней.


## notifications

Сообщение с заметками на сегодня, завтра, послезавтра, послезавтра и через неделю.


## settings

Сообщение с настройками.

<table>
    <tr>
        <th><kbd>🗣 ru</kbd></th>
        <th><kbd>🔗 True</kbd></th>
        <th><kbd>⬆️</kbd></th>
        <th><kbd>🔕</kbd></th>
        <th><kbd>⬛️</kbd></th>
    </tr>
    <tr>
        <th><kbd>-3</kbd></th>
        <th><kbd>-1</kbd></th>
        <th><kbd>3 🌍</kbd></th>
        <th><kbd>+1</kbd></th>
        <th><kbd>+3</kbd></th>
    </tr>
    <tr>
        <th><kbd>-1h</kbd></th>
        <th><kbd>-10m</kbd></th>
        <th><kbd>08:00 ⏰</kbd></th>
        <th><kbd>+10m</kbd></th>
        <th><kbd>+1h</kbd></th>
    </tr>
    <tr><th colspan="5"><kbd>Настройки по умолчанию</kbd></th></tr>
</table>

|             Знак              | Обозначение                                                                                                                      |
|:-----------------------------:|:---------------------------------------------------------------------------------------------------------------------------------|
|         <kbd>🗣</kbd>         | Язык (по умолчанию `ru`)                                                                                                         |
|         <kbd>🔗</kbd>         | Сокращать ли ссылки (https://ru.wikipedia.org/wiki/Гиперссылка -> [ru.wikipedia.org](https://ru.wikipedia.org/wiki/Гиперссылка)) |
| <kbd>⬇️</kbd> / <kbd>⬆️</kbd> | Порядок сортировки событий                                                                                                       |                                                                                             |
|         <kbd>🔕</kbd>         | Включить ли уведомления (по умолчанию выключены)                                                                                 |
| <kbd>⬜️</kbd> / <kbd>⬛️</kbd> | Тема бота (заменяет тёмные смайлики на светлые)                                                                                  |
|         <kbd>🌍</kbd>         | Ваш часовой пояс                                                                                                                 |
|         <kbd>⏰</kbd>          | Время уведомления                                                                                                                |


## trash

Список удалённых событий.

| <kbd>🔼</kbd><br>Выбрать одно событие | <kbd>↕️</kbd><br>Выбрать несколько событий |
|:-------------------------------------:|:------------------------------------------:|
|   <kbd>🧹</kbd><br>Очистить корзину   |     <kbd>🔄</kbd><br>Обновить корзину      |


## today

| <kbd>➕</kbd>  | <kbd>🔼</kbd> |  <kbd>↕️</kbd>  | <kbd>Menu</kbd> |
|:-------------:|:-------------:|:---------------:|:---------------:|
| <kbd>🔙</kbd> | <kbd><</kbd>  | <kbd>&gt;</kbd> |  <kbd>🔄</kbd>  |

|      Знак       | Обозначение                           |
|:---------------:|---------------------------------------|
|  <kbd>➕</kbd>   | Добавить событие                      |
|  <kbd>🔼</kbd>  | Выбрать одно событие                  |
|  <kbd>↕️</kbd>  | Выбрать несколько событий             |
| <kbd>Menu</kbd> | Вернуться в меню                      |
|  <kbd>🔙</kbd>  | Вернуться в календарь                 |
|  <kbd><</kbd>   | Показать сообщение на вчерашний день  |
|  <kbd>></kbd>   | Показать сообщение на завтрашний день |
|  <kbd>🔄</kbd>  | Обновить сообщение                    |


## export

Экспорт событий в разных форматах файлов `csv`, `xml`, `json`, `jsonl`.


## Сообщение на один день

|     <kbd>📝</kbd><br>Отредактировать текст     | <kbd>🏷</kbd><br>Поставить статус на событие |    <kbd>🗑</kbd><br>Удалить событие    |
|:----------------------------------------------:|:--------------------------------------------:|:--------------------------------------:|
|          <kbd>📋</kbd><br>Отображение          |                                              | <kbd>📅</kbd><br>Изменить дату события |
|     <kbd>ℹ️</kbd><br>Информация о событии      |       <kbd>🗄</kbd><br>Удалить событие       |                                        |
| <kbd>🔙</kbd><br>Вернуться в сообщение на день |                                              |  <kbd>🔄</kbd><br>Обновить сообщение   |


## Cтатусы событий

Статус - это один или несколько эмодзи, используемых для обозначения заметки или добавления различных эффектов.

Заметка может иметь максимум 5 статусов.

> [!IMPORTANT]
> Существуют несовместимые статусы.
> 
> **Их нельзя размещать вместе в одной заметке.**
> 
> Если у вас есть одна заметка из пары, то вы не сможете разместить вторую.
> 
> | Несовместимые статусы                       | 
> |---------------------------------------------|
> | `🔗` (Ссылка) и `💻` (Код)                  |
> | `🪞` (Скрыто) и `💻` (Код)                  |
> | `🔗` (Ссылка) и `⛓` (Без сокращения ссылок) |
> | `🧮` (Нумерованный список) и `🗒` (Список)  |
> 
> Status effects are used only to visually display events.
> The event text itself remains unchanged.


## Лимиты

Существуют лимиты для разных групп пользователей.

### Максимальные возможные значения

| user_status | note<br>day | symbol<br>day | note<br>month | symbol<br>month | note<br>year | symbol<br>year | note<br>all | symbol<br>all |
|:------------|-------------|---------------|---------------|-----------------|--------------|----------------|-------------|---------------|
| default     | 20          | 4000          | 75            | 10000           | 500          | 80000          | 500         | 100000        |
| premium     | 40          | 8000          | 100           | 15000           | 750          | 100000         | 900         | 150000        |
| admin       | 60          | 20000         | 200           | 65000           | 1000         | 120000         | 2000        | 200000        |


## Поиск

В боте есть поиск по событиям.
Искать можно сообщением начинающимся с `#` например `#query` или командой `/search query`.
Такой поиск пытается найти все совпадения.
Запрос `#1 2` ищет все заметки, в которых есть цифры `1` **ИЛИ** `2` (`t1ext`, `tex2t`, `2te1xt`).


## open

```ebnf
Daily message
/open_today[_page_<page>]
/open_now[_page_<page>]

Monthly/Yearly calendar message
/open_calendar
/open_calendar_year

Open
/open[_<year>[_<month>[_<day>[_page_<page>]]]]
```
