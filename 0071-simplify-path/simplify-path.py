class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        check = path.split('/')
        for i in range(len(check)):
            if check[i] == '.' or len(check[i]) == 0:
                continue
            elif check[i] == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(check[i])
        print(stack)
        return '/' + '/'.join(stack)