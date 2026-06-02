class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        #iterate through, add nums to a stack
        #if encounter an operator, take last two of stack, peform funciton, append result of function to end of stack
        #return total

        for i in range(len(tokens)):
            if tokens[i] in operators:
                num2 = stack.pop()
                stack[-1] = self.operatorFunction(stack[-1], num2, tokens[i])
            else:
                stack.append(int(tokens[i]))

        return stack[0]

    def operatorFunction(self, num1, num2, operator) -> int:
        if operator == "+":
            result = num1 + num2
        elif operator == "-": 
            result = num1 - num2
        elif operator == "*": 
            result = num1 * num2
        elif operator == "/": 
            result = int(num1 /  num2)

        return result