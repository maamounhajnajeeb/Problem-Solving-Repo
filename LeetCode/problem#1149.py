Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) == 0 and len(text1) == 0:
            return 0
        table = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    table[i+1][j+1] = 1 + table[i][j]
                else:
                    table[i+1][j+1] = max(table[i+1][j], table[i][j+1])
        return table[-1][-1]
