from ast_nodes.main_nodes import algebra

class add(algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "+"
    def __repr__(self):
        return f"add(left : {self.left},  right : {self.right})"

class subtract(algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "-"
    def __repr__(self):
        return f"subtract(left: {self.left},  right : {self.right})"

class multiply(algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "*"
    def __repr__(self):
        return f"multiply(left : {self.left},  right : {self.right})"

class divide(algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "/"
    def __repr__(self):
        return f"divide(left : {self.left},  right : {self.right})"

class equal_to(algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "="
    def __repr__(self):
        return f"(left : {self.left} =  right : {self.right})"    

class not_equal_to(algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "!="
    def __repr__(self):
        return f"(left : {self.left} !=  right : {self.right})"    

class greater_than(algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = ">"
    def __repr__(self):
        return f"(left : {self.left} >  right : {self.right})"    

class less_than(algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "<"
    def __repr__(self):
        return f"(left : {self.left} <  right : {self.right})"    

class greater_than_or_equal_to(algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = ">="
    def __repr__(self):
        return f"(left : {self.left} >=  right : {self.right})"    

class less_than_or_equal_to(algebra):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.operator = "<="
    def __repr__(self):
        return f"(left : {self.left} <=  right : {self.right})"    

class left_bracket(algebra):
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

class variable(algebra):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"var({self.value})"

class number(algebra):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"num({self.value})"

