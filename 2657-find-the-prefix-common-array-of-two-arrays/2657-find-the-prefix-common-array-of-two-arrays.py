class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c = []
        for i in  range(len(A)):

            check =  A[0:i+1]
            check2 = B[0:i+1]
            count = 0
            for i in check:
                if i in check2:
                    count +=1
            c.append(count)
        
        return c
