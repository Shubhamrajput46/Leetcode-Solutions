class Solution(object):
    def isAphanumeric(self,s):
        x=ord(s)
        if (97 <= x <= 122) or (65 <= x <= 90) or (48 <= x <= 57):
            return True
        return False

    def isPalindrome(self, s):
        s = s.lower()

        i=0
        j=len(s)-1

        while i<j:
            if not self.isAphanumeric(s[i]):
                i +=1
                continue

            if not self.isAphanumeric(s[j]):
                j-=1
                continue
                
            if s[i]==s[j]:
                i +=1
                j -=1
            
            else:
                return False
        return True
