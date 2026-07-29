from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # vị trí tiếp theo để ghi phần tử khác val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

if __name__ == "__main__":
    solution = Solution()

    nums1 = [3,2,2,3]
    k1 = solution.removeElement(nums1, 3)
    print(k1)

    nums2 = [0,1,2,2,3,0,4,2]
    k2 = solution.removeElement(nums2, 2)
    print(k2)