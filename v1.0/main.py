from tokenizer import tokenize
from evaluator import evaluate

def main():
    while True : 
        eq = input("Enter Expression to Evaluate (0 to Exit) :")
        if (eq == '0'):
            break
        else :
            tokens = tokenize(list(eq))
            ans = evaluate(tokens)
            print(" = {}".format(ans))
            
if __name__ == "__main__":
    main()
