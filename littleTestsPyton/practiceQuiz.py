# for n in range(6,18+1,3):
#     print(n*2)

# for count in range(1, 6):
#     print(count+1)

for outer_loop in range(2, 6+1):
    for inner_loop in range(outer_loop):
        if inner_loop % 2 == 0:
            print(inner_loop)