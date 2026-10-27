from typing import Any, Literal

from telebot.types import (
    CopyTextButton,
    ForceReply,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    SwitchInlineQueryChosenChat,
)

buttons_data_types = (
    list[list[dict[str, str | dict | CopyTextButton | SwitchInlineQueryChosenChat]]]
    | list[list[str]]
    | dict[str, Any]
    | None
)
keyboard_types = Literal["inline", "reply", "force_reply", "reply_remove"] | str


def generate_inline_buttons(buttons_data: buttons_data_types) -> InlineKeyboardMarkup:
    """
    >>> from pprint import pprint
    >>> markup = [
    ...     [
    ...         {"button text": "call data"},  # simple button
    ...     ],
    ...     [
    ...         {
    ...             "button text": {
    ...                 "url": None,
    ...                 "callback_data": "call data",
    ...                 "web_app": None,
    ...                 "switch_inline_query": None,
    ...                 "switch_inline_query_current_chat": None,
    ...                 "switch_inline_query_chosen_chat": None,
    ...                 "callback_game": None,
    ...                 "pay": None,
    ...                 "copy_text": None,
    ...                 "login_url": None,
    ...                 "**kwargs": {},
    ...             }
    ...         },
    ...         {
    ...             "text": "button text",
    ...             "url": None,
    ...             "callback_data": "call data",
    ...             "web_app": None,
    ...             "switch_inline_query": None,
    ...             "switch_inline_query_current_chat": None,
    ...             "switch_inline_query_chosen_chat": None,
    ...             "callback_game": None,
    ...             "pay": None,
    ...             "copy_text": None,
    ...             "login_url": None,
    ...             "**kwargs": {},
    ...         },
    ...     ],
    ... ]
    ...
    >>> buttons = generate_inline_buttons(markup)
    >>> result = [isinstance(buttons, InlineKeyboardMarkup)]
    >>> for r in buttons.keyboard:
    ...     result.append([])
    ...     for b in r:
    ...         result[-1].append(b.to_dict())
    ...
    >>> pprint(result)
    [True,
     [{'callback_data': 'call data', 'text': 'button text'}],
     [{'callback_data': 'call data', 'text': 'button text'},
      {'callback_data': 'call data', 'text': 'button text'}]]
    """
    if isinstance(buttons_data, InlineKeyboardMarkup):
        return buttons_data

    keyboard: list[list[InlineKeyboardButton]] = []
    for row in buttons_data:
        keyboard.append([])
        for button in row:
            if button == {}:
                continue
            if len(button.keys()) == 1:
                [(text, data)] = button.items()
                if isinstance(data, str):
                    keyboard[-1].append(InlineKeyboardButton(text, callback_data=data))
                elif isinstance(data, dict):
                    [(text, data)] = button.items()
                    if data.get("switch_inline_query_chosen_chat"):
                        if isinstance(
                            data["switch_inline_query_chosen_chat"],
                            str,
                        ):
                            new_data = SwitchInlineQueryChosenChat(
                                data["switch_inline_query_chosen_chat"]
                            )
                            data["switch_inline_query_chosen_chat"] = new_data
                        elif isinstance(
                            data["switch_inline_query_chosen_chat"],
                            dict,
                        ):
                            new_data = SwitchInlineQueryChosenChat(
                                **data["switch_inline_query_chosen_chat"]
                            )
                            data["switch_inline_query_chosen_chat"] = new_data
                        else:
                            return None
                    if data.get("copy_text"):
                        if isinstance(data["copy_text"], str):
                            data["copy_text"] = CopyTextButton(data["copy_text"])
                        elif isinstance(data["copy_text"], dict):
                            data["copy_text"] = CopyTextButton(**data["copy_text"])
                        else:
                            return None
                    keyboard[-1].append(InlineKeyboardButton(text=text, **data))
                else:
                    return None
            else:
                keyboard[-1].append(InlineKeyboardButton(**button))
    return InlineKeyboardMarkup(keyboard=keyboard)


def generate_reply_buttons(buttons_data: buttons_data_types) -> ReplyKeyboardMarkup:
    """
    >>> from pprint import pprint
    >>> markup = [["1", "2", "3"]]
    >>> pprint(generate_reply_buttons(markup).keyboard)
    [[{'text': '1'}, {'text': '2'}, {'text': '3'}]]
    """
    if isinstance(buttons_data, InlineKeyboardMarkup):
        return buttons_data
    markup = ReplyKeyboardMarkup()
    for row in buttons_data:
        markup.add(*row)
    return markup


def generate_force_reply_buttons(buttons_data: buttons_data_types) -> ForceReply:
    if isinstance(buttons_data, InlineKeyboardMarkup):
        return buttons_data
    return ForceReply(**{} if buttons_data is None else buttons_data)


def generate_reply_remove_buttons(
    buttons_data: buttons_data_types,
) -> ReplyKeyboardRemove:
    if isinstance(buttons_data, InlineKeyboardMarkup):
        return buttons_data
    return ReplyKeyboardRemove(**{} if buttons_data is None else buttons_data)


def edit_button_data(
    markup: InlineKeyboardMarkup,
    row: int,
    column: int,
    callback_data: str = ...,
    text: str = ...,
) -> None:
    if callback_data is not ...:
        markup.keyboard[row][column].callback_data = callback_data
    if text is not ...:
        markup.keyboard[row][column].text = text
