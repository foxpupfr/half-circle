import ast_nodes.sub_nodes.algebra as algebra

def is_number_node(node_to_check):
    return isinstance(node_to_check, algebra.number_node)

def is_variable_node(node_to_check):
    return isinstance(node_to_check, algebra.variable_node)

