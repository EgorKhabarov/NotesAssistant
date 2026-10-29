import re
import sys
from typing import Any

from telegram_utils.argument_parser import (
    _DataTypes,
    _ReturnTypes,
    get_arguments,
    validate_arguments,
)


class __CommandRegex:
    # re.Pattern is marked as @final and should not be subclassed
    def __init__(self) -> None:
        self.username: str = "[a-zA-Z0-9_]{5,32}"
        self.__regex: re.Pattern[str] = re.compile(
            r"(?s)\A/(?P<command>[a-zA-Z0-9_]+)"
            rf"(?P<username>@{self.username}\b)?"
            r"(?:\s|$)(?P<arguments>.+)?\Z"
        )
        self.set_username()

    def set_username(self, raw_bot_username: str | None = None) -> None:
        self.username = (
            re.escape(raw_bot_username) if raw_bot_username else "[a-zA-Z0-9_]{5,32}"
        )
        self.__regex = re.compile(
            r"(?s)\A/(?P<command>[a-zA-Z0-9_]+)"
            rf"(?P<username>@{self.username}\b)?"
            r"(?:\s|$)(?P<arguments>.+)?\Z"
        )

    def match(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
    ) -> re.Match[str] | None:
        return self.__regex.match(string, pos, endpos)


command_regex = __CommandRegex()


def get_command_arguments(
    message: str,
    arguments: dict[str, _DataTypes | tuple[_DataTypes, Any]],
) -> dict[str, _ReturnTypes]:
    """
    >>> try: get_command_arguments("", {"arg1": "long str", "arg2": "str"})
    ... except SyntaxError as e: str(e)
    'parameter after or before "long str"'
    >>> try: get_command_arguments("", {"arg1": "long str", "arg2": "long str"})
    ... except SyntaxError as e: str(e)
    'multiple starred expressions in assignment'
    >>> get_command_arguments("", {})
    {}
    >>> arguments_1 = {"arg1": "str", "arg2": ("str", 1)}
    >>> get_command_arguments("", arguments_1)
    {'arg1': None, 'arg2': None}
    >>> get_command_arguments("/c", arguments_1)
    {'arg1': None, 'arg2': 1}
    >>> get_command_arguments("/c@namebot", arguments_1)
    {'arg1': None, 'arg2': 1}
    >>> get_command_arguments("/c@namebot arg1", arguments_1)
    {'arg1': 'arg1', 'arg2': 1}
    >>> get_command_arguments("/c@namebot arg1 arg2", arguments_1)
    {'arg1': 'arg1', 'arg2': 'arg2'}
    >>> get_command_arguments("/c@namebot arg1 arg2 arg3", arguments_1)
    {'arg1': 'arg1', 'arg2': 'arg2'}
    >>> get_command_arguments("/c@namebot arg1 arg2", {"text": "long str"})
    {'text': 'arg1 arg2'}
    >>> get_command_arguments("abrakadabra", {})
    {}
    >>> get_command_arguments("abrakadabra", {"text": "long str"})
    {'text': None}
    """
    validate_arguments(arguments)
    match = command_regex.match(message)

    if match is None:
        return {k: None for k in arguments}

    command_arguments = match.groupdict()["arguments"] if match else ""
    if not command_arguments:
        return {
            k: (v[1] if isinstance(v, tuple) else None) for k, v in arguments.items()
        }
    return get_arguments(command_arguments, arguments)


def parse_command(
    message: str,
    arguments: dict[str, _DataTypes | tuple[_DataTypes, Any]],
) -> dict[str, Any]:
    """
    >>> try: parse_command("", {"arg1": "long str", "arg2": "str"})
    ... except SyntaxError as e: str(e)
    'parameter after or before "long str"'
    >>> try: parse_command("", {"arg1": "long str", "arg2": "long str"})
    ... except SyntaxError as e: str(e)
    'multiple starred expressions in assignment'
    >>> parse_command("", {})
    {'command': None, 'username': None, 'arguments': {}}
    >>> parse_command("/c@namebot", {})
    {'command': 'c', 'username': '@namebot', 'arguments': {}}
    >>> parse_command("/c@namebot arg1", {})
    {'command': 'c', 'username': '@namebot', 'arguments': {}}
    >>> parse_command("/c@namebot arg1 arg2", {})
    {'command': 'c', 'username': '@namebot', 'arguments': {}}

    >>> arguments_1 = {"arg1": "str", "arg2": ("str", 1)}
    >>> parse_command("", arguments_1)
    {'command': None, 'username': None, 'arguments': {'arg1': None, 'arg2': None}}
    >>> parse_command("/c@namebot", arguments_1)
    {'command': 'c', 'username': '@namebot', 'arguments': {'arg1': None, 'arg2': 1}}
    >>> parse_command("/c@namebot arg1", arguments_1)
    {'command': 'c', 'username': '@namebot', 'arguments': {'arg1': 'arg1', 'arg2': 1}}
    >>> parse_command("/c@namebot arg1 arg2", arguments_1)
    {'command': 'c', 'username': '@namebot', 'arguments': {'arg1': 'arg1', 'arg2': 'arg2'}}
    """
    res_arguments = get_command_arguments(message, arguments)
    match = command_regex.match(message)

    if match:
        groups = match.groupdict()
        return {
            "command": groups["command"],
            "username": groups["username"],
            "arguments": res_arguments,
        }
    else:
        return {
            "command": None,
            "username": None,
            "arguments": {k: None for k in arguments},
        }
