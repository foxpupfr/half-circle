import ast.nodes as nodes
from tokens.tokentypes import tokentype
from tokens.token import token
from tokens.binding_values import binding_values


def parse_expr(node_or_expr):

    for binding_value in binding_values.values():
        
        i = 0

        while i < len(node_or_expr):
            match node_or_expr[i]:

                case current_token if node_or_expr[i].binding_val < binding_value:
                    pass

                case token(value = val1,  type_ = tokentype.EQUAL_TO):
                    parent_node = nodes.equal_to(
                            parse_expr(node_or_expr[:i:]),
                            parse_expr(node_or_expr[i + 1::])
                            )
                    return parent_node

                case token(value = val,  type_ = tokentype.MINUS):
                    parent_node = nodes.subtract(
                            parse_expr(node_or_expr[:i:]),
                            parse_expr(node_or_expr[i + 1::])
                            )
                    return parent_node

                case token(value = val,  type_ = tokentype.PLUS):
                    parent_node = nodes.add(
                            parse_expr(node_or_expr[:i:]),
                            parse_expr(node_or_expr[i + 1::])
                            )
                    return parent_node

                case token(value = val,  type_ = tokentype.MULTIPLY):
                    parent_node = nodes.multiply(
                            parse_expr(node_or_expr[:i:]),
                            parse_expr(node_or_expr[i + 1::])
                            )
                    return parent_node

                case token(value = val,  type_ = tokentype.DIVIDE):
                    parent_node = nodes.divide(
                            parse_expr(node_or_expr[:i:]),
                            parse_expr(node_or_expr[i + 1::])
                            )
                    return parent_node

                case token(value = val,  type_ = tokentype.EXPONATION):
                    pass

                case token(value = val,  type_ = tokentype.LEFT_BRACKET) | token(value = val,  type_ = tokentype.RIGHT_BRACKET):
                    parent_node = nodes.left_bracket(
                            parse_expr(node_or_expr[:i:]),
                            parse_expr(node_or_expr[i + 1::])
                            )
                    return parent_node

                case token(value = val,  type_ = tokentype.VARIABLE):
                    return nodes.variable(node_or_expr[i].value)

                case token(value = val,  type_ = tokentype.NUMBER):
                    return nodes.number(node_or_expr[i].value)

    
            i += 1
