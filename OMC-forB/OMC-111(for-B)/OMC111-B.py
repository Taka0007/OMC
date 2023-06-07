def num_sum(K: int) -> int:
    ans = 0
    while K > 0:
        ans += K % 10
        K //= 10
    return ans

ans = 0

# 1-51まで検証
for i in range(1, 51):
    if num_sum(i ** 2) == num_sum((i + 1) ** 2):
        ans += i

print(ans)
