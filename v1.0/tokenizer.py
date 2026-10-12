def tokenize(equation):
    tokenized_equation = [i for i in equation]
    while True:
        for i in range(len(tokenized_equation)-1):
            if ((tokenized_equation[i][-1].isdigit() or tokenized_equation[i][-1] == '.') and (tokenized_equation[i+1][-1].isdigit() or tokenized_equation[i+1][-1] == '.')) or (tokenized_equation[i] == tokenized_equation[i+1] and tokenized_equation[i] in '/*'):
                tokenized_equation[i] = tokenized_equation[i] + tokenized_equation.pop(i+1)
                break
        else:
            break
    while True:
        for i in range(len(tokenized_equation)):
            if (tokenized_equation[i] == '-'):
                if (tokenized_equation[i-1] in "**//^%+"):
                    tokenized_equation[i] = '-' + tokenized_equation.pop(i+1)
                    break
                else:
                    tokenized_equation[i+1] = '-' + tokenized_equation[i+1]
                    if (i != 0):
                        tokenized_equation[i] = '+'
                    else:
                        tokenized_equation.pop(i)
                    break
        else:
            break
    return tokenized_equation
