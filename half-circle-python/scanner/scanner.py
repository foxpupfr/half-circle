import scanner.tokentypes as tokentypes

def scan(expr_to_parse):
    tokens = []
    for i in range(len(expr_to_parse)):
        if expr_to_parse[i] >= "a" and expr_to_parse[i] <= "z":
            tokens.append(tokentypes.tokentype.VARIABLE)
        elif expr_to_parse[i] in "1234567890":
            tokens.append(tokentypes.tokentype.NUMBER)
        else:
            tokens.append(tokentypes.tokentype(expr_to_parse[i]))
    return tokens
