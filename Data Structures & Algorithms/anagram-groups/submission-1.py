class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)
        for string in strs:
            count = [0] *26
            for c in string:
                count[ord(c)-ord('a')] +=1
            anagrams_map[tuple(count)].append(string)
        return list(anagrams_map.values())    