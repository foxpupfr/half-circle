# half-circle

A custom Computer Algebra System (CAS) written from scratch in Python Which aims to solve high school and college level mathematics problems.

The orginal goal is to learn maths by building this CAS and also making a tool which can explain maths while solving without missing any details so others can learn.Hence in this state it outputs everything it handles data including all nodes

This project is being build from pure intuition of how things should be from first principles

## Table of Contents
- [About The Project](#half-circle)
- [Screenshots](#screenshots)
- [Scanner](#scanner)
- [Parser](#parser)
- [Serializer](#serializer)
- [Solver](#solver)
- [Trying It Out](#trying-it-out)
- [Known bugs](#known-bugs)

### Screenshots

<img width="1972" height="1104" alt="image" src="https://github.com/user-attachments/assets/af0d8c10-3e2f-4144-92a5-4a8c464f5cbc" />

<img width="1972" height="1104" alt="image" src="https://github.com/user-attachments/assets/d4dc6823-21c9-49a0-9beb-6dedd7953d1d" />

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

- This parser uses concepts from pratt parsing which I didn't realise while building and were implicitly added
- The parser does only one pass
- **Eg** :
``` 
THE  ENGINE IS CONVERTING THE PROBLEM INTO AN AST...

(left : subtract(left: var(x),  right : num(5)) =  right : num(10))
```

## Serializer 

- A serializer which can remake ast into human readable string 
- **Eg** : 
```
x - 5 = 10
```

## Solver 

- As of now the solver can solve numeric expressions like '2 * (2 + 3) + 3 * (4 - 1)'
- It is still not able to solve Algebra as of now 


## Trying it out 

- You can download from the [releases](https://github.com/foxpupfr/half-circle/releases) page.
- Make sure to make it executable if on Linux with `chmod +x half-circle` then `./half-circle-linux`
- On windows it may display weird characters cause it as primarily made for Linux windows support will be improved also make sure to run it in powershell with `./half-cricle-windows.exe`

-               OR

- You can clone this github repo and enter the python version folder then run the main.py

```
git clone https://github.com/foxpupfr/half-circle.git
cd half-circle/src
python3 main.py
```

## known bugs

- It has issues with unary plus or minus 
