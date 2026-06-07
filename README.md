<table>
    <td><a href="/README.md">EN</a></td>
    <td><a href="/docs/README_ru.md">RU</a></td>
</table>

[![GitHub Actions Workflow Status](https://github.com/EgorKhabarov/TODO-bot/actions/workflows/tests.yml/badge.svg)](https://github.com/EgorKhabarov/TODO-bot/actions/workflows/tests.yml)

[![Telegram](https://egorkhabarov.github.io/resources/badges/Telegram.svg)](https://t.me/NotesAssistantBot)
[![UptimeRobot Status](https://img.shields.io/uptimerobot/status/m796658291-a3b1e18d0d9b2662434240e6)](https://uptimerobot.com/)

# NotesAssistant
### Bot for organizing notes in Telegram
Storing, adding, editing and deleting notes by date.
You can tag a note with an emoji.
Convenient search by emoji statuses and dates.
Birthdays and holidays are marked on the calendar (you need to set an emoji status).

# Installation instructions

### Download

```shell
git clone https://github.com/EgorKhabarov/NotesAssistant
cd NotesAssistant
cp config.example.yaml config.yaml
pip install -r requirements.txt
```

### Settings

Edit `config.yaml` in the bot directory

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

### Launch
Only bot
```shell
python start_bot.py
```
Server
```shell
python -c "from server import app;app.run('0.0.0.0')"
```

### Getting administrator rights

#### Get your telegram **chat_id**

Launch the bot and send the command `/id`.
Add the resulting `chat_id` to `ADMIN_IDS` in `config.yaml` and restart the bot.

> [!IMPORTANT]
> Add only chat_id of personal accounts (private chats)!
> Any interaction of any person in a telegram group with a bot is perceived as on behalf of the group.

### Setting up PythonAnywhere

- Create a web server using the latest available version of Python
- In the `Code` category change `Working directory` to the path to the folder with `server.py`
- In the `Security` category change `Force HTTPS` to `Enabled`

### Docker

```shell
docker build -t NotesAssistant .
docker volume create NotesAssistantData
docker volume create NotesAssistantLogs
docker run -p 5000:5000 -v NotesAssistantData:/app/data -v NotesAssistantLogs:/app/logs --name NotesAssistantContainer NotesAssistant -d NotesAssistant
```
```shell
docker compose up -d --build
```

---

# Commands

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

Greets the user.

| Buttons              | Actions                     |
|:---------------------|-----------------------------|
| <kbd>/menu</kbd>     | Same as `/menu` command     |
| <kbd>/calendar</kbd> | Same as `/calendar` command |


## menu

Navigation through bot functions.

| Buttons                     | Actions                                              |
|:----------------------------|------------------------------------------------------|
| <kbd>📚 Help</kbd>          | Same as `/help`                                      |
| <kbd>📆 Calendar</kbd>      | Same as `/calendar`                                  |
| <kbd>👤 Account</kbd>       | Personal account and data export                     |
| <kbd>👥 Groups</kbd>        | Group settings                                       |
| <kbd>📆 7 days</kbd>        | Notes in the next 7 days                             |
| <kbd>🔔 Notifications</kbd> | View notes that will be included in the notification |
| <kbd>⚙ Settings</kbd>       | Same as `/settings`                                  |
| <kbd>🗑 Bin</kbd>           | Recycle bin with deleted notes (premium)             |


## help

Gives access to information about the bot's capabilities.


## calendar

Calendar.

<table>
    <tr><th colspan="7">January (1.2000) (Leap 🐲) (52-5)</th></tr>
    <tr><th>  Mo </th><th> Tu! </th><th> We </th><th> Th </th><th> Fr </th><th> Sa </th><th> Su </th></tr>
    <tr><th>     </th><th>     </th><th>    </th><th>    </th><th>    </th><th><img alt="#1" src="https://img.shields.io/badge/%231-blue"></th><th>  2 </th></tr>
    <tr><th>   3 </th><th><img alt="4!*" src="https://img.shields.io/badge/4!*-green"></th><th>  5 </th><th><img alt="6³" src="https://img.shields.io/badge/6³-green"></th><th>  7 </th><th>  8 </th><th>  9 </th></tr>
    <tr><th> 10! </th><th>  11 </th><th> 12 </th><th> 13 </th><th> 14 </th><th> 15 </th><th> 16 </th></tr>
    <tr><th>  17 </th><th>  18 </th><th> 19 </th><th> 20 </th><th> 21 </th><th> 22 </th><th> 23 </th></tr>
    <tr><th>  24 </th><th>  25 </th><th> 26 </th><th> 27 </th><th> 28 </th><th> 29 </th><th> 30 </th></tr>
    <tr><th>  31 </th><th>     </th><th>    </th><th>    </th><th>    </th><th>    </th><th>    </th></tr>
    <tr><th colspan="2"><<</th><th><</th><th>⟳</th><th>></th><th colspan="2">>></th></tr>
    <tr><th colspan="4">🔙</th><th colspan="3">🗂</th></tr>
</table>


### Designations

#### First button

When pressed, a yearly calendar appears.

| Designation | Meaning                                       |
|:------------|-----------------------------------------------|
| January     | Names of the month                            |
| (1.2000)    | Month and year numbers                        |
| (Leap 🐲)   | Is it a leap year and the animal of this year |
| (52-5)      | Numbers of the first and last week            |


#### Days of the week

When pressed, they do nothing.
The text on the button may end with the `!` character.
This means that on this day of the week there are repeating notes with an interval of a week ([more about statuses](#note-statuses)).


#### Button for the day

When pressed, it calls up [message for one day](#message-for-one-day)

| Sign | Designation                                                                                                                           |
|:----:|---------------------------------------------------------------------------------------------------------------------------------------|
| `#`  | Today                                                                                                                                 |
| `*`  | There are notes on this day<br>If there are less than 10 notes then it will consist of degree icons<br>indicating the number of notes |
| `!`  | There is an important note on this day<br>For example, with the status birthday `🎉` or holiday `🎊`                                  |


#### Navigation buttons

|    Buttons    | Actions                              |
|:-------------:|--------------------------------------|
| <kbd><<</kbd> | Show calendar for **one year ago**   |
| <kbd><</kbd>  | Show calendar for **one month ago**  |
| <kbd>⟳</kbd>  | Show calendar for **current date**   |
| <kbd>></kbd>  | Show calendar **one month ahead**    |
| <kbd>>></kbd> | Show calendar for **one year ahead** |

> [!TIP]
> When you click on a <kbd>⟳</kbd> in the calendar, today's date opens.


#### Colors

| Color                                                          | Designation                 |
|----------------------------------------------------------------|-----------------------------|
| <img alt="4!*" src="https://img.shields.io/badge/blue-blue">   | Today                       |
| <img alt="4!*" src="https://img.shields.io/badge/green-green"> | There are notes on this day |


## account

Here you can change your username and password or log out of your account.
You can also view your limits <kbd>📊</kbd>.


## groups

You can connect a group to your account in the bot.

<table>
    <tr><th><kbd>🔸All</kbd></th><th><kbd>Member</kbd></th><th><kbd>Moderator</kbd></th><th><kbd>Admin</kbd></th></tr>
    <tr><th colspan="4"><kbd>&lt;Your first group name&gt;</kbd></th></tr>
    <tr><th colspan="2"><kbd>🔙</kbd></th><th colspan="2"><kbd>👥 Create group</kbd></th></tr>
</table>


## week_event_list

Message with notes in the next 7 days.


## notifications

Message with notes for today, tomorrow, after tomorrow, after after tomorrow and in a week.


## settings

Message with settings.

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
    <tr><th colspan="5"><kbd>Default settings</kbd></th></tr>
</table>

|             Sign              | Designation                                                                                                                    |
|:-----------------------------:|--------------------------------------------------------------------------------------------------------------------------------|
|         <kbd>🗣</kbd>         | Language (default `ru`)                                                                                                        |
|         <kbd>🔗</kbd>         | Should I shorten links (https://en.wikipedia.org/wiki/Hyperlink → [en.wikipedia.org](https://en.wikipedia.org/wiki/Hyperlink)) |
| <kbd>⬇️</kbd> / <kbd>⬆️</kbd> | Note sort order                                                                                                                |
|         <kbd>🔕</kbd>         | Whether to enable notifications (disabled by default)                                                                          |
| <kbd>⬜️</kbd> / <kbd>⬛️</kbd> | Bot theme (replaces dark emoticons with light ones)                                                                            |
|         <kbd>🌍</kbd>         | Your time zone                                                                                                                 |
|         <kbd>⏰</kbd>          | Notification Time                                                                                                              |


## trash

List of deleted notes.

| <kbd>🔼</kbd><br>Select one note | <kbd>↕️</kbd><br>Select multiple notes |
|:--------------------------------:|:--------------------------------------:|
|   <kbd>🧹</kbd><br>Empty Trash   |      <kbd>🔄</kbd><br>Update cart      |


## today

| <kbd>➕</kbd>  | <kbd>🔼</kbd> |  <kbd>↕️</kbd>  | <kbd>Menu</kbd> |
|:-------------:|:-------------:|:---------------:|:---------------:|
| <kbd>🔙</kbd> | <kbd><</kbd>  | <kbd>&gt;</kbd> |  <kbd>🔄</kbd>  |

|      Sign       | Designation                 |
|:---------------:|-----------------------------|
|  <kbd>➕</kbd>   | Add note                    |
|  <kbd>🔼</kbd>  | Select one note             |
|  <kbd>↕️</kbd>  | Select multiple notes       |
| <kbd>Menu</kbd> | Return to menu              |
|  <kbd>🔙</kbd>  | Return to calendar          |
|  <kbd><</kbd>   | Show message for yesterday  |
|  <kbd>></kbd>   | Show message for tomorrow   |
|  <kbd>🔄</kbd>  | Update message              |


## export

Export notes in different file formats `csv`, `xml`, `json`, `jsonl`.


## Message for one note

| <kbd>📝</kbd>Edit text    | <kbd>🏷</kbd>Statuses        | <kbd>🗑</kbd>Delete note     |
|:--------------------------|:-----------------------------|:-----------------------------|
| <kbd>📋</kbd>Display      |                              | <kbd>📅</kbd>Change date     |
| <kbd>ℹ️</kbd>Information  | <kbd>🗄</kbd>Сhange history  |                              |
| <kbd>🔙</kbd>Back         |                              | <kbd>🔄</kbd>Update message  |


## Note statuses

A status is one or more emoji to mark an note or add different effects.

Note can have a maximum of 5 statuses.

> [!IMPORTANT]
> There are incompatible statuses.
> 
> **They cannot be placed together in the same note.**
> 
> If you have one note from a pair, then you will not be able to place the second one.
> 
> | Incompatible statuses                    | 
> |------------------------------------------|
> | `🔗` (Link) and `💻` (Code)              |
> | `🪞` (Hidden) and `💻` (Code)            |
> | `🔗` (Link) and `⛓` (No link shortening) |
> | `🧮` (Numbered List) and `🗒` (List)     |
> 
> Status effects are used only to visually display events.
> The event text itself remains unchanged.


## Limits

There are limits for different user groups.

### Maximum possible values

| user_status | note<br>day | symbol<br>day | note<br>month | symbol<br>month | note<br>year | symbol<br>year | note<br>all | symbol<br>all |
|:------------|-------------|---------------|---------------|-----------------|--------------|----------------|-------------|---------------|
| default     | 20          | 4000          | 75            | 10000           | 500          | 80000          | 500         | 100000        |
| premium     | 40          | 8000          | 100           | 15000           | 750          | 100000         | 900         | 150000        |
| admin       | 60          | 20000         | 200           | 65000           | 1000         | 120000         | 2000        | 200000        |


## Search

The bot features a convenient search feature for notes.
You can search using a message beginning with `#` (e.g., `#query`) or the command `/search query`.
This search attempts to find all matches.
The query `#1 2` finds all notes containing the numbers `1` **OR** `2` (`t1ext`, `tex2t`, `2te1xt`).


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
