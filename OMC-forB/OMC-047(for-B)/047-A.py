ans = 0

for a in range(1,10):
    for b in range(a+1,10):
        for c in range(b+1,10):
            for d in range(c+1,10):
                ans += 1
                
print(ans)