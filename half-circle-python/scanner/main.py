from enum import Enum
class tokentype(Enum):
    NUMBER = str
    PLUS = "+"
    MINUS = "-"
    VARIABLE = "x"
    EQUAL_TO = "="
    WHITESPACE = " "
print(tokentype("+"))
expr_to_parse = "5 + x = 10"
parsed = [] 
for i in expr_to_parse:
    parsed.append(tokentype(i))
print(parsed)
