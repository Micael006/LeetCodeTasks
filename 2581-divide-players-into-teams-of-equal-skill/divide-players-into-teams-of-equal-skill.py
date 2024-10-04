class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        team_skill = skill[0] + skill[-1]
        answer = 0

        for i in range(len(skill) // 2):
            if skill[i] + skill[-i - 1] != team_skill:
                return -1
            answer += skill[i] * skill[-i - 1]
        
        return answer