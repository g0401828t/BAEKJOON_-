up = input()
down = input()

cumulated_result = 0
for i in range(len(down)):
    current_result = int(up) * int(down[len(down) - 1 - i])
    print(current_result)
    cumulated_result += int(str(current_result) + i * str(0))
print(cumulated_result)

