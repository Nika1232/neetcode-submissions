class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for letter in operations:
            if letter == "C":
                result.pop()
            elif letter == "D":
                result.append(result[-1] * 2)
            elif letter == "+":
                result.append(result[-2] + result[-1])
            else:
                result.append(int(letter))
        return sum(result)