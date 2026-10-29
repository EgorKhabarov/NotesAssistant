import os
from pathlib import Path

import git
import yaml

config_path = "config.yaml"

if not Path(config_path).exists():
    config_path = "config.example.yaml"

with open(config_path, "r", encoding="utf-8") as file:
    config: dict = yaml.safe_load(file.read()) or {}

try:
    repo = git.Repo()
    try:
        branch = repo.active_branch.name
    except TypeError:
        branch = repo.head.commit.hexsha[:8]
except git.exc.InvalidGitRepositoryError:
    branch = "master"

SQLALCHEMY_DATABASE_URI_temp: str | dict[str, str] = config.get(
    "SQLALCHEMY_DATABASE_URI",
    "sqlite:///data/database.sqlite3",
)
LOG_FILE_PATH: str = config.get("LOG_FILE_PATH", "logs/latest.log")

BOT_TOKEN: str = config.get("BOT_TOKEN", "")
WEATHER_API_KEY: str = config.get("WEATHER_API_KEY", "")

MIN_CALENDAR_YEAR: int = int(config.get("MIN_CALENDAR_YEAR", 1900))
MAX_CALENDAR_YEAR: int = int(config.get("MAX_CALENDAR_YEAR", 2300))

BOT_NOTIFICATIONS: bool = config.get("BOT_NOTIFICATIONS", True)
LIMIT_IMAGE_GENERATOR_URL: str = config.get("LIMIT_IMAGE_GENERATOR_URL", "")

TELEGRAM_WEBHOOK: bool = config.get("TELEGRAM_WEBHOOK", False)
TELEGRAM_WEBHOOK_URL: str = config.get("TELEGRAM_WEBHOOK_URL", "")
TELEGRAM_WEBHOOK_FLASK_PATH: str = config.get("TELEGRAM_WEBHOOK_FLASK_PATH", "")
TELEGRAM_WEBHOOK_SECRET_TOKEN: str = config.get("TELEGRAM_WEBHOOK_SECRET_TOKEN", "")

GITHUB_WEBHOOK: bool = config.get("GITHUB_WEBHOOK", False)
GITHUB_WEBHOOK_FLASK_PATH: str = config.get("GITHUB_WEBHOOK_FLASK_PATH", "")
GITHUB_WEBHOOK_SECRET: str = config.get("GITHUB_WEBHOOK_SECRET", "")

__wp = config.get("WSGI_PATH", "")

SQLALCHEMY_DATABASE_URI: str
if isinstance(SQLALCHEMY_DATABASE_URI_temp, dict):
    try:
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI_temp[branch]
    except KeyError:
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI_temp["master"]
else:
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI_temp

WSGI_PATH: Path | None = None
if __wp:
    WSGI_PATH = Path(__wp)
elif GITHUB_WEBHOOK and os.getenv("PYTHONANYWHERE_DOMAIN"):
    WSGI_PATH = Path(f"/var/www/{os.getenv('USERNAME')}_pythonanywhere_com_wsgi.py")

ADMIN_IDS = tuple(config.get("ADMIN_IDS", ()))
WHITE_LIST = tuple(
    int(x) for x in config.get("WHITE_LIST", []) or [] if x and x != "your_chat_id"
)
BLACK_LIST = tuple(
    int(x) for x in config.get("BLACK_LIST", []) or [] if x and x != "banned_chat_id"
)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42"
}
COMMANDS = (
    "start",
    "menu",
    "calendar",
    "today",
    "weather",
    "forecast",
    "week_event_list",
    "dice",
    "export",
    "help",
    "settings",
    "account",
    "groups",
    "commands",
    "search",
    "id",
    "clear_logs",
    "version",
    "v",
    "login",
    "signup",
    "logout",
    "open",
)

ts = "\u2800"
"""
Special transparent symbol for filling empty space in buttons
"⠀" or chr(10240) or "\\u2800"
"""

sql_order_dict = {
    "usual": """
ABS(DAYS_BEFORE_EVENT(date, statuses)) ASC, -- Близость к текущему дню
DAYS_BEFORE_EVENT(date, statuses) DESC,    -- Будущие события перед прошедшими
CASE
    WHEN statuses LIKE '%🟥%' THEN 1
    WHEN statuses LIKE '%📬%' THEN 2
    WHEN statuses LIKE '%🗞%' THEN 3
    WHEN statuses LIKE '%📅%' THEN 4
    WHEN statuses LIKE '%📆%' THEN 5
    WHEN statuses LIKE '%🎉%' THEN 6
    WHEN statuses LIKE '%🎊%' THEN 7
    ELSE 8
END ASC, -- Приоритет статусов
IFNULL(recent_changes_time, adding_time) DESC,
event_id DESC -- Если параметры совпадают, сортировать по большему event_id
""",
    "day": """
CASE
    WHEN statuses LIKE '%🟥%' THEN 1
    WHEN statuses LIKE '%📬%' THEN 2
    WHEN statuses LIKE '%🗞%' THEN 3
    WHEN statuses LIKE '%📅%' THEN 4
    WHEN statuses LIKE '%📆%' THEN 5
    WHEN statuses LIKE '%🎉%' THEN 6
    WHEN statuses LIKE '%🎊%' THEN 7
    ELSE 8
END ASC, -- Приоритет статусов
IFNULL(recent_changes_time, adding_time) DESC,
event_id DESC -- Если параметры совпадают, сортировать по большему event_id
""",
    "event_id": """
event_id ASC
""",
    "recent_changes_time": """
recent_changes_time ASC
""",
}

string_branch = "" if branch == "master" else f":{branch}"
__version__ = "2026.10.29.2"
__author__ = "EgorKhabarov"
__repository__ = "https://github.com/EgorKhabarov/NotesAssistant"
