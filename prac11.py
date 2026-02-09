n = int(input("Enter the no.of voters : "))
A = list(map(int, input("Enter the values : ").split()))
freq = {}
for v in A:
    freq[v] = freq.get(v, 0) + 1
for party, votes in freq.items():
    if votes >= n / 2:
        print(party)
        break
else:
    print(-1)