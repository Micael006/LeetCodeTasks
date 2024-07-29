class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        simplified = [x for x in path.split('/') if x != '' and x != '.']
        for elem in simplified:
            if elem == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(elem)
        
        return '/' + '/'.join(stack)