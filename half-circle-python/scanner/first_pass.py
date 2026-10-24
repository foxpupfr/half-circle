from tokens.tokentypes import tokentype

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
    skip_index += -1 #this was added to avoid bug where 5x wont be scanned properly
    
    if number.count(".") > 1: 
        print ("\033[91mScanner Error : invalid use of '.'\033[0m")
        return None, None
    return number, skip_index





