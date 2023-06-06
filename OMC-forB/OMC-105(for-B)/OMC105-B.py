import math

ans = 1

def f(N):
    return N - (int(math.sqrt(N)))**2


while abs(f(ans)-100)>0.1:
    ans += 1
        
print('解答:',ans)
print('その時のf(n):',f(ans))