class Solution:
    def is_prime(self,num):
        if num <=1:
            return False
        if num==2:
            return True
        for i in range(2,num):
            if num%i==0:
                return False
        return True

    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        for i in nums:
            if self.is_prime(nums.count(i)):
                return True
        return False

        