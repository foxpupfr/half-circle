# Imports

import ast_nodes.main_nodes as main_nodes



# Subtract node

class subtract_node(main_nodes.algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "-"
    def __repr__(self):
        return f"subtract(left: {self.left},  right : {self.right})"
