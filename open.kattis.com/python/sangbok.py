max, n = input().split()
song_ticks = [int(word) for word in input().split()]
song_ticks.sort()
max, n = int(max) * 60, int(n)

cnt = 0
for i in range(len(song_ticks)):
    if cnt + song_ticks[i] >= max: break
    cnt += song_ticks[i]

print(cnt)