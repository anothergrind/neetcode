# Given two strings s and t, return true if the two strings are anagrams of each other,
# otherwise return false.
#
# An anagram is a string that contains the exact same characters as another string,
# but the order of the characters can be different

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

# Constraints: s and t consist of lowercase English letters

# Mistakes I made: I was iterating via range instead of accessing the string directly

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    # strat is to iterate through both strings, and making sure at the end
    # the tally's are the same with a dictionary, but how to do that?
    s_dict = {}
    t_dict = {}

    for char in s:
        if char in s_dict:
            s_dict[char] = s_dict[char] + 1
        else:
            s_dict[char] = 1

    for char in t:
        if char in t_dict:
            t_dict[char] = t_dict[char] + 1
        else:
            t_dict[char] = 1
        
        if s_dict == t_dict:
            return True
        
    return False