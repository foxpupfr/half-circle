# Imports 

import ast_nodes.main_nodes as main_nodes



# Less than or equal to node

class less_than_or_equal_to_node(main_nodes.algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "<="
    def __repr__(self):
        return f"(left : {self.left} <=  right : {self.right})"


