class Solution:
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        best = ""
        minLen = float('inf')
        left = 0
        count = 0
        
        for right in range(n):
            if s[right] == '1':
                count += 1
            
            # Shrink window while we have too many 1's
            while count > k:
                if s[left] == '1':
                    count -= 1
                left += 1
            
            if count == k:
                # Trim leading zeros to tighten the window
                while s[left] == '0':
                    left += 1
                
                length = right - left + 1
                candidate = s[left:right+1]
                
                if length < minLen:
                    minLen = length
                    best = candidate
                elif length == minLen and candidate < best:
                    best = candidate
        
        return best