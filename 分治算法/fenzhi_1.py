
class Solution:
    def merge(self, nums_left: list, nums_right: list) -> list:
        arr = []
        while nums_left and nums_right:
            if nums_left[0] < nums_right[0]:
                arr.append(nums_left.pop(0))
            else:
                arr.append(nums_right.pop(0))
        
        while nums_left:
            arr.append(nums_left.pop(0))
        while nums_right:
            arr.append(nums_right.pop(0))
        
        return arr
    
    def mergeSort(self, nums: list):
        if len(nums) < 2:
            return arr
        mid = len(nums)//2
        nums_left = self.mergeSort(nums[0:mid])
        nums_right = self.mergeSort(nums[mid+1:len(nums)-1])
        return self.merge(nums_left, nums_right)
    
    def sortArr(self, nums:list) -> list:
        return self.mergeSort(nums)
    

if __name__ == '__main__':
    arr = [1, 6, 90, 3,45, 6, 8,14]
    S = Solution()
    S.sortArr(arr)
    print(arr)

        
        
            