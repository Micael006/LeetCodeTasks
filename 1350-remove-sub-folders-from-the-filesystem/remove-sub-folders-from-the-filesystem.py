import pprint

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folders_dict = dict()
        for name in folder:
            cur = name[1:].split('/')
            helper = folders_dict
            for key in cur:
                if key not in helper:
                    helper[key] = dict()
                helper = helper[key]
            helper['$'] = dict()
        
        answer = []
        q = deque()
        for key in folders_dict:
            q.append([key, folders_dict[key], []])

        while q:
            cur_key, helper, cur_path = q.popleft()
            if '$' in helper:
                answer.append('/' + '/'.join(cur_path + [cur_key]))
            else:
                for key in helper:
                    q.append([key, helper[key], cur_path + [cur_key]])
        


        return answer