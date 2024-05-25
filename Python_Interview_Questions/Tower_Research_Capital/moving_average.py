def moving_average(nums, window):
    ma = []

    if len(nums) < window:
        return nums

    total = sum(nums[:window])
    ma.append(total / window)

    left_pointer, right_pointer = 1, 1 + window
    while right_pointer <= len(nums):
        total = total - nums[left_pointer - 1] + nums[right_pointer - 1]
        ma.append(total/window)

        left_pointer += 1
        right_pointer += 1

    return ma

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    window = 3
    print(moving_average(nums, window))