# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         if not p:
#             return not s
        
#         current_match = bool(s) and p[0] in [s[0], '.']
        
#         if len(p)>=2 and p[1] == '*':
#             return (self.isMatch(s, p[2:]) or current_match and self.isMatch(s[1:], p))
#         else:
#             return current_match and self.isMatch(s[1:], p[1:])
   
# class Solution(object):
#     def isMatch(self, text, pattern):
#         memo = {}
#         def dp(i, j):
#             if (i, j) not in memo:
#                 if j == len(pattern):
#                     ans = i == len(text)
#                 else:
#                     first_match = i < len(text) and pattern[j] in {text[i], '.'}
#                     if j+1 < len(pattern) and pattern[j+1] == '*':
#                         ans = dp(i, j+2) or first_match and dp(i+1, j)
#                     else:
#                         ans = first_match and dp(i+1, j+1)

#                 memo[i, j] = ans
#             return memo[i, j]

#         return dp(0, 0)
    
class Solution(object):
    def isMatch(self, s, p):
        memo = {}
        def dp(i,j):
            if (i,j) not in memo:
            
                if j == len(p):
                    ans = i == len(s)
                    return ans
                current = i < len(s) and p[j] in {s[i], '.'}
                if j+1 < len(p) and p[j+1] == '*':
                    ans = dp(i,j+2) or current and dp(i+1, j)
                else:
                    ans = current and dp(i+1,j+1)
                memo[(i,j)] = ans
            return memo[(i,j)]
        return dp(0,0)