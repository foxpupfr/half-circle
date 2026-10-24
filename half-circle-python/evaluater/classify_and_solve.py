from helpers.ast_walker import tree_walk


def classify_and_solve(ast):
    ast_info = tree_walk(ast)
    print(ast_info)
    if len(ast_info) == 1:
        import evaluater.solvers.liner_equation_solver as liner_equation_solver
        liner_equation_solver.solve(ast)
    if len(ast_info) == 0:
        import evaluater.solvers.normal_expression_solver
    else:
        print("Cannot solve the equation with current solvers")
