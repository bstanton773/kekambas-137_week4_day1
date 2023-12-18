# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2


def solution(nums):
    current_max = 0
    current_count = 0
    for num in nums:
        if num == 1:
            current_count += 1
        else:
            if current_count > current_max:
                current_max = current_count
            current_count = 0
    if current_count > current_max:
        current_max = current_count
    return current_max

def solution(nums):
    # print(nums)
    # str_nums = ''.join([str(num) for num in nums])
    # print(str_nums)
    # ones = str_nums.split('0')
    # print(ones)
    # consec_counts = [len(one) for one in ones]
    # print(consec_counts)
    # return max(consec_counts)
    return max([len(consec) for consec in ''.join([str(num) for num in nums]).split('0')])


print(solution([1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]))