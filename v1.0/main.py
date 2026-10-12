from tokenizer import tokenize
from evaluator import evaluate

def main():
    while True : 
        eq = input("Enter Expression to Evaluate (0 to Exit) : ")
        if not eq.strip():
            print("Invalid Expression : No Input Provided")
            continue
        if (eq == '0'):
            break
        else :
            if '/0' in eq:
                print("Zero Division Error")
                continue
            elif (eq[0] in '*/%'):
                print("Invalid Expression : Equation Started with ",eq[0])
                continue
            elif '..' in eq:
                print("Invalid Number")
                continue
            else:
                for i in range(len(eq)):
                    if (eq[i] not in '0123456789./*%+-^'):
                        print("Invalid Expression : {} Detected".format(eq[i]))
                        break
                    elif (eq[i] in '+**//%-' and i == len(eq) - 1):
                        print("Invalid Expression : Equation Ended with ",eq[i])
                        break
                else:
                    try:
                        tokens = tokenize(list(eq))
                        ans = evaluate(tokens)
                        print(" = {}".format(ans))
                    except:
                        print("Invalid Expression : No Solution Found")
                        continue

if __name__ == "__main__":
    main()
    