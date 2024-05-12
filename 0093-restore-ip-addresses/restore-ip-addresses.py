class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        answer = set()
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s) - 1):
                for k in range(j + 1, len(s) - 1):
                    new_ip = s[:i + 1] + '.' + s[i + 1: j + 1] + '.' + s[j + 1: k + 1] + '.' + s[k+1:]
                    nums = new_ip.split('.')
                    validated = True
                    for z in range(len(nums)):
                        if nums[z] != str(int(nums[z])) or int(nums[z]) > 255:
                            validated = False
                    if validated:
                        answer.add(new_ip)
        return list(answer)