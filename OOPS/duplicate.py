def removeDuplicates(nums) -> int:
    i = 1
    count = 0
    while i < len(nums):
        if nums[i] == None:
            break
        if nums[i] != nums[i - 1]:
            i = i + 1
            count += 1
        else:
            j = i

            while j < len(nums):
                nums[j - 1] = nums[j]
                if j == len(nums) - 1:
                    nums[j] = None
                j = j + 1
    return count


ans = removeDuplicates([1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5])
print(ans)
