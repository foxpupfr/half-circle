import scanner.scanner as scanner
import parser.parser as parser

expr_to_parse = input("Please enter the expression to evaluate : ")
expr_to_parse += " " # adding space as eof charecter

token_list = scanner.first_pass(expr_to_parse)
print(token_list)
print()

token_list = scanner.second_pass(token_list)
print(token_list)
print()

final_token_list = scanner.third_pass(token_list)
print(final_token_list)

parser.parse(token_list)
