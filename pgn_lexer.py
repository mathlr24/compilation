import re

class PgnLexer:
    def __init__(self):
        self.tokens = []

    def tokenize(self, content):
        self.tokens = []
        pattern = "|".join(f"(?P<{name}>{regex})" for name, regex in TOKENS)
        for match in re.finditer(pattern, content):
            name = match.lastgroup
            value = match.group(name)
            if name not in IGNORED_TOKENS:
                if name == "MOVE" and value in RESULTS:
                    name = "RESULT"
                self.tokens.append(Token(name, value))
        return self.tokens

TOKENS = [
    ("OPEN_BRACKET", "\["),
    ("CLOSE_BRACKET", "\]"),
    # Keywords
    ("EVENT", "Event"),
    ("SITE", "Site"),
    ("DATE", "Date"),
    ("ROUND", "Round"),
    ("WHITE", "White"),
    ("BLACK", "Black"),

    ("STRING", "\".*?\""),
    ("NUMBER", "\d+\."),
    ("MOVE", "(?<![\d-])(?!1-0|0-1|1/2-1/2)[A-Za-z0-9#+=()!?-]+"),
    ("RESULT", r"\s1-0|0-1|1/2-1/2"),  # nouveau jeton pour les résultats
    ("COMMENT", "{.*?}"),
]


IGNORED_TOKENS = ["COMMENT","RESULT"]

RESULTS = ["1-0", "0-1", "1/2-1/2"]


class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}({self.value})"
