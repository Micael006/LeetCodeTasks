# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.data = []
        for item in nestedList:
            helper = deque()
            helper.append(item)
            while len(helper) > 0:
                cur_item = helper.popleft()
                if cur_item.isInteger():
                    self.data.append(cur_item.getInteger())
                else:
                    for arr in cur_item.getList()[::-1]:
                        helper.appendleft(arr)
        self.cur_index = -1
                   
    def next(self) -> int:
        if self.cur_index < len(self.data) - 1:
            self.cur_index += 1
            return self.data[self.cur_index]
        else:
            raise StopIteration
    
    def hasNext(self) -> bool:
        if self.cur_index < len(self.data) - 1:
            return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())