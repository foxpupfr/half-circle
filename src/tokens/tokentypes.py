from enum import Enum


class tokentype(Enum):

# Main operators
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    EXPONATION = "^"
    LEFT_BRACKET = "("
    RIGHT_BRACKET = ")"


# Comparsional, Relational and Other operators
    EQUAL_TO = "="
    NOT = "!"
    NOT_EQUAL_TO = "!="
    GREATER_THAN = ">"
    LESS_THAN = "<"
    GREATER_THAN_OR_EQUAL_TO = ">="
    LESS_THAN_OR_EQUAL_TO = "<="
    

# Whitespace
    WHITESPACE = " "

# Variable
    VARIABLE = "var"

# Numbers
    NUMBER = "num"
