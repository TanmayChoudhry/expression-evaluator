def evaluate(equation):
    while (len(equation) > 1):
        if ('**' in equation):
            i = equation.index('**')
            try: 
                n = i - 1
                count = 1
                while n + 3 < len(equation) - 1:
                    if equation[n+3] == '**':
                        n += 2
                        count += 1
                    else:
                        break
                for i in range(count):
                    equation[n] = float(equation[n]) ** float(equation[n+2])
                    del equation[n+1:n+3]
                    n -= 2
            except:
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
