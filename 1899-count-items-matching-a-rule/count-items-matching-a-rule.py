class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count = 0
        indexs = ['type', 'color', 'name']
        key = indexs.index(ruleKey)
        for item in items:
            if item[key] == ruleValue:
                count += 1
        return count

