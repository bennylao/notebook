import itertools


def target_sum(nums, target):
    success_combinations = []
    nums.sort()
    for combination in itertools.combinations(nums, 4):
        if sum(combination) == target and list(combination) not in success_combinations:
            success_combinations.append(list(combination))
    print(success_combinations)


def target_sum_2(nums, target):
    success_combinations = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                for a in range(len(nums)):
                    if len({i, j, k, a}) == 4 and (nums[i] + nums[j] + nums[k] + nums[a]) == target:
                        combination = [nums[i], nums[j], nums[k], nums[a]]
                        combination.sort()
                        if combination not in success_combinations:
                            success_combinations.append(combination)
    print(success_combinations)


if __name__ == "__main__":
    target_list = [3, 0, -1, 0, -2, 5]
    target_num = 2
    target_sum(target_list, target_num)
    # target_sum_2(target_list, target_num)
