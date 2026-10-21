from tokens.tokentypes import tokentype
from tokens.token import token
from tokens.binding_values import check_binding_value

#first pass for basic token splitting 
def first_pass(expr_to_scan):

    token_list = []
    i = 0 # "i" stands for index i think
        
    while i < len(expr_to_scan):
        match expr_to_scan[i]:
            case "+":
                token_list.append(("+",tokentype.PLUS))

            case "-":
                token_list.append(("-",tokentype.MINUS))

            case "*":
                token_list.append(("*",tokentype.MULTIPLY))

            case "/":
                token_list.append(("/",tokentype.DIVIDE))

            case "=":
                token_list.append(("=",tokentype.EQUAL_TO))

            case ">":
                token_list.append((">",tokentype.GREATER_THAN))

            case "<":
                token_list.append(("<",tokentype.LESS_THAN))

            case "(":
                token_list.append(("(", tokentype.LEFT_BRACKET))

            case ")":
                token_list.append((")", tokentype.RIGHT_BRACKET))

            case char if char.islower() and char.isalpha():
                token_list.append((expr_to_scan[i],tokentype.VARIABLE))

            case char if char.isdigit():
                number, skip_index = tokenify_numbers_ahead(expr_to_scan, i)
                if number == None:
                    return None
                i += skip_index
                token_list.append((number,tokentype.NUMBER))

        i += 1

    return token_list


#helper function for first_pass
def tokenify_numbers_ahead(expr_to_scan, i): # To group numbers
    skip_index = 0
    number = ""

    while True:
        if expr_to_scan[i + skip_index].isdigit():
            number += expr_to_scan[i + skip_index]
        elif expr_to_scan[i + skip_index] == "." and expr_to_scan[i + skip_index + 1].isdigit():
            number += "."
        else:
            break
        skip_index += 1
    
    if number.count(".") > 1: 
        print ("\033[91mScanner Error : invalid use of '.'\033[0m")
        return None, None
    return number, skip_index


# seond pass for grouping and cleaning up
def second_pass(token_list):

    i = 0  

    while i < len(token_list):
        match token_list[i : i + 2]:

            case [(val1, tokentype.VARIABLE), (val2, tokentype.NUMBER)]:
                token_list[i], token_list[i + 1] = token_list[i + 1], token_list[i]
                token_list.insert(i+1, ("*",tokentype.MULTIPLY))

            case [(val1, tokentype.NUMBER), (val2, tokentype.VARIABLE)]:
                token_list.insert(i+1, ("*",tokentype.MULTIPLY))

            case [(val1, tokentype.GREATER_THAN),(val2, tokentype.EQUAL_TO)]:
                token_list.insert(i + 1, (">=", tokentype.GREATER_THAN_OR_EQUAL_TO))
                token_list.pop(i)
                token_list.pop(i + 1)

            case [(val1, tokentype.LESS_THAN) , (val2, tokentype.EQUAL_TO)]:
                token_list.insert(i + 1, ("<=", tokentype.LESS_THAN_OR_EQUAL_TO))
                token_list.pop(i)
                token_list.pop(i + 1)

            case [(val1, tokentype.NOT), (val2, tokentype.EQUAL_TO)]:
                token_list.insert(i + 1, ("!=", tokentype.NOT_EQUAL_TO))
                token_list.pop(i)
                token_list.pop(i + 1)

            case [(val1, tokentype.PLUS), (val2, tokentype.MINUS)]:
                token_list.pop(i)

            case [(val1, tokentype.MINUS), (val2, tokentype.PLUS)]:
                token_list.pop(i)

            case [(val1, tokentype.MINUS), (val2, tokentype.MINUS)]:
                token_list.insert(i + 1, ("+", tokentype.PLUS))
                token_list.pop(i)
                token_list.pop(i + 1)

            case [(val1, tokentype.PLUS) ,(val2,tokentype.PLUS)]:
                token_list.pop(i)
        
        i += 1
    return token_list


#third pass for object conversation
def third_pass(token_list):

    final_token_list = []

    for i in range(len(token_list)):
        value, type_ = token_list[i]
        binding_val = check_binding_value(type_)
        final_token_list.append(token(value, type_, binding_val)) # conversion into objects

    return final_token_list
