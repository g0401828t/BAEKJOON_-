import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for n in range(N):
    board.append(list(map(str, sys.stdin.readline().strip())))

# 8ㅌ8로 자른 보드를 확인
def Check(data):
    start = ["W", "B"]
    result = float("inf")
    # 처음 시작을 "W"일때와 "B"일때 뭐가 더 적게 칠해도 되는지 확인
    for i in range(2):
        count = 0
        now = start[i]
        for y in range(8):
            for x in range(8):
                if data[y][x] != now:
                    count += 1

                #  8x8 라서 다음 줄로 넘어갈때는 현재 끝나는 칸의 색과 같은 색이 칠해져야한다
                if x != 7:
                    if now == "W":
                        now = "B"
                    else:
                        now = "W"
        if count < result:
            result = count
    return result

# 8x8로 잘라서 확인
result = float("inf")
for n in range(N-7):
    for m in range(M-7):
        data = [row[m:m+8] for row in board[n:n+8]]
        count = Check(data)
        if count < result:
            result = count

print(result)
