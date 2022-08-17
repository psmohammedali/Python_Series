def summaryRanges(nums):
    my_list = []
    i = 0
    while i < len(nums):
        first = i
        if first == len(nums) - 1:
            my_list.append(str(nums[len(nums) - 1]))
            return my_list
        str_formed = ""
        second = i + 1
        while second < len(nums):
            if nums[second] == nums[first] + 1:
                first = second
                second = first + 1
                continue
            else:
                if i == first:
                    str_formed = str(nums[i])
                else:
                    str_formed = str(nums[i]) + "->" + str(nums[first])
                my_list.append(str_formed)
                i = second
                break
        else:
            if i == first:
                str_formed = str(nums[i])
            else:
                str_formed = str(nums[i]) + "->" + str(nums[first])
            my_list.append(str_formed)
            break

    return my_list


n = [0,1,3,5,6]
ans = summaryRanges(n)
print(ans)