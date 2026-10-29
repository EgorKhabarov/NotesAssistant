from typing import Any, Literal, TypeAlias

from telebot.types import (
    CopyTextButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    SwitchInlineQueryChosenChat,
)

# str | dict | CopyTextButton | SwitchInlineQueryChosenChat
_InlineRowItem: TypeAlias = dict[str, Any]
_ButtonsDataTypes: TypeAlias = (
    list[list[_InlineRowItem]] | list[list[str]] | dict[str, Any] | None
)
keyboard_types = Literal["inline", "reply", "force_reply", "reply_remove"] | str


def generate_inline_buttons(
    buttons_data: _ButtonsDataTypes,
) -> InlineKeyboardMarkup | None:
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

    if not isinstance(buttons_data, list):
        return None

    keyboard: list[list[InlineKeyboardButton]] = []
    for row in buttons_data:
        keyboard.append([])
        for button in row:
            if not isinstance(button, dict) or button == {}:
                continue
            if len(button.keys()) == 1:
                text, data = next(iter(button.items()))
                if isinstance(data, str):
                    keyboard[-1].append(InlineKeyboardButton(text, callback_data=data))
                elif isinstance(data, dict):
                    btn_params = dict(data)
                    if btn_params.get("switch_inline_query_chosen_chat"):
                        chat_param = btn_params["switch_inline_query_chosen_chat"]
                        if isinstance(chat_param, str):
                            btn_params["switch_inline_query_chosen_chat"] = (
                                SwitchInlineQueryChosenChat(chat_param)
                            )
                        elif isinstance(chat_param, dict):
                            btn_params["switch_inline_query_chosen_chat"] = (
                                SwitchInlineQueryChosenChat(**chat_param)
                            )
                        else:
                            return None
                    if btn_params.get("copy_text"):
                        copy_param = btn_params["copy_text"]
                        if isinstance(copy_param, str):
                            btn_params["copy_text"] = CopyTextButton(copy_param)
                        elif isinstance(copy_param, dict):
                            btn_params["copy_text"] = CopyTextButton(**copy_param)
                        else:
                            return None
                    keyboard[-1].append(InlineKeyboardButton(text=text, **btn_params))
                else:
                    return None
            else:
                keyboard[-1].append(InlineKeyboardButton(**button))
    return InlineKeyboardMarkup(keyboard=keyboard)


def generate_reply_buttons(
    buttons_data: _ButtonsDataTypes,
) -> ReplyKeyboardMarkup | None:
    """
    >>> from pprint import pprint
    >>> markup = [["1", "2", "3"]]
    >>> pprint(generate_reply_buttons(markup).keyboard)
    [[{'text': '1'}, {'text': '2'}, {'text': '3'}]]
    """
    if isinstance(buttons_data, InlineKeyboardMarkup):
        return buttons_data
    if not isinstance(buttons_data, list):
        return None
    markup = ReplyKeyboardMarkup()
    for row in buttons_data:
        markup.add(*row)
    return markup


# def generate_force_reply_buttons(buttons_data: _ButtonsDataTypes) -> ForceReply:
#     if isinstance(buttons_data, InlineKeyboardMarkup):
#         return buttons_data
#     return ForceReply(**{} if buttons_data is None else buttons_data)


# def generate_reply_remove_buttons(
#     buttons_data: _ButtonsDataTypes,
# ) -> ReplyKeyboardRemove:
#     if isinstance(buttons_data, InlineKeyboardMarkup):
#         return buttons_data
#     return ReplyKeyboardRemove(**{} if buttons_data is None else buttons_data)


def edit_button_data(
    markup: InlineKeyboardMarkup,
    row: int,
    column: int,
    callback_data: str | None = None,
    text: str | None = None,
) -> None:
    if callback_data is not None:
        markup.keyboard[row][column].callback_data = callback_data
    if text is not None:
        markup.keyboard[row][column].text = text
