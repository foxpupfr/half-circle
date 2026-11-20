# Imports

from tokens.token import token
from helpers.binding_values import check_binding_value



# Third pass for object conversation

def third_pass(token_list):

    final_token_list = []
    
    # Just loops through and converts eveything into objects under class token
    for i in range(len(token_list)):
        value, type_ = token_list[i]
        binding_val = check_binding_value(type_) # Assigns binding_values for tokens
        final_token_list.append(token(value, type_, binding_val)) # Conversion into objects

    return final_token_list
