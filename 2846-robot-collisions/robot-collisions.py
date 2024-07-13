class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = []
        for i in range(len(positions)):
            robots.append([positions[i], healths[i], directions[i], i])
        
        robots.sort(key=lambda tup: tup[0])

        stack = []
        for i in range(len(robots)):
            if robots[i][2] == "L":
                while len(stack) > 0 and stack[-1][2] == "R" and robots[i][1] > 0:
                    if robots[i][1] > stack[-1][1]:
                        robots[i][1] -= 1
                        stack.pop()
                    elif robots[i][1] == stack[-1][1]:
                        robots[i][1] = 0
                        stack.pop()
                    else:
                        robots[i][1] = 0
                        stack[-1][1] -= 1

            if robots[i][1] > 0:
                stack.append(robots[i])
        
        if len(stack) > 0:
            stack.sort(key=lambda tup: tup[3])
        
        return [x[1] for x in stack]
            