def next_letter(s):
    res = ""
    prev_char = ""
    for i in range(len(s)):
        curr_char = s[i]
        if curr_char == prev_char:
            res += chr(ord(curr_char) + 1)
        else:
            res += curr_char
        prev_char = curr_char
    return res

# Example usage
s = "This is sarath"
result = next_letter(s)
print(result)  # Output: helmp
