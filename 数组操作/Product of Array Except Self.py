class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = len(nums)
        pro = [1 for _ in range(l)]  #构造一个与l大小一样的数组存储乘积
        left = 1
        for i in range(l):
            pro[i] *= left
            left *= nums[i]
        right = 1
        for j in range(l-1, -1 ,-1):
            pro[j] *= right
            right *= nums[j]
        return pro

if __name__ == '__main__':
    nums = [-1,1,0,-3,3]
    S = Solution()
    print(S.productExceptSelf(nums))