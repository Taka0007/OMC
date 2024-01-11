ans = 0

for x in range(1,505):
    for y in range(1,673):
        if 4*x + 3*y == 2022:
            ans += 1

# output  
print(ans)