import scanner as scanner
import parser.parser as parser
import evaluater.classify_and_solve as evaluater

expr_to_parse = input("Please enter the expression to evaluate : ")
expr_to_parse += " " # adding space as eof charecter

#tokenization
token_list = scanner.first_pass.first_pass(expr_to_parse)
print(token_list)
print()

token_list = scanner.second_pass.second_pass(token_list)
print(token_list)
print()

final_token_list = scanner.third_pass.third_pass(token_list)
print(final_token_list)

#conversion into ast
print("\n\033[0;35mTHE  ENGINE IS CONVERTING THE PROBLEM INTO AN AST...\033[0m\n")
ast = parser.parse_expr(final_token_list)
print(ast)
print()

import helpers.serializer as serialize
print(serialize.serialize(ast))
print()

#trying to solve it 
print("solving...\n")
answer = evaluater.classify_and_solve(ast)
print(answer)
