from tokens.tokentypes import tokentype

# Here we will check and assign binding values for each kind of token 
# These binding values are meant to change as this project grows hence this file 

# CURRENT VALUES    

binding_values = {
        tokentype.EQUAL_TO : 7,
        tokentype.MINUS : 6,
        tokentype.PLUS : 5,
        tokentype.MULTIPLY : 4,
        tokentype.DIVIDE : 3,
        tokentype.EXPONATION : 2,
        tokentype.LEFT_BRACKET : 1,
        tokentype.VARIABLE : 0,
        tokentype.NUMBER : 0
}



def check_binding_value(type_):
    match type_:
        case tokentype.VARIABLE:
            return 0

        case tokentype.NUMBER:
            return 0

        case tokentype.EQUAL_TO:
            return binding_values[type_]

        case tokentype.MINUS:
            return binding_values[type_]

        case tokentype.PLUS:
            return binding_values[type_]

        case tokentype.MULTIPLY:
            return binding_values[type_]

        case tokentype.DIVIDE:
            return binding_values[type_]

        case tokentype.EXPONATION:
            return binding_values[type_]

        case tokentype.LEFT_BRACKET | tokentype.RIGHT_BRACKET:
            return binding_values[type_]
