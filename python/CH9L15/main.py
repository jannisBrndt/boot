def find_max(nums):
    max_so_far = float("-inf")
    for i in range(0, len(nums)):
        if nums[i] > max_so_far:
            max_so_far = nums[i]
    return max_so_far

def main():
    list = [1, 2, 3, 4, 5]
    find_max(list)

main()
