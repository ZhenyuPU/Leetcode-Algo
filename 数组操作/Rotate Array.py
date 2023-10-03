class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        l = len(nums)
        self.reverse(nums, 0, l-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, l-1)

    def reverse(self, nums: list[int], left: int, right: int):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    

nums = [1,2,3,4,5,6,7]
k = 3
S = Solution()
S.rotate(nums, 3)
print(nums)