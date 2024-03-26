# Priblem link : https://onlinemathcontest.com/contests/omc183/tasks/4292
# declare val
ans = 0
for num in range(10,100):
    if num % 9 == 8 and num % 6 == 5:
        ans = num
# output
print(ans)