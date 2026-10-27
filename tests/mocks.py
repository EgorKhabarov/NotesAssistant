# noinspection PyPackageRequirements
from telebot.types import CallbackQuery, Chat, Message, User


def message_mock(message_id: int, text: str, html_text=None) -> Message:
    if html_text is None:
        html_text = text

    return Message(
        message_id=message_id,
        from_user=User(
            id=1,
            is_bot=False,
            first_name="first_name",
            username="username",
            last_name="last_name",
            full_name="first_name last_name",
        ),
        date=100,
        chat=Chat(
            id=1,
            type="private",
            title=None,
            username="username",
            first_name="first_name",
            last_name="last_name",
        ),
        content_type="text",
        options={"text": text},
        json_string="",
    )


def callback_mock(data: str, message: Message | None = None) -> CallbackQuery:
    if message is None:
        message = message_mock(1, "message text")
    return CallbackQuery(
        id=100,  # TODO int -> str
        from_user=User(
            id=1,
            is_bot=False,
            first_name="first_name",
            username="username",
            last_name="last_name",
            full_name="first_name last_name",
        ),
        data=data,
        chat_instance="",
        json_string="",
        message=message,
        inline_message_id=100,  # TODO int -> str
    )
