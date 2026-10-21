# half-circle

A custom Computer Algebra System (CAS) written from scratch in Python Which aims to solve high school and collage level mathematics problems

## Scanner

- The scanner is almost decided as of now and has three passes

- **First Pass** : In first pass scanner splits out raw tokens in form of list containing tuples
- **Eg** : 
```
Please enter the expression to evaluate : x + -5 = 10
[('x', <tokentype.VARIABLE: 'var'>), ('+', <tokentype.PLUS: '+'>), ('-', <tokentype.MINUS: '-'>), ('5', <tokentype.NUMBER: 'num'>), ('=', <tokentype.EQUAL_TO: '='>), ('10', <tokentype.NUMBER: 'num'>)]
```

- **Second Pass** : In second pass the scanner groups some of tokens and also cleans up a bit \
- **Eg** : *converting `+-` into `-`, converting `>` and `=` tokens which are nearby to `>=` etc...*
```
[('x', <tokentype.VARIABLE: 'var'>), ('-', <tokentype.MINUS: '-'>), ('5', <tokentype.NUMBER: 'num'>), ('=', <tokentype.EQUAL_TO: '='>), ('10', <tokentype.NUMBER: 'num'>)]
```
- **Third pass** : In third pass scanner converts these tokens in tuples into object for easier handling by the parser
- **Eg** :
```
[token(x, tokentype.VARIABLE,0), token(-, tokentype.MINUS,1), token(5, tokentype.NUMBER,0), token(=, tokentype.EQUAL_TO,None), token(10, tokentype.NUMBER,0)]
```

## Parser

- The parser is under design 
  
