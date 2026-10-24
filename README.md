# half-circle

A custom Computer Algebra System (CAS) written from scratch in Python Which aims to solve high school and collage level mathematics problems.

The orginal goal is to learn maths by building this CAS and also making a tool which can explain maths while solving without missing any details so others can learn

This project is being build from pure intuition of how things should be withoput using no external help

## Table of Contents
- [About The Project](#half-circle)
- [Small Demo](#small-demo)
- [Scanner](#scanner)
- [Parser](#parser)
- [Serializer](#serializer)
- [Solver](#solver)
- [Trying It Out](#trying-it-out)
- [Known bugs](#known-bugs)

### Small Demo

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b887ccee-d680-4492-bf60-23f6dc889ff0" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cab34f65-8785-45e0-aae2-4556a4832565" />

## Scanner

- The scanner is almost decided as of now and has three passes

- **First Pass** : In first pass scanner splits out raw tokens in form of list containing tuples (this is probably not easily readable)
- **Eg** : 
```
Please enter the expression to evaluate :  x + -5 = 10
[('x', <tokentype.VARIABLE: 'var'>), ('+', <tokentype.PLUS: '+'>), ('-', <tokentype.MINUS: '-'>), ('5', <tokentype.NUMBER: 'num'>), ('=', <tokentype.EQUAL_TO: '='>), ('10', <tokentype.NUMBER: 'num'>)]
```

- **Second Pass** : In second pass the scanner groups some of tokens and also cleans up a bit also handles things like implicit multiplication
- **Eg** : *converting `+-` into `-`, converting `>` and `=` tokens which are nearby to `>=` etc...*
```
[('x', <tokentype.VARIABLE: 'var'>), ('-', <tokentype.MINUS: '-'>), ('5', <tokentype.NUMBER: 'num'>), ('=', <tokentype.EQUAL_TO: '='>), ('10', <tokentype.NUMBER: 'num'>)]
```

- **Third pass** : In third pass scanner converts these tokens in tuples into object for easier handling by the parser
- **Eg** :
```
[token(x, tokentype.VARIABLE,0), token(-, tokentype.MINUS,6), token(5, tokentype.NUMBER,0), token(=, tokentype.EQUAL_TO,7), token(10, tokentype.NUMBER,0)]
```

## Parser

- The parser has been completed as of now.
- I have used concepts from pratt parsing which i didn't realise while building and were implicitly added
  
- The parser does only one pass
- **Eg** :
``` 
THE  ENGINE IS CONVERTING THE PROBLEM INTO AN AST...

(left : subtract(left: var(x),  right : num(5)) =  right : num(10))
```

## Serializer 

- I have also build a serliizer which can remake ast into human readable string 
- **Eg** : 
```
x - 5 = 10
```

## Solver 

Solver is work under progress because i need to figure more things 

I also want to make it moduler so i can add calculus, trignometry and other things later

## Trying it out 

- you can clone this github repo and enter the python version folder then run the main.py
```
git clone https://github.com/foxpupfr/half-circle.git
cd half-circle/half-circle-python
python3 main.py
```

## known bugs

- it may have issue with paranthesis and uniary plus or minus 
- i aim to fix this bug one i can solve basic liner equations
