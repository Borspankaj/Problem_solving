class Solution:
    def plusOne(self, digits):
        r=len(digits)-1
        temp=1
        for i in range(r,-1,-1):
            if digits[i]==9:
                if temp==1:
                    digits.append(0)
                    digits.pop(i)
                    if i==0:
                        digits.insert(0,1)
            else:
                digits[i]+=temp
                temp=0
            
        return digits
