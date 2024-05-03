from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            complement = target - nums[i]
            try:
                if nums[i] == complement:
                    nums[i] = None
                    complement_idx = nums.index(complement)
                else:
                    complement_idx = nums.index(complement)
                return [i, complement_idx]
            except ValueError:
                nums[i] = num
                pass
        return False


tests = [
    (
        ([2, 7, 11, 15], 9),
        [0, 1],
    ),
    (
        ([3, 2, 4], 6),
        [1, 2],
    ),
    (
        ([3, 3], 6),
        [0, 1],
    ),
]
