import sys
input = sys.stdin.readline

# n과 m을 입력받아 정수형으로 변환
n, m = map(int, input().split())

# 2차원 배열 A를 (n+1) x (n+1) 크기로 초기화 (0번 인덱스는 패딩)
A = [[0]*(n+1)]
D = [[0]*(n+1) for _ in range(n+1)]

# A 배열에 실제 데이터 입력받기 (1번 인덱스부터 사용)
for i in range(n):
    # 입력받은 행의 맨 앞에 0을 추가하여 패딩
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
        
# M개의 질의(부분 합) 처리
for _ in range(m):
    # (x1, y1)부터 (x2, y2)까지의 영역 좌표를 입력받음
    x1, y1, x2, y2 = map(int, input().split())

    # 누적 합 배열 D를 이용하여 직사각형 영역의 합 계산
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]

    print(result)