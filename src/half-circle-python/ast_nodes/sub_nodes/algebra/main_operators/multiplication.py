import ast_nodes.main_nodes as main_nodes
import ast_nodes.sub_nodes.algebra as algebra

class multiply_node(main_nodes.algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "*"
    def __repr__(self):
        return f"multiply(left : {self.left},  right : {self.right})"

    def evaluate_node(self, node):
        match node:
            case multiply_node(left =  algebra.number_node, right = algebra.number_node):
                return node.left.value * node.right.value
            case _:
                pass
