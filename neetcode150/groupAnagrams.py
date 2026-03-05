# Group Anagrams
# Given an array of strings strs, gruop all anagrams together into sublists.
# You may return the output in any order

# An anagram is a string that contains the exact same characters as another string, 
# but the order of the characters can be different.

# Example 1
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2
# Input: strs = ["x"]
# Output: [["x"]]

# Example 3
# Input: strs = [""]
# Output: [[""]]

# Reflection: I didn't fully read question, really didn't even understand the anagram before implementing (1)
# I didn't implement it properly (2)
# using dictionaries is apparently the same thing as a hashtable 

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # two for loops
        # one to keep track of current loop, index of list
        # other to keep track of the string

        res = defaultdict(list)
        n = len(strs)

        for i in range(n):
            key = "".join(sorted(strs[i]))
            res[key].append(strs[i])

        return list(res.values())