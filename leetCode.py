nums = list(map(int, input().split()))
hasil = []
i = 0
for num in nums:
    i += num
    hasil.append(i)
print(hasil)