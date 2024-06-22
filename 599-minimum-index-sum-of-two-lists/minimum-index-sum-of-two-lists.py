class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        myDict ={}
        myList = []
        for i in range (len(list1)):
            if list1[i] in list2:
                myDict[list1[i]] = i
                j = list2.index(list1[i])
                myDict[list1[i]] += j         
        min_value = min(myDict.values())
        for i ,j in myDict.items():
            if j == min_value:
                myList.append(i)
        return myList
