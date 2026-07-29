from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # slow: vị trí cuối cùng của vùng các phần tử duy nhất
        slow = 0

        # fast duyệt tìm phần tử mới; vì mảng đã sắp xếp nên
        # phần tử trùng luôn nằm cạnh nhau.
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 1, 2]
    k1 = sol.removeDuplicates(nums1)
    print(k1, nums1[:k1])  # 2 [1, 2]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    print(k2, nums2[:k2])  # 5 [0, 1, 2, 3, 4]
