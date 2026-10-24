import ast_nodes.sub_nodes.algebra as algebra

def solve(ast):
    match:
        case algebra.number:
            pass
        case algebra.variable:
            pass
        case _:
            solve()
