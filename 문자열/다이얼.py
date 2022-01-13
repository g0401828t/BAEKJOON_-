import sys

data = sys.stdin.readline()


# 디이얼 만들기
dic = {}
count = 0
index = 2
for d in range(26):
    if index == 9 or index == 7:
        if count < 4:
            dic[chr(d + 65)] = index
        else:
            index += 1
            dic[chr(d + 65)] = index
            count = 0
    else:
        if count < 3:
            dic[chr(d + 65)] = index
        else:
            index += 1
            dic[chr(d + 65)] = index
            count = 0
    count += 1


result = 0
for i in range(len(data) - 1):  # 마지막 개행 없애주기 위해 -1
    d = data[i]
    result += dic[d] + 1        # 2번 -> 3초, 3번 -> 4초... 순으로 시간이 걸린다. 따라서 각각 +1씩 해준다

print(result)
