import sys
from collections import deque


# 뱀 객체를 생성할 클래스
class Snake:

    __pos = [(0, 0)]
    __dc = [0, 1, 0, -1]
    __dr = [1, 0, -1, 0]

    def __init__(self, size):
        self.size = size
        self.length = 1
        self.direction = 0

    # 뱀의 다음 위치와 안전 여부를 확인하는 함수
    def next_pos(self):
        # 머리의 현재 위치를 확인
        c_head_now, r_head_now = self.__pos[0]

        # 진행 방향에 따른 다음 위치를 확인
        c_head_new, r_head_new = c_head_now + self.__dc[self.direction], r_head_now + self.__dr[self.direction]

        # 다음 진행 방향에 몸이 있는 경우 : return False
        if (c_head_new, r_head_new) in self.__pos:
            return False

        # 다음 진행 방향이 벽일 경우 : return False
        elif not (0 <= c_head_new < self.size and 0 <= r_head_new < self.size):
            return False

        # 아닐 경우 다음 머리 위치를 반환
        else:
            return (c_head_new, r_head_new)

    # 뱀이 단순히 이동할 떄의 함수
    def move(self, c, r):
        self.__pos = [(c, r)] + self.__pos[:-1]

    # 뱀이 사과를 먹을 때의 함수
    def eat(self, c, r):
        self.__pos = [(c, r)] + self.__pos
        self.length += 1

    # 뱀이 방향을 바꿀 때의 함수
    def rotate(self, d):
        if d == 'L':
            self.direction = (self.direction - 1) % 4
        else:
            self.direction = (self.direction + 1) % 4

    # 뱀의 위치를 print 하는 함수
    def print_snake(self):
        temp_field = [[0] * self.size for _ in range(self.size)]

        for temp_c, temp_r in self.__pos:
            temp_field[temp_c][temp_r] = 1

        for x in range(self.size):
            print(temp_field[x])


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

# field
field = [[0 for _ in range(N)] for _ in range(N)]

# 사과 놓기 (value : 1)
for _ in range(K):
    c, r = map(int, sys.stdin.readline().split())
    field[c - 1][r - 1] = 1

L = int(sys.stdin.readline())

# 뱀의 움직임 정보 (시간, 방향)
movement = deque()
for _ in range(L):
    t, d = sys.stdin.readline().split()
    movement.append((int(t), d))

# 풀이 시작
# 뱀 객체 생성
snake = Snake(N)

# 결과값을 저장할 변수 time
time = 0

# 회전 여부를 확인하는 변수 trigger / 회전 내역을 저장하는 next_rotate
trigger = True
next_rotate = (-1, "N")

# 게임 시작
while True:
    # 시간 1 추가
    time += 1

    # 가장 빠른 회전 내역 확인
    if trigger and len(movement):
        next_rotate = movement.popleft()
        trigger = False

    # 뱀의 다음 움직임 확인
    next_pos = snake.next_pos()

    # 만일 게임이 끝난다면
    if not next_pos:
        break

    # 만일 다음 위치에 사과가 있다면 성장
    elif field[next_pos[0]][next_pos[1]]:
        field[next_pos[0]][next_pos[1]] = 0
        snake.eat(next_pos[0], next_pos[1])

    # 사과가 없다면 단순 이동
    else:
        snake.move(next_pos[0], next_pos[1])

    # 만일 회전해야 할 시점이라면
    if time == next_rotate[0]:
        trigger = True
        snake.rotate(next_rotate[1])

print(time)