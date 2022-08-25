def solve(s):
    my_string = ""
    space_found = False
    i = 0
    while i < len(s):
        if s[i] == " ":
            space_found = True
            my_string = my_string + " "
            i = i + 1
            continue

        if space_found or i == 0:
            capital_letter = chr(ord("A") + (ord(s[i]) - ord('a')))
            my_string = my_string + capital_letter
            space_found = False
            i = i + 1
            continue

        my_string = my_string + s[i]
        i = i + 1
    return my_string


s = 'this is ali'
ans = solve(s)
print(ans)