class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = defaultdict(list)
        for word in strs:
            sort = ''.join(sorted(word))
            diction[sort].append(word)
        return list(diction.values())
