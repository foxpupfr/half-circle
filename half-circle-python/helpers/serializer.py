import ast_nodes.sub_nodes.algebra.algebra as algebra


def serialize(ast):
    serialized_ast = ""
    match ast:
        case algebra.number_node():
            serialized_ast += ast.value
            return serialized_ast
        case algebra.variable_node():
            serialized_ast += ast.value
            return serialized_ast
        case _:
            serialized_ast += serialize(ast.left) + " " + ast.operator + " " + serialize(ast.right)
            return serialized_ast
