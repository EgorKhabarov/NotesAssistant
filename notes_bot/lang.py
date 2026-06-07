import importlib
from typing import Any, Literal

from notes_bot.request import request


class LazyTranslation(dict):
    def __missing__(self, lang_iso: str):
        try:
            module = importlib.import_module(f"notes_bot.locales.{lang_iso}")
            data = getattr(module, "translation")
        except ModuleNotFoundError:
            if lang_iso != "en":
                return self["en"]
            raise KeyError(f'No translation for language "{lang_iso}" and fallback "en" missing')
        except AttributeError:
            raise KeyError(f'Module "locales.{lang_iso}" has no "translation" dict')
        self[lang_iso] = data
        return data


translation = LazyTranslation()


def get_translate(target: str, lang_iso: str | None = None) -> str | Any:
    _lang_iso: str = lang_iso or (
        request.entity.settings.lang if request.entity else "en"
    )
    result: dict = translation[_lang_iso]
    for key in target.split("."):
        result = result[key]
    return result


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
