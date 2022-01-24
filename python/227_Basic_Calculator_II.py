class Solution:
    def calculate(self, s: str) -> int:
        
        s = s.replace(' ','')
        res = []
        currentNumber = ''
        operation = '+'
            
        for i, si in enumerate(s):
            
            currentChar = si
            if currentChar.isdigit():
                currentNumber += currentChar
            
            if not currentChar.isdigit() or i == len(s) - 1:
                
                currentNumber = int(currentNumber)
                if operation == '-':
                    res.append(-currentNumber)

                elif operation == '+':
                    res.append(currentNumber)

                elif operation == '*':
                    top = res.pop(-1)
                    res.append(int(currentNumber) * int(top))
                     
                elif operation == '/':
                    top = res.pop(-1)
                    sign = 1 if int(top) // int(currentNumber) > 0 else -1
                    res.append(abs(int(top)) // abs(int(currentNumber)) * sign)
                    
                operation = currentChar
                currentNumber = ''
        
        
        result = 0
        if res:
            result = sum(res)

        return result

if __name__ == '__main__':


    s = "2+ 4 / 2 * 9"
    ans = Solution().calculate(s)
    print(ans)