N = int(input())
lst = []
for _ in range(N):
    A, B = map(int, input().split())
    lst.append([A,B])

# lambda x: () tuple형식으로 주면 앞에서부터 정렬하고 앞 값이 같으면 뒤에꺼로 정렬
lst.sort(key = lambda x: (x[0], x[1]))
for i in range(N):
    print(lst[i][0], lst[i][1])