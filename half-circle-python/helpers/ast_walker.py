import ast_nodes.sub_nodes.algebra as algebra



variables = {}
def tree_walk(ast):
    #so we have to look at base node first then recurive call tree walker ig 
    # aslo add varible and tuype to dict ig yeah thats it ig 
    match ast:
        case algebra.variable():
            variables[ast.value] = variables.get(ast.value, 0) + 1
        case algebra.number():
            pass
        case _:
            left_node = tree_walk(ast.left)
            right_node = tree_walk(ast.right)
            parent_node = left_node, right_node  #this creates a tuple if you wonder
    return variables
        
   
