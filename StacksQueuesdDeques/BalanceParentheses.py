class BalanceParentheses(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addSymbol(self, item):
        self.items.append(item)

    def removeSymbol(self, item):
        return self.items.pop()

    def print_items(self):
        print(self.items)

    def evalBalance(self, expression, ):
        square_open = 0
        square_close = 0
        parentheses_open = 0
        parentheses_close = 0
        curly_open = 0
        curly_close = 0
        for char in expression:
            if char == "[":
                square_open += 1
                self.addSymbol(char)
                self.print_items()
            elif char == "(":
                parentheses_open += 1
                self.addSymbol(char)
                self.print_items()
            elif char == "{":
                curly_open += 1
                self.addSymbol(char)
                self.print_items()
            else:
                last_open = self.removeSymbol(char)
                if char == "]" and last_open == "[":
                    print("True")
                    return True
                elif char == ")" and last_open == "(":
                    print("True")
                    return True
                elif char == "}" and last_open == "{":
                    print("True")
                    return True
                else:
                    print("False")
                    return False
                print(last_open)

        self.print_items()



eval_exp = BalanceParentheses()
eval_exp.evalBalance("([])")









