class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        cur = []
        def generate(opened, closed):
            if opened < n:
                cur.append('(')
                generate(opened + 1, closed)
                cur.pop()
            
            if closed < opened:
                cur.append(')')
                generate(opened, closed + 1)
                cur.pop()

            if opened == closed == n:
                answer.append(''.join(cur))
                return
        
        generate(0, 0)
        return answer
            
