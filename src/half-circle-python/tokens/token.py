class token:
    def __init__(self,value,type_,binding_val):
        self.value = value
        self.type_ = type_
        self.binding_val = binding_val
    def __repr__(self):
        return f"token({self.value}, {self.type_},{self.binding_val})"
    def __eq__(self, other):
        if isinstance(other, token):
            return self.value == other.value and self.type_ == other.type_ and self.binding_val == other.binding_val
        return False

