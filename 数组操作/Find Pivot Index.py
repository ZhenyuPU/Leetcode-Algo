class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        curr_sum = 0
        for i in range(len(nums)):
            if curr_sum * 2 + nums[i] == sum:
                return i
            curr_sum += nums[i]
        return -1


if __name__ == '__main__':
    nums = [2,1,-1]
    #print("Please input a list:")
    #nums = input()
    S = Solution()
    print("The pivot index is:",S.pivotIndex(nums))