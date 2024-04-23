a, b, list_ = map(int, input().split()), list(map(int, input().split()))
print(*[i for i in list(map(int, input().split())) if i < b], end=' ')