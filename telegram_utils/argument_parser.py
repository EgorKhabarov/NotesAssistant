from collections.abc import Callable
from datetime import datetime
from typing import Any, Literal, TypeAlias

_DataTypes: TypeAlias = (
    str
    | Literal[
        "str",
        "int",
        "float",
        "date",
        "long str",
    ]
)
_ReturnTypes: TypeAlias = str | int | float | datetime | list[int] | None


def get_arguments(
    text: str,
    arguments: dict[str, _DataTypes | tuple[_DataTypes, Any]],
) -> dict[str, _ReturnTypes]:
    """
    >>> try: get_arguments("", {"arg1": "long str", "arg2": "str"})
    ... except SyntaxError as e: str(e)
    'parameter after or before "long str"'
    >>> try: get_arguments("", {"arg1": "long str", "arg2": "long str"})
    ... except SyntaxError as e: str(e)
    'multiple starred expressions in assignment'

    >>> get_arguments("", {})
    {}
    >>> get_arguments("abrakadabra", {})
    {}

    >>> arguments_1 = {"text": "long str"}
    >>> get_arguments("arg1 arg2", arguments_1)
    {'text': 'arg1 arg2'}
    >>> get_arguments("abrakadabra", arguments_1)
    {'text': 'abrakadabra'}

    >>> arguments_2 = {"arg1": "str", "arg2": ("str", "default")}
    >>> get_arguments("", arguments_2)
    {'arg1': None, 'arg2': 'default'}
    >>> get_arguments("arg1", arguments_2)
    {'arg1': 'arg1', 'arg2': 'default'}
    >>> get_arguments("arg1 arg2", arguments_2)
    {'arg1': 'arg1', 'arg2': 'arg2'}
    >>> get_arguments("arg1 arg2 arg3", arguments_2)
    {'arg1': 'arg1', 'arg2': 'arg2'}

    >>> arguments_3 = {"arg1": "str", "arg2": ("int", 1)}
    >>> get_arguments("", arguments_3)
    {'arg1': None, 'arg2': 1}
    >>> get_arguments("123 123", arguments_3)
    {'arg1': '123', 'arg2': 123}
    >>> get_arguments("arg1 123", arguments_3)
    {'arg1': 'arg1', 'arg2': 123}
    >>> get_arguments("arg1", arguments_3)
    {'arg1': 'arg1', 'arg2': 1}
    >>> get_arguments("arg1 arg2", arguments_3)
    {'arg1': 'arg1', 'arg2': 1}

    >>> arguments_4 = {"arg1": "float"}
    >>> get_arguments("123", arguments_4)
    {'arg1': 123.0}
    >>> get_arguments("123.456", arguments_4)
    {'arg1': 123.456}

    >>> arguments_5 = {"arg1": "date"}
    >>> get_arguments("01012000", arguments_5)
    {'arg1': None}
    >>> get_arguments("text", arguments_5)
    {'arg1': None}
    >>> get_arguments("01/02/2000", arguments_5)
    {'arg1': None}
    >>> get_arguments("01:02:2000", arguments_5)
    {'arg1': None}
    >>> get_arguments("01.02.2000", arguments_5)
    {'arg1': datetime.datetime(2000, 2, 1, 0, 0)}
    >>> get_arguments("2000.02.01", arguments_5)
    {'arg1': datetime.datetime(2000, 2, 1, 0, 0)}
    """
    validate_arguments(arguments)

    if not arguments:
        return {}

    if not text:
        return {
            k: (v[1] if isinstance(v, tuple) else None) for k, v in arguments.items()
        }

    types = [(t[0] if isinstance(t, tuple) else t) for t in arguments.values()]
    args = [text.strip()] if "long str" in types else text.strip().split()

    result: dict[str, _ReturnTypes] = {k: None for k in arguments}
    defaults = ((d[1] if isinstance(d, tuple) else None) for d in arguments.values())

    for i, (n, t, d) in enumerate(zip(arguments, types, defaults)):
        try:
            arg = args[i]
        except IndexError:
            result[n] = d
        else:
            result[n] = __process_value(t, arg, d)

    return result


def validate_arguments(
    arguments: dict[str, _DataTypes | tuple[_DataTypes, Any]],
) -> None:
    if arguments == {}:
        return
    if not isinstance(arguments, dict):
        raise TypeError("arguments must be a dict")
    if any(len(t) != 2 for t in arguments.values() if isinstance(t, tuple)):
        raise SyntaxError(
            "tuple must contain exactly 2 elements: (type, default_value)"
        )

    types = [(t[0] if isinstance(t, tuple) else t) for t in arguments.values()]

    if types.count("long str") > 1:
        raise SyntaxError("multiple starred expressions in assignment")

    if types.count("long str") and len(types) > 1:
        raise SyntaxError('parameter after or before "long str"')


def __process_value(
    arg_type: _DataTypes,
    value: str,
    default: Any = None,
) -> _ReturnTypes:
    match arg_type:
        case "str":
            return value
        case "long str":
            return value
        case "int":
            try:
                return int(value)
            except ValueError:
                try:
                    return int(float(value))
                except ValueError:
                    return default
        case "float":
            try:
                return float(value)
            except ValueError:
                return default
        case "date":
            try:
                return datetime.strptime(value, "%d.%m.%Y")
            except ValueError:
                try:
                    return datetime.strptime(value, "%Y.%m.%d")
                except ValueError:
                    return default
        case _:
            return value


def getargs(
    text: str,
) -> Callable[
    [dict[str, _DataTypes | tuple[_DataTypes, Any]]], dict[str, _ReturnTypes]
]:
    def closure(
        arg: dict[str, _DataTypes | tuple[_DataTypes, Any]],
    ) -> dict[str, _ReturnTypes]:
        return get_arguments(text, arg)

    return closure
