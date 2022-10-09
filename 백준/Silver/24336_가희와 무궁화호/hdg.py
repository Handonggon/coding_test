info = {'Seoul': 0, 'Yeongdeungpo': 9.1, 'Anyang': 23.9, 'Suwon': 41.5, 'Osan': 56.5, 'Seojeongri': 66.5, 'Pyeongtaek': 75
      , 'Seonghwan': 84.4, 'Cheonan': 96.6, 'Sojeongni': 107.4, 'Jeonui': 114.9, 'Jochiwon': 129.3, 'Bugang': 139.8, 'Sintanjin': 151.9
      , 'Daejeon': 166.3, 'Okcheon': 182.5, 'Iwon': 190.8, 'Jitan': 196.4, 'Simcheon': 200.8, 'Gakgye': 204.6, 'Yeongdong': 211.6, 'Hwanggan': 226.2
      , 'Chupungnyeong': 234.7, 'Gimcheon': 253.8, 'Gumi': 276.7, 'Sagok': 281.3, 'Yangmok': 289.5, 'Waegwan': 296, 'Sindong': 305.9, 'Daegu': 323.1
      , 'Dongdaegu': 326.3, 'Gyeongsan': 338.6, 'Namseonghyeon': 353.1, 'Cheongdo': 361.8, 'Sangdong': 372.2, 'Miryang': 381.6, 'Samnangjin': 394.1
      , 'Wondong': 403.2, 'Mulgeum': 412.4, 'Hwamyeong': 421.8, 'Gupo': 425.2, 'Sasang': 430.3, 'Busan': 441.7}

[N, Q] = list(map(int, input().split()))

def timeToHour(time):
    if time == '-:-':
        return 0;
    [hour, minute] = list(map(int, time.split(':')))
    return (hour * 60) + minute

schedule = {}
for _ in range(N):
    [station, arrival, departure] = input().split()
    schedule[station] = [timeToHour(arrival), timeToHour(departure)]

sections = [input().split() for _ in range(Q)]

for [start, end] in sections:
    distance = abs(info[end] - info[start])
    duration = ((1440 + schedule[end][0] - schedule[start][1]) % 1440) / 60

    print(distance / duration)