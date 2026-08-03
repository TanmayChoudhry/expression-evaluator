def evaluate(equation):
    while (len(equation) > 1):
        if ('**' in equation):
            i = equation.index('**')
            equation[i-1:i+2] = [float(equation[i-1]) ** float(equation[i+1])]
            continue
        elif ('^' in equation):
            i = equation.index('^')
            equation[i-1:i+2] = [float(equation[i-1]) ** float(equation[i+1])]
            continue
        elif ('//' in equation):
            i = equation.index('//')
            equation[i-1:i+2] = [float(equation[i-1]) // float(equation[i+1])]
            continue
        elif ('/' in equation):
            i = equation.index('/')
            equation[i-1:i+2] = [float(equation[i-1]) / float(equation[i+1])]
            continue
        elif ('%' in equation):
            i = equation.index('%')
            equation[i-1:i+2] = [float(equation[i-1]) % float(equation[i+1])]
            continue
        elif ('*' in equation):
            i = equation.index('*')
            equation[i-1:i+2] = [float(equation[i-1]) * float(equation[i+1])]
            continue
        elif ('-' in equation):
            i = equation.index('-')
            equation[i-1:i+2] = [float(equation[i-1]) - float(equation[i+1])]
            continue
        elif ('+' in equation):
            i = equation.index('+')
            equation[i-1:i+2] = [float(equation[i-1]) + float(equation[i+1])]
            continue
    return equation[0]
