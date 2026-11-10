from helpers.node_checker import  is_number_node, is_variable_node
import ast_nodes.main_nodes as main_nodes
import ast_nodes.sub_nodes.algebra as algebra

class add_node(main_nodes.algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "+"
    def __repr__(self):
        return f"add(left : {self.left},  right : {self.right})"

    def evaluate_node(self, node):
        match node:
 
            case add_node(left = l, right = r) if is_number_node(l) and is_number_node(r):
                return node.left.value + node.right.value 
            
            # For adding terms like x + x into 2x

            case _:
                return node

