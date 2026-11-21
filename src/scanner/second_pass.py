# Imports

from tokens.tokentypes import tokentype



# Second pass for grouping and cleaning up

def second_pass(token_list):

    i = 0  
    
    # Slices the token list in pairs of two like [element_1, element_2]
    while i < len(token_list):
        match token_list[i : i + 2]:

            # Catches token pairs like [x, 5] converts it into [5, *, x]  
            case [(val1, tokentype.VARIABLE), (val2, tokentype.NUMBER)]:
                token_list[i], token_list[i + 1] = token_list[i + 1], token_list[i]
                token_list.insert(i+1, ("*",tokentype.MULTIPLY))
            
            # Catches token pairs like [5, x] converts it into [5, *, x]
            case [(val1, tokentype.NUMBER), (val2, tokentype.VARIABLE)]:
                token_list.insert(i+1, ("*",tokentype.MULTIPLY))
            
            # Catches token pairs like [x, (] or [5, (] converts it into [x, *, (] or [5, *, (]
            case [(val1, tokentype.VARIABLE), (val2, tokentype.LEFT_BRACKET)] | [(val1, tokentype.NUMBER), (val2, tokentype.LEFT_BRACKET)]:
                token_list.insert(i+1, ("*",tokentype.MULTIPLY))
            
            # Catches token pairs  like [), x] or [), 5] converts it into [), *, x] or [), *, 5]
            case [(val1, tokentype.RIGHT_BRACKET), (val2, tokentype.VARIABLE)] | [(val1, tokentype.RIGHT_BRACKET), (val2, tokentype.NUMBER)]:
                token_list.insert(i+1, ("*",tokentype.MULTIPLY))
            
            # Catches token pairs like [>, =] converts it into [>=,]
            case [(val1, tokentype.GREATER_THAN),(val2, tokentype.EQUAL_TO)]:
                token_list.insert(i + 1, (">=", tokentype.GREATER_THAN_OR_EQUAL_TO))
                token_list.pop(i)
                token_list.pop(i + 1)
            
            # Catches token pairs like [<, =] converts it into [<=,]
            case [(val1, tokentype.LESS_THAN) , (val2, tokentype.EQUAL_TO)]:
                token_list.insert(i + 1, ("<=", tokentype.LESS_THAN_OR_EQUAL_TO))
                token_list.pop(i)
                token_list.pop(i + 1)
            
            # Catches token pairs like [!, =] converts it into [!=,]
            case [(val1, tokentype.NOT), (val2, tokentype.EQUAL_TO)]:
                token_list.insert(i + 1, ("!=", tokentype.NOT_EQUAL_TO))
                token_list.pop(i)
                token_list.pop(i + 1)
            
            # Catches token pairs like [+, -] converts it into [-,]
            case [(val1, tokentype.PLUS), (val2, tokentype.MINUS)]:
                token_list.pop(i)
            
            # Catches token pairs like [-, +] converts it into [-,]
            case [(val1, tokentype.MINUS), (val2, tokentype.PLUS)]:
                token_list.pop(i)
            
            # Catches token pairs like [-, -] converts it into [+,]
            case [(val1, tokentype.MINUS), (val2, tokentype.MINUS)]:
                token_list.insert(i + 1, ("+", tokentype.PLUS))
                token_list.pop(i)
                token_list.pop(i + 1)
            
            # Catches token pairs like [+, +] converts into [+,]
            case [(val1, tokentype.PLUS) ,(val2,tokentype.PLUS)]:
                token_list.pop(i)
        
        i += 1
    return token_list
