class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        # ans = []
        for i in range(len(expression)):
            oper = expression[i]
            if oper in "+-*":
                sub_str1 = expression[0:i]
                sub_str2 = expression[i+1:]
                s1 = self.diffWaysToCompute(sub_str1)
                s2 = self.diffWaysToCompute(sub_str2)
                for elem_left in s1:
                    for elem_right in s2:
                        if oper == "*":
                            res.append(int(elem_left) * int(elem_right))
                        elif oper == "+":
                            res.append(int(elem_left) + int(elem_right))
                        elif oper == "-":
                            res.append(int(elem_left) - int(elem_right))
        if len(res) == 0:
            res.append(int(expression))
        # print(res)
        return res