def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    end = h2*60*60 + m2*60 + s2
    start = h1*60*60 + m1*60 + s1
    
    # 먼저 시침은 초당 360도/12*60*60 만큼 움직임 1/120도
    # 분침은 360도/60*60 => 0.1도
    # 초침은 360 / 60 => 6도

    if start == 0 or start == 12 * 3600:
        answer += 1
    
    for tm in range(start + 1, end + 1):
        bh = ((tm - 1) / 120) % 360
        bm = ((tm - 1) / 10) % 360
        bs = ((tm - 1) * 6) % 360

        h = (tm / 120) % 360
        m = (tm / 10) % 360
        s = (tm * 6) % 360
        
        if s == 0:
            s = 360
        
        if bh > bs and h <= s:
            answer += 1

        if bm > bs and m <= s:
            answer += 1

        if h%360 == m%360 == s%360:
            answer -= 1
        # print(bh, bm ,bs, ", ", h, m, s, ", ", answer)
        
        
        
    return answer