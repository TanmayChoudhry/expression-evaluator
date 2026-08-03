def tokenize(equation):
    tokenized_equation = []
    current_number = ""
    while (len(equation) >  0):
        for i in range(len(equation)):
            if (equation[i] == '*') and (equation[i+1] == '*'):
                tokenized_equation.append(current_number)
                current_number = ''
                tokenized_equation.append('**')
                del equation[i:i+2]
                break
            elif (equation[i] == '/') and (equation[i+1] == '/'):
                tokenized_equation.append(current_number)
                current_number = ''
                tokenized_equation.append('//')
                del equation[i:i+2]
                break
            elif (equation[i] in '*/%^+-'):
                tokenized_equation.append(current_number)
                current_number = ''
                tokenized_equation.append(equation[i])
                del equation[i]
                break
            elif (equation[i].isdigit()) or (equation[i] == '.'):
                current_number += equation[i]
                del equation[i]
                break
    tokenized_equation.append(current_number)
    if tokenized_equation[1] == '-':
        n = tokenized_equation.pop(2)
        tokenized_equation[0:2] = [float('-' + n)]
    return tokenized_equation
