import config


def end(num_diff: int):
    return "day" if num_diff == 1 else "days"


translation = {
    "func": {
        "deldate": lambda x: f"<b>{x} {end(x)} before delete</b>",
    },
    "arrays": {
        "relative_date_list": (
            "Today",
            "Tomorrow",
            "Day after tomorrow",
            "Yesterday",
            "Day before yesterday",
            "After",
            "ago",
            end,
        ),
        "account": (
            "Events per day",
            "Symbols per day",
            "Events per month",
            "Symbols per month",
            "Events per year",
            "Symbols per year",
            "Total events",
            "Total symbols",
        ),
        "months_list": (
            (("January", 1), ("February", 2), ("March", 3)),
            (("April", 4), ("May", 5), ("June", 6)),
            (("July", 7), ("August", 8), ("September", 9)),
            (("October", 10), ("November", 11), ("December", 12)),
        ),
        "week_days_list": ("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"),
        "week_days_list_full": (
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ),
        "months_name": (
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
        "months_name2": (
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
    "text": {
        "page": "Page",
        "add_bot_to_group": "Add bot to group",
        "restore_to_default": "Set default settings",
        "migrate": """
The group (<code>{from_chat_id}</code>) migrate into a supergroup (<code>{to_chat_id}</code>).
<b>Due to the nature of Telegram, all previous bot messages in this group are outdated and can no longer be used to interact with your account.
Call up new messages using bot commands.</b>
""",
        "account_has_been_deleted": "Your account has been deleted.",
        "recover": "Recover",
        "leap": "leap",
        "not_leap": "non-leap",
        "trash_bin": "To trash bin",
        "delete_permanently": "Delete permanently",
        "changes_saved": "Changes saved",
        "event_about_info": (
            "Information about event",
            "text length",
            "time added",
            "time of last changes",
        ),
        "clean_bin": "Clear basket",
        "bin_is_emptied": "Bin is emptied",
        "send_event_text": "Send the text of the event",
        "send_group_name": "Send the name of the group",
        "recurring_events": "Recurring events",
        "week_events": "Events in the next 7 days",
        "are_you_sure_edit": "Are you sure you want to change the event text to",
        "edit_username": "Change username",
        "edit_password": "Change password",
        "logout": "Logout",
        "leave_group": "Leave the group",
        "create_group": """
👥 Groups

Send group name
""",
        "change_group_name": "Change group name",
        "delete_group": "Delete group",
        "remove_bot_from_group": "Remove a bot from a group",
        "meters_per_second": "m/s",
        "get_premium": "Get Premium",
        "status": {
            "-1": "ban",
            "0": "normal",
            "1": "premium",
            "2": "admin",
        },
        "export_group": "Export group data",
        "event_history": (
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
        "search_placeholder": """
Reply to this message with a new search query.
`<code>.</code>` - search all
""",
        "search_filters": {
            "db": ("Before date", "<"),
            "dd": ("During date", "="),
            "da": ("After date", ">"),
            "tc": ("Status Match", "="),
            "ta": ("Approximate status match", "≈"),
            "tn": ("Not status match", "≠"),
        },
        "search_filters_clue": (
            "Click on {} to add a filter",
            "Click on the buttons below to remove the filter",
        ),
        "search_filter_clue": (
            "Select filter type",
            "Select date for filter",
            "Select status for filter",
        ),
        "bool": {
            "yes": "Yes",
            "no": "No",
        },
        "lang_flag": "",
        "saved": "Saved",
    },
    "messages": {
        "start": """
Greetings! I am your personal calendar assistant.
Here you can easily create events and notes that can be accessed from the calendar. Just use special emoji to add effects or make your search even more convenient!

📅 Calendar: Use a convenient calendar and easily move between days and months.

🔍 Search: Search for events by text and use convenient filters, so that not a single important event will escape your notice!

🔔 Notifications: Never miss important moments! Set notification for a specific time or turn them off at your convenience.

☁️ Weather: Want to know the weather forecast for your city? Just ask me and I will provide you with up-to-date data.

👑 Premium user benefits: Limits have been increased and a handy recycle bin is available for events that have been removed.

Use all the advantages of the bot to streamline your life and not miss a single important moment! If you have any questions, enter the /help command. Happy using! 🌟
""",
        "settings": """⚙️ Settings

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
        "group": """
👥 Group

id: `<code>{}</code>`
name: `<code>{}</code>`
""",
        "groups": (
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
        "account": """
👤 Account

<pre><code class='language-yaml'>id:       {}
chat_id:  {}
username: {}
reg_date: {}</code></pre>
""",
        "help": {
            "title": "📚 Help",
            "page main": [
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
            "page messages": [
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
            "page commands": [
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
            "page about": [
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
            "Events": """
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
            "Statuses": """
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
            "Limits": """
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
            "Calendar": """
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
            "1_day": """
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
            "7_days": """
<u>Types of messages > <b>7 days</b></u>

Displays events for the next 7 days.

Called by the command /week_event_list.
""",
            "Settings": """
<u>Types of messages > <b>Settings</b></u>

Called by the command /settings.
This message allows users to modify their settings.

To change the city, you need to reply to the bots message containing the city name settings.
The city is used for requesting the current weather (/weather) and weather forecast (/forecast).

The time zone is used to determine the user's local time.
""",
            "Basket": """
<u>Types of messages > <b>Basket</b></u>

Regular users can only delete their event permanently.
Premium users additionally have the option to move the event to the trash.
<b>Events in the trash are stored for no more than 30 days!</b>

In the trash basket, there is an option to restore the event to its original date.
""",
            "Search": """
<u>Types of messages > <b>Search</b></u>

You can search for events by sending a message to the bot using the following template:
#&lt;search query> or /search &lt;search query>

<b>Please note that the search query is case-sensitive!</b>

The bot looks for occurrences of the word in the text, date and status.
It returns all events that have matches.

For example, the request <code>#03.05. Music</code> will return all events that have the date 3rd May and contain the word "Music".

# TODO Expanding the capabilities of search queries is planned.
""",
            "Notifications": """
<u>Types of messages > <b>Notifications</b></u>

Notifications are disabled by default.
You can enable and customize the notification time in the settings (/settings).
The bot notifies about important "🟥" events, events with recurring status ("📬", "📅", "🗞", "📆"), and events with the status "🔔".
""",
            "BotNews": """
<u><b>Bot News</b></u>

▪️ .
""",
            "BotVersion": f"""
<b>Bot Version</b>

<pre><code class='language-version'>{config.__version__}{config.string_branch}</code></pre>
""",
            "CommandOpen": """
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
        "weather": """{} {} <u>{}</u>
Local time <b>{}</b>
Measurements from⠀<b>{}</b>
<b>{}°C</b>, feels like <b>{}°C</b>.
Wind 💨 <b>{} m/s</b>, direction {} (<b>{}°</b>)
Sunrise <b>{}</b>
Sunset⠀<b>{}</b>
Visibility <b>{}</b>m""",
        "search": "Search",
        "basket": "Basket",
        "reminder": "Notification",
        "menu": (
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
        "limit": "Limit for",
        "frequently_used_dates": "Press for pin",
    },
    "buttons": {
        "commands": {
            "not_login": {
                "user": (
                    ("start", "Start"),
                    ("login", "<username> <password>"),
                    ("signup", "<email> <username> <password>"),
                ),
                "member": (
                    ("start", "Start"),
                ),
            },
            "-1": {
                "user": (
                    ("_", "You are banned"),
                ),
                "member": (
                    ("_", "You are banned"),
                ),
            },
            "0": {
                "user": (
                    ("start", "Start"),
                    ("menu", "Menu"),
                    ("calendar", "Calendar"),
                    ("today", "Today's message"),
                    ("weather", "{city} Weather"),
                    ("forecast", "{city} Weather forecast for 5 days"),
                    ("week_event_list", "Weekly events"),
                    ("dice", "Roll the dice (randomizer)"),
                    ("export", "{format} Save my data in format. (csv, xml, json, jsonl)"),
                    ("help", "Help"),
                    ("settings", "Settings"),
                    ("account", "Account"),
                    ("groups", "Groups"),
                    ("logout", "Logout"),
                ),
                "member": (
                    ("start", "Start"),
                    ("menu", "Menu"),
                    ("calendar", "Calendar"),
                    ("today", "Today's message"),
                    ("weather", "{city} Weather"),
                    ("forecast", "{city} Weather forecast for 5 days"),
                    ("week_event_list", "Weekly events"),
                    ("dice", "Roll the dice (randomizer)"),
                    ("export", "{format} Save my data in format. (csv, xml, json, jsonl)"),
                    ("help", "Help"),
                    ("settings", "Settings"),
                ),
            },
            "1": {
                "user": (
                    ("start", "Start"),
                    ("menu", "Menu"),
                    ("calendar", "Calendar"),
                    ("today", "Today's message"),
                    ("weather", "{city} Weather"),
                    ("forecast", "{city} Weather forecast for 5 days"),
                    ("week_event_list", "Weekly events"),
                    ("dice", "Roll the dice (randomizer)"),
                    ("export", "{format} Save my data in format. (csv, xml, json, jsonl)"),
                    ("help", "Help"),
                    ("settings", "Settings"),
                    ("account", "Account"),
                    ("groups", "Groups"),
                    ("logout", "Logout"),
                ),
                "member": (
                    ("start", "Start"),
                    ("menu", "Menu"),
                    ("calendar", "Calendar"),
                    ("today", "Today's message"),
                    ("weather", "{city} Weather"),
                    ("forecast", "{city} Weather forecast for 5 days"),
                    ("week_event_list", "Weekly events"),
                    ("dice", "Roll the dice (randomizer)"),
                    ("export", "{format} Save my data in format. (csv, xml, json, jsonl)"),
                    ("help", "Help"),
                    ("settings", "Settings"),
                ),
            },
            "2": {
                "user": (
                    ("start", "Start"),
                    ("menu", "Menu"),
                    ("calendar", "Calendar"),
                    ("today", "Today's message"),
                    ("weather", "{city} Weather"),
                    ("forecast", "{city} Weather forecast for 5 days"),
                    ("week_event_list", "Weekly events"),
                    ("dice", "Roll the dice (randomizer)"),
                    ("export", "{format} Save my data in format. (csv, xml, json, jsonl)"),
                    ("help", "Help"),
                    ("settings", "Settings"),
                    ("account", "Account"),
                    ("groups", "Groups"),
                    ("commands", "Command list"),
                    ("logout", "Logout"),
                ),
                "member": (
                    ("start", "Start"),
                    ("menu", "Menu"),
                    ("calendar", "Calendar"),
                    ("today", "Today's message"),
                    ("weather", "{city} Weather"),
                    ("forecast", "{city} Weather forecast for 5 days"),
                    ("week_event_list", "Weekly events"),
                    ("dice", "Roll the dice (randomizer)"),
                    ("export", "{format} Save my data in format. (csv, xml, json, jsonl)"),
                    ("help", "Help"),
                    ("settings", "Settings"),
                    ("commands", "Command list"),
                ),
            },
        },
        "select_status": {
            "folders": (
                (("🗂 Importance", "1"),),
                (("🗂 Miscellaneous", "2"),),
                (
                    ("🗂 Effects", "3"),
                    ("🗂 Custom", "4"),
                ),
            ),
            "1": (
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
            "2": (
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
            "3": (
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
            "4": (
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
    "errors": {
        "success": "Success",
        "failure": "Failure",
        "email_is_taken": "This email is already taken",
        "wrong_username": """
Wrong username
Length from 4 to 31 characters.
Use only Latin letters, numbers, and underscores.
Cannot start with a number.
Cannot have two underscores in a row.
""",
        "wrong_email": "Wrong email",
        "incorrect_password": "Incorrect password",
        "password_too_easy": "The password is too easy",
        "username_is_taken": "This username is taken",
        "account_not_found": "Account not found",
        "not_enough_permissions": "Not enough permissions",
        "forbidden_to_log_account_in_group": "You can't log into your account in a group",
        "forbidden_to_log_group": "This telegram group is not connected to the user's group",
        "already_connected_group": "This telegram group is already connected to the user's group",
        "no_account": """
You are not logged in to your account. Login
<code>/login </code>&lt;username&gt; &lt;password&gt;
or create an account
<code>/signup </code>&lt;email&gt; &lt;username&gt; &lt;password&gt;
""",
        "many_attempts": "Sorry, too many requests. Please try again in {} seconds.",
        "many_attempts_weather": "The weather was requested too often. Retry in {} seconds.",
        "error": "An error has occurred",
        "file_is_too_big": "An error has occurred. Maybe the file is too big 🫤",
        "export": "You can't export data so often\nPlease wait <b>{t} minutes</b>",
        "export_format": "Wrong format. Choose from (csv, xml, json, jsonl)",
        "export_empty": "There were no events in this group.",
        "deleted": "Sorry, this command is not available for you",
        "no_events_to_interact": "No events to interact",
        "already_on_this_page": "You are already on this page",
        "status_already_posted": "Status is already posted on event",
        "more_5_statuses": "You can not put more than 5 statuses",
        "message_is_too_long": "Message is too long",
        "change_information_is_too_long": "The change information is too long",
        "exceeded_limit": "You have exceeded the daily limit.\nReduce the number of characters or remove unnecessary events.",
        "limit_exceeded": "Limit exceeded",
        "message_empty": "🕸  It's empty here🕷  🕸",
        "request_empty": "Request is empty :/",
        "invalid_request": "Error in request",
        "nothing_found": "🕸  Nothing has found🕷  🕸",
        "get_permission": "Please give the bot <b>permission to delete messages</b> to keep the chat clean",
        "delete_messages_older_48_h": "Due to Telegram restrictions, the bot cannot delete messages <b>older than 48 hours</b>.",
        "weather_invalid_city_name": "Error. Invalid city name.\nTry again /weather {city}",
        "forecast_invalid_city_name": "Error. Invalid city name.\nTry again /forecast {city}",
        "nodata": "👀 You have no events for this date",
        "invalid_date": "Invalid date!",
        "settings": {
            "commit_changes": "You have not saved your settings! Click 💾 to save",
        },
        "bin": {
            "confirmation_of_purification": "Are you sure you want to permanently delete the events in your trash? Click again to delete the events in your trash",
        },
        "event": {
            "commit_clear_history": "Are you sure you want to clear the event's change history? Click again to clear change history",
        },
        "confirmation_of_deletion": {
            "event": "Are you sure you want to permanently delete the event? Click again to permanently delete the event",
            "events": "Are you sure you want to permanently delete events? Click again to permanently delete events",
        },
    },
    "select": {
        "status_to_event": "Select a status for the event:",
        "notification_date": "Select notification date",
        "event_to_open": "Select an event to open",
        "event": "Choose an event",
        "events": "Choose an events",
        "date": "Select a date",
        "new_date": "Select a new date for the event",
        "what_do_with_event": "Choose what to do with the event",
        "what_do_with_events": "Choose what to do with the events",
        "events_new_date": "Please select a new date for these events",
    },
}
