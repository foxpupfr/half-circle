import ast_nodes.sub_nodes.algebra as algebra
from ast_nodes.sub_nodes.algebra.other_operators.greater_than import greater_than_node
import helpers.serializer as serialize

def solve(ast):
    print(serialize.serialize(ast))
    match ast:
        case algebra.number_node():
            try:
                return int(ast.value)
            except ValueError:
                return float(ast.value)
        case algebra.variable_node():
            return ast.value
        case algebra.add_node():
            solved_ast = solve(ast.left) + solve(ast.right)
            return solved_ast
        case algebra.subtract_node():
            solved_ast = solve(ast.left) - solve(ast.right)
            return solved_ast
        case algebra.multiply_node():
            solved_ast = solve(ast.left) * solve(ast.right)
            return solved_ast
        case algebra.divide_node():
            solved_ast = solve(ast.left) / solve(ast.right)
            return solved_ast
        case algebra.equal_to_node():
            solved_ast = solve(ast.left) == solve(ast.right)
            return solved_ast
        case algebra.not_equal_to_node():
            solved_ast = solve(ast.left) != solve(ast.right)
            return solved_ast
        case algebra.greater_than_node():
            solved_ast = solve(ast.left) > solve(ast.right)
            return solved_ast
        case algebra.less_than_node():
            solved_ast = solve(ast.left) < solve(ast.right)
            return solved_ast
        case algebra.greater_than_or_equal_to_node():
            solved_ast = solve(ast.left) >= solve(ast.right)
            return solved_ast
        case algebra.less_than_or_equal_to_node():
            solved_ast = solve(ast.left) <= solve(ast.right)
            return solved_ast
        case algebra.bracket_node():
            solved_ast = solve(ast.value)
            return solved_ast
