class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_1 = []
        word_2 = []
        for i in s:
            word_1.append(i)
        for i in t: 
            word_2.append(i)
        if sorted(word_1) == sorted(word_2):
            return True
        else:
            return False