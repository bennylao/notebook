def targetSum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums) - 3):
        if i and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j != i + 1 and nums[j] == nums[j - 1]:
                continue
            sum = target - nums[i] - nums[j]
            left, right = j + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == sum:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > sum:
                    right -= 1
                else:
                    left += 1
    return result


print(targetSum([3, 0, -1, 0, -2, 5], 2))
