from collections import deque

def solve(isConnected):
    vis = set()
    n=len(isConnected)
    count=0
    for i in range(n):
        if i in vis:
            continue
        count+=1
        vis.add(i)
        q=deque([i])
        while q:
            el=q.pop()
            for adji in range(n):
                if isConnected[el][adji] and adji not in vis:
                    vis.add(adji)
                    q.appendleft(adji)
    return count
