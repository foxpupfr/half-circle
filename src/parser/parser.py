# Imports

import ast_nodes.sub_nodes.algebra as algebra
from tokens.tokentypes import tokentype
from tokens.token import token
from helpers.binding_values import binding_values
from . import parsing_helpers as parsing_help


# Main Parser

def parse_expr(node_or_expr : list[token]):

    print([x.value for x in node_or_expr])

    # Follows binding_values listed in ./../helpers/binding_values.py for parsing into AST
    for binding_value in binding_values.values():
        
        i = 0
        
        # Slices tokens one by one to check for operators and make up the AST
        while i < len(node_or_expr):
            match node_or_expr[i]:
                
                # If it encounters a bracket specifically '(' token before its chance according to parser came. You dont want '(2x + 3)' to be split into '2x' + '3' , ignoring the brackets (PEDMAS) . So it will skip the node till it finds closing bracket or specifically ')'. So the below case along with the help of a helper function in './parsing_helpers.py' does that for you. When the chance for brackets do come it will be handled far below with its own case.
                                            
                case token(value = val,  type_ = tokentype.LEFT_BRACKET) if node_or_expr[i].binding_val != binding_value:
                    skip_index = parsing_help.manage_brackets(node_or_expr,i) # This helper take index and node_or_expr as parameter
                    i += skip_index

                # The below 'case' checks if the binding value of the current token (operator) is less than the value specified for this pass of the loop if True it does not split the current node and continues.Please Check './../helpers/binding_values.py' for more reference on that.

                case current_token if node_or_expr[i].binding_val < binding_value:
                    pass
                
                
                # If it encounters '=' token
                case token(value = val1,  type_ = tokentype.EQUAL_TO):
                    parent_node = algebra.equal_to_node(
                            parse_expr(node_or_expr[:i:]),
                            parse_expr(node_or_expr[i + 1::])
                            )
                    return parent_node
                
                # If it encounters '-' token
                case token(value = val,  type_ = tokentype.MINUS):
                    parent_node = algebra.subtract_node(
                            parse_expr(node_or_expr[:i:]),
                            parse_expr(node_or_expr[i + 1::])
                            )
                    return parent_node
                
                # If it encounters '+' token
                case token(value = val,  type_ = tokentype.PLUS):
                    parent_node = algebra.add_node(
                            parse_expr(node_or_expr[:i:]),
                            parse_expr(node_or_expr[i + 1::])
                            )
                    return parent_node

                case token(value = val,  type_ = tokentype.MULTIPLY):
                    parent_node = algebra.multiply_node(
                            parse_expr(node_or_expr[:i:]),
                            parse_expr(node_or_expr[i + 1::])
                            )
                    return parent_node
                
                # If it encounters '/' token
                case token(value = val,  type_ = tokentype.DIVIDE):
                    parent_node = algebra.divide_node(
                            parse_expr(node_or_expr[:i:]),
                            parse_expr(node_or_expr[i + 1::])
                            )
                    return parent_node
                
                # If it encounters '^' token 
                # Not supported as of now 
                case token(value = val,  type_ = tokentype.EXPONATION):
                    pass

                # BRACKETS ARE A SPECIAL CASE
                
                # If it encounters '(' token 
                case token(value = val,  type_ = tokentype.LEFT_BRACKET):
                    skip_index = parsing_help.manage_brackets(node_or_expr,i)
                    parent_node = algebra.bracket_node(
                            parse_expr(node_or_expr[i+1 :skip_index:])
                            )
                    return parent_node
                
                # If it encounters a 'variable' token for example x  or y  or z 
                case token(value = val,  type_ = tokentype.VARIABLE):
                    return algebra.variable_node(node_or_expr[i].value)
                
                # If it encounters a 'number' token for example 12 or 2 or 1 
                case token(value = val,  type_ = tokentype.NUMBER):
                    return algebra.number_node(node_or_expr[i].value)

    
            i += 1


