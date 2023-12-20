# import
import math

# 問題にある関数の実装
def f(N):
    return (math.ceil(math.sqrt(N)))**2 - ( math.floor(math.sqrt(N)))**2
        
# Answer
ans = 1
# calcurate result
num = 0
# Limit
N = 10**5

# calcuration
while True:
    num += f(ans)
    if num >= N:
        break
    ans += 1
    
# output
print("ans is:",ans)