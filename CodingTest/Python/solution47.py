def solution(play_time, adv_time, logs):
    total_time = calc_tot(play_time)
    adv_tot_time = calc_tot(adv_time)
    
    lst = []
    # 30만
    for log in logs:
        s, e = log.split("-")
        lst.append([calc_tot(s), 1])
        lst.append([calc_tot(e), -1])
    
    # 464,758,001 정도라는데...?
    # n ^(3/2) 라는 가정하에 저렇게 뜨는 거지
    lst.sort()
    
    cumulative_sum = []
    cur_val = 0
    # 사실상 얘는 360000 정도고
    for i, j in lst:
        cum_len = len(cumulative_sum)
        for _ in range(cum_len + 1, i + 1):
            if len(cumulative_sum) == 0:
                cumulative_sum.append(0 + cur_val)
            else:
                cumulative_sum.append(cumulative_sum[-1] + cur_val)
        cur_val += j
    
    # 얘도 사실상 30만 정도
    for i in range(len(cumulative_sum) + 1, total_time + 1):
        cumulative_sum.append(cumulative_sum[-1] + cur_val)
        
    if play_time == adv_time:
        return "00:00:00"
        
    max_val = 0
    max_idx = 0
    for i in range(total_time - adv_tot_time + 1):
        if i == 0:
            if max_val < cumulative_sum[i + adv_tot_time - 1]:
                max_val = cumulative_sum[i + adv_tot_time - 1]
                max_idx = i
        else:
            if max_val < cumulative_sum[i + adv_tot_time - 1] - cumulative_sum[i - 1]:
                max_val = cumulative_sum[i + adv_tot_time - 1] - cumulative_sum[i - 1]
                max_idx = i

    return calc_time(max_idx)
    
def calc_tot(time):
    h, m, s = map(int, time.split(":"))
    return 3600 * h + 60 * m + s
    
def calc_time(second):
    h = second // 3600
    second = second % 3600
    m = second // 60
    s = second % 60
    return str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)

# 개인적으로 얘는 간단한 테스트케이스를 만들어서 생각하는게 쉬운듯
# ex) play_time = 8초 adv_time = 3초 정도 되는 그런 테케
    