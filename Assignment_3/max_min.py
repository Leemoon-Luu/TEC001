nums = []

def max_min(nums):

    while True:
        a = input("Enter your number: ")
        if a == "":
            break
        nums.append(int(a))
    max = nums[0]
    min = nums[0]

    for i in nums:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min

max, min = max_min(nums)
print("Maximum:", max)
print("Minimum:", min)
    