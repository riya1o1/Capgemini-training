s1 = input("Enter the first value : ").strip()
s2 = input("Enter the second value : ").strip()
if len(s1) > len(s2):
    s1, s2 = s2, s1
max_len = 0
max_sum = 0
for i in range(len(s1)):
    for j in range(i + 1, len(s1) + 1):
        sub = s1[i:j]
        if sub in s2:
            length = len(sub)
            ascii_sum = sum(ord(c) for c in sub)
            if length > max_len or (length == max_len and ascii_sum > max_sum):
                max_len = length
                max_sum = ascii_sum0
print(max_sum)