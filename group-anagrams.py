class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = dict()
        for s in strs:
            # key = ''.join(sorted(s))
            key = tuple(sorted(s))
            if key in anagram_hash:
                anagram_hash[key].append(s)
            else:
                anagram_hash[key] = [s]
        return [anagram_list for anagram_list in anagram_hash.values()]
