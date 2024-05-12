class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        new_grid = []
        for i in range(len(grid) - 2):
            new_grid.append([0] * (len(grid) - 2))

        def add_to_deque(d, elem, index):
            if len(d) > 0:
                if index - d[0][1] >= 3:
                    d.popleft()
            while len(d) > 0:
                if d[-1][0] > elem:
                    break
                d.pop()
            d.append((elem, index))

        def create_buffer(startIndex):
            b = []
            for i in range(startIndex, startIndex + 3):
                new_deque = deque()
                for j in range(2):
                    add_to_deque(new_deque, grid[i][j], j)
                b.append(new_deque)
            return b
        for i in range(len(grid) - 2):
            buffer = create_buffer(i)
            #print(f"first_buffer:")
            #print(*buffer, sep='\n')
            for j in range(len(grid) - 2):
                for z in range(len(buffer)):
                    add_to_deque(buffer[z], grid[i + z][j + 2], j + 2)
                #print()
                #print(f"buffer{i}{j}")
                #print(*buffer, sep='\n')
                new_grid[i][j] = max(buffer[0][0][0], buffer[1][0][0], buffer[2][0][0])
        #print()
        #print("new_grid")
        #print(*new_grid, sep='\n')
        return new_grid
        