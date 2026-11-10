from tokens.tokentypes import tokentype

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
