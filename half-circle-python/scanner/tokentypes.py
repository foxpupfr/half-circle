from enum import Enum


class tokentype(Enum):

# basic operators
    PLUS = "+"
    MINUS = "-"
    MULPLICATION = "*"
    DIVISION = "/"

    EQUAL_TO = "="
    NOT = "!"
    GREATER_THAN = ">"
    LESS_THAN = "<"
    NOT_EQUAL_TO = "!="
    GREATER_THAN_OR_EQUAL_TO = ">="
    LESS_THAN_OR_EQUAL_TO = "<="
    
    LEFT_BRACKET = "("
    RIGHT_BRACKET = ")"

# whitespace
    WHITESPACE = " "

# variable
    VARIABLE = "var"

# numbers
    NUMBER = "num"
