ans = 0

# iは1～100
for i in range(1,101):
    ans += i//5
    ans += i//25
print(ans)