class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs_set = set([tuple(x) for x in obstacles])
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]

        max_dist = 0
        cur_pos = [0, 0]
        cur_dir = 0
        
        for command in commands:
            if command == -1:
                cur_dir += 1
            elif command == -2:
                cur_dir -= 1
            cur_dir %= len(directions)
            step = directions[cur_dir]
            for k in range(command):
                if (cur_pos[0] + step[0], cur_pos[1] + step[1]) in obs_set:
                    break
                cur_pos[0] += step[0]
                cur_pos[1] += step[1]
                max_dist = max(max_dist, cur_pos[0]**2 + cur_pos[1]**2)
            
        return max_dist

