import ast_nodes.main_nodes as main_nodes

class variable_node(main_nodes.algebra):
    def __init__(self, value, sign = "+"):
        self.value = value
        self.sign = sign 
    def __repr__(self):
        return f"var({self.value})"
