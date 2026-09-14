class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number1 = self.strval(num1)
        number2 = self.strval(num2)
        return str(number1 * number2)
        
    def strval(self, string) -> int:
        val = 0
        for c in string:
            digit = ord(c)-48
            val *= 10
            val += digit
        return val