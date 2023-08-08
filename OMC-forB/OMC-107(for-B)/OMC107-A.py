ans = 0
# 1000-9999まで走査
for i in range(1000,10000):
    if str(i)[0]!=str(i)[1] and str(i)[1]!=str(i)[2] and str(i)[2]!=str(i)[3]:
        ans += 1
print(ans)