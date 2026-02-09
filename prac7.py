S = input("Enter the lowercase letters : ").strip()
freq = {}
for ch in S:
    freq[ch] = freq.get(ch, 0) + 1
max_freq = max(freq.values())
steps = len(S) - max_freq
print(steps)
