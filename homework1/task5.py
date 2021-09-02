from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Given a list of integers numbers "nums".
    You need to find a sub-array with length less equal to "k", with maximal sum.
    The written function should return the sum of this sub-array.
    Examples:
        nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
        result = 16
    """
    mx = max(nums)
    for length in range(2, k + 1):
        s = sum(nums[:length])
        for i in range(len(nums) - length):
            s = s - nums[i] + nums[i + length]
            if s > mx:
                mx = s
    return mx
