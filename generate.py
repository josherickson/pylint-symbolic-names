"""Finds built-in pylint messages and generates a README.md file containing their definitions."""
import inspect
import pkgutil
from pylint import checkers

README_HEADER = (
    '# Pylint Symbolic Names\n\n'
    'The list of symbolic names for every pylint message, which are particularly useful for '
    'disabling warnings in a readable way such as `#pylint: disable=missing-docstring` rather '
    'than `#pylint: disable=C0111`.\n\n'
    'This list was automatically generated using [generate.py](generate.py). You can '
    'also get the list of messages yourself with the built-in pylint command `pylint --list-msgs`.'
    '\n\n'
    '| Code | Symbolic Name | Message |\n'
    '| ---- |-------------- | ------- |\n'
)


def generate_readme(messages: dict, filename: str):
    """Generates a markdown file containing a table with the list of pylint messages."""
    with open(filename, 'w') as readme_file:
        readme_file.write(README_HEADER)
        for key, value in sorted(messages.items()):
            readme_file.write(
                '| {code} | `{symbolic_name}` | {message} |\n'.format(
                    code=key, symbolic_name=value[1], message=_escape_markdown_chars(value[0])
                )
            )


def find_all_messages() -> dict:
    """Iterates through each module under 'pylint.checkers' and returns pylint messages."""
    messages = {}

    for loader, name, _is_pkg in pkgutil.walk_packages(checkers.__path__):
        module = loader.find_module(name).load_module(name)
        _add_messages(module, messages)

    return messages


def _add_messages(module: object, messages: dict):
    """Adds any pylint messages found from BaseChecker-inherited classes within the module."""
    for _name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, checkers.BaseChecker):
            if hasattr(obj, 'msgs'):
                messages.update(obj.msgs)


def _escape_markdown_chars(string: str) -> str:
    """Replaces newlines with spaces and escapes special markdown characters."""
    #pylint: disable=anomalous-backslash-in-string
    return string.replace('\n', ' ').replace('_', '\_').replace('*', '\*').replace('`', '\`')


def main():
    """Finds pylint messages and generates a markdown file containing them."""
    messages = find_all_messages()
    generate_readme(messages, 'README.md')


if __name__ == '__main__':
    main()
