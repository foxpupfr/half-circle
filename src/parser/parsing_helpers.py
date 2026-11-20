# ---Imports---

from tokens.token import token
from tokens.tokentypes import tokentype



# ---Helper functions for parsing---


# Bracket Manager : This function is triggered when parser sees a '(' token and then it help to skip all the things inside the bracket last to be parsed 

def manage_brackets(node_or_expr, i):
    
    skip_index = 0
    left_bracket_count = 0
    right_bracket_count = 0
    
    while i < len(node_or_expr):
        
        match node_or_expr[i]:
            case token(value = val,  type_ = tokentype.LEFT_BRACKET):
                left_bracket_count += 1

            case token(value = val,  type_ = tokentype.RIGHT_BRACKET):
                right_bracket_count += 1

        if left_bracket_count == right_bracket_count:
            skip_index += 1
            break
        
        i += 1
        skip_index += 1

    if left_bracket_count != right_bracket_count:
        print("\033[91mParser Error : invalid use of '()'\033[0m")

    return skip_index

            
