class Solution(object):
    def myAtoi(self, str):

        # O(N) runtime and O(1) space
        no_space=str.lstrip()

        Int_Min=-(2**31)
        Int_Max=2**31-1
        l=len(no_space)
        
        if not no_space:
            return 0
        if no_space[0] != '+' and no_space[0] != '-' and no_space[0].isnumeric() is False:
            return 0
        
        ans = no_space[0]
        for i in range(1,l):
            if no_space[i].isnumeric() is True:
                ans += no_space[i]
            else:
                break
                
        ans = ans.replace("+","")
        
        if ans:
            
            if ans == "-":
                return 0
            elif int(ans)>Int_Max:
                return Int_Max
            elif int(ans)<Int_Min:
                return Int_Min
            
        else:
            return 0
        return int(ans)