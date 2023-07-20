n, k = map(int, input().split())
# 퀘스트 경험치, 낮은 것부터 정렬
quest = list(map(int, input().split()))
quest.sort()
#총 경험치와 활성된 돌멩이
akane = 0
routine = -1
# 다활성되면 k개만, 그전에는 활성된 것만 경험치 추가
for i in quest:
    routine += 1
    if routine < k:
        akane += i*routine
    elif routine >= k:
        akane += i*k
    else:
        continue

print(akane)