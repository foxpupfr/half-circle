import ast_nodes.main_nodes as main_nodes
import ast_nodes.sub_nodes.algebra as algebra


class divide_node(main_nodes.algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "/"
    def __repr__(self):
        return f"divide(left : {self.left},  right : {self.right})"
