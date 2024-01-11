ans = 0

for a in range(1,61):
    for b in range(1,61):
        for c in range(1,61):
            if (a<=b) and (b>=c):
                ans += 1

# output
print(ans)
