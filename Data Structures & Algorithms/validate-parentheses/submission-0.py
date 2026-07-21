class Solution:
    def isValid(self, s: str) -> bool:
        compair = {')':'(',
                    '}':'{',
                    ']':'['}
        temp = []
        for bracket in s:
            if bracket not in compair:
                temp.append(bracket)
            else:
                if not temp:
                    return False
                bra = temp.pop()
                if compair[bracket] != bra:
                    return False
        return len(temp) == 0