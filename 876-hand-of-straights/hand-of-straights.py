class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True
        d = dict()
        for elem in hand:
            d[elem] = d.get(elem, 0) + 1
        check_keys = sorted(d.keys())
        for key in check_keys:
            if d[key] == 0:
                continue
            for i in range(key + 1, key + groupSize):
                d[i] = d.get(i, 0) - d[key]
                if d[i] < 0:
                    return False
            d[key] = 0
        return True
            