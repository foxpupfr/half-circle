# Imports 

import ast_nodes.main_nodes as main_nodes



# Left bracket

class bracket_node(main_nodes.algebra):
    def __init__(self, value):
        self.operators = ("(", ")")
        self.value = value
    def __repr__(self):
        return f"bracket( {self.value} )"

