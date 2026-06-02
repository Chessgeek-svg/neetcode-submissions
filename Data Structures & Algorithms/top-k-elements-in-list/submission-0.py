class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k >= len(set(nums)):
            return list(set(nums))

        frequencyMap = {}

        for num in nums:
            if num not in frequencyMap:
                frequencyMap[num] = 1
            else:
                frequencyMap[num] += 1

        mostFrequentArray = []
        dictKeys = list(frequencyMap.keys())
        dictValues = list(frequencyMap.values())

        while k > 0:
            index = dictValues.index(max(dictValues))
            mostFrequentArray.append(dictKeys[index])
            dictValues.pop(index)
            dictKeys.pop(index)
            k -= 1
        
        return mostFrequentArray

        