N = int(input())

schedule = []
for _ in range(N):
    council = list(map(int, input().split()))
    schedule.append(council)

schedule.sort(key = lambda x: x[0]) #시작 시간 기준 정렬
schedule.sort(key = lambda x: x[1]) #종료 시간 기준 정렬 => 종료 시간이 같다면 시작 시간이 빠른 순으로!

cnt = 1 #첫 list를 카운트
end = schedule[0][1]
for i in range(1, N):
    if schedule[i][0] >= end: #새로운 방이 뒤에 이어진다면 => 정렬을 위에서 해서 가능한 방법
        cnt += 1
        end = schedule[i][1]

print(cnt)


