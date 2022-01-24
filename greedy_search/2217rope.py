#핵심은 equal하게 무게를 가져간다
#시간 초과 해결 방법? => temp = cand[:k] 이런거는 좋은 방법이 아님
#for 문 안의 조건문 보다는 for문 전체 돌린 후 최댓값 찾기!


N = int(input())

rope = []
for _ in range(N):
    rope.append(int(input()))
rope.sort(reverse = True)

cand = []
for k in range(0, N):
    cand.append(rope[k] * (k+1)) #k+1 활용 인지

        
print(max(cand))
    