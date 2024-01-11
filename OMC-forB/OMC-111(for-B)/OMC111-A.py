ans = 0

for i in range(1,10**5):
    if len(set(str(i)))==1:
        ans += 1
        
# output
print(ans)