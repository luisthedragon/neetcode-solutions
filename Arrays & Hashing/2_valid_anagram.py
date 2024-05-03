class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_letters = dict()
        t_letters = dict()
        for i in range(len(s)):
            if s[i] not in s_letters:
                s_letters[s[i]] = 1
            else:
                s_letters[s[i]] += 1

            if t[i] not in t_letters:
                t_letters[t[i]] = 1
            else:
                t_letters[t[i]] += 1

        return s_letters == t_letters


tests = [
    (
        ("anagram", "nagaram"),
        True,
    ),
    (
        ("rat", "car"),
        False,
    ),
]
