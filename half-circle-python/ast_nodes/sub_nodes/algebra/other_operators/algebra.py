import ast_nodes.main_nodes as main_nodes





class equal_to_node(main_nodes.algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "="
    def __repr__(self):
        return f"(left : {self.left} =  right : {self.right})"    

class not_equal_to_node(main_nodes.algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "!="
    def __repr__(self):
        return f"(left : {self.left} !=  right : {self.right})"    

class greater_than_node(main_nodes.algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = ">"
    def __repr__(self):
        return f"(left : {self.left} >  right : {self.right})"    

class less_than_node(main_nodes.algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "<"
    def __repr__(self):
        return f"(left : {self.left} <  right : {self.right})"    

class greater_than_or_equal_to_node(main_nodes.algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = ">="
    def __repr__(self):
        return f"(left : {self.left} >=  right : {self.right})"    

class less_than_or_equal_to_node(main_nodes.algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "<="
    def __repr__(self):
        return f"(left : {self.left} <=  right : {self.right})"    

class left_bracket_node(main_nodes.algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "("
    def __repr__(self):
        return f"left : {self.left},  right : {self.right}"    

# class right_bracket(algebra):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#         self.operator = ")"





