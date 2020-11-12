class BalanceParenthesesSol(object):

    def balance_check(self, s):
        if len(s) % 2 != 0:
            return False
        #what is a set??
        opening = set('([{')
        matches = {('(', ')'), ('[', ']'), ('{', '}')}
        # a python list can operate as a stack
        stack = []

        for paren in s:
           # pushing the parentheses if its an opening one
            if paren in opening:
                stack.append(paren)
            else:
                #if there are not a corresponding opening parentheses, there is not match
                if len(stack) == 0:
                    return False
                last_open = stack.pop()
                # this notation can be used because matches is a tuple
                if (last_open, paren) not in matches:
                    return False

        return len(stack) == 0


x = BalanceParenthesesSol()
print(x.balance_check('[()]'))
#matches = set([('(', ')'), ('[', ']'), ('{', '}')])
