import re

LINK_REGEX = re.compile(r'(?<!\\)\[.+?\]\((.*?)\)')
BTN_URL_REGEX = re.compile(
    r"(\[([^\[]+?)\]\(buttonurl:(?:/{0,2})(.+?)(:same)?\))")

FORMATS = ['**', '`', '```', '__']


def message_parser(message):
    text = message
    LINKS_REGEX_MATCHER = re.findall(LINK_REGEX, text)
    new_string = text
    if LINKS_REGEX_MATCHER:
        for link in LINKS_REGEX_MATCHER:
            justdoit = False
            if link[:2] and link[-2:] in FORMATS:
                new_link = link[2:-2]
                justdoit = True
            elif link[:1] and link[-1:] in FORMATS:
                new_link = link[1:-1]
                justdoit = True
            elif link[:3] and link[-3:] in FORMATS:
                new_link = link[3:-3]
                justdoit = True

            if justdoit:
                new_string = new_string.replace(link, new_link)

    BUTTONS_REGEX_MATCHER = re.findall(BTN_URL_REGEX, new_string)
    buttons = []
    if BUTTONS_REGEX_MATCHER:
        for button in BUTTONS_REGEX_MATCHER:
            btn_name = button[1]
            btn_url = 
            same_row = bool(button[3])
            buttons.append((btn_name, btn_url, same_row))
        string = re.sub(BTN_URL_REGEX, '', new_string)
    else:
        string = new_string
    return string.strip(), buttons


def escape_invalid_curly_brackets(text, valids) -> str:
    new_text = ""
    idx = 0
    while idx < len(text):
        if text[idx] == "{":
            if idx + 1 < len(text) and text[idx + 1] == "{":
                idx += 2
                new_text += "{{{{"
                continue
            else:
                success = False
                for v in valids:
                    if text[idx:].startswith('{' + v + '}'):
                        success = True
                        break
                if success:
                    new_text += text[idx:idx + len(v) + 2]
                    idx += len(v) + 2
                    continue
                else:
                    new_text += "{{"

        elif text[idx] == "}":
            if idx + 1 < len(text) and text[idx + 1] == "}":
                idx += 2
                new_text += "}}}}"
                continue
            else:
                new_text += "}}"

        else:
            new_text += text[idx]
        idx += 1

    return new_text
