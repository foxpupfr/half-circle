
import scanner.scanner as scanner
import parser.parser as parser

expr_to_parse = input("Please enter the expression to evaluate : ")

token_list = scanner.scan(expr_to_parse)
print(token_list)
parser.parse(token_list)
