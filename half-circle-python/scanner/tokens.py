class token:
    def __init__(self,value,type_):
        self.value = value
        self.type_ = type_
    def __repr__(self):
        return f"token({self.value}, {self.type_})"

