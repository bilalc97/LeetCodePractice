def two_sum(nums, target):
    """
    Return indices of the two numbers such that they add up to a specific target.

    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    needed_for_ind = {}
    for i in range(len(nums)):
        if nums[i] in needed_for_ind:
            return [i, needed_for_ind[nums[i]]]
        else:
            needed_for_ind[target - nums[i]] = i
    return []

if __name__ == "__main__":
    print(two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(two_sum([7, 32, 8, 1, 7], 14))
    print(two_sum([5, 6, 8, 9, 19, 3], 20))
