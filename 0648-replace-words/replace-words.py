class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = []
        for elem in sentence.split():
            found = False
            for i in range(len(elem)):
                if elem[:i + 1] in dictionary:
                    ans.append(elem[:i + 1])
                    found = True
                    break
            if not found:
                ans.append(elem)
        return ' '.join(ans)
