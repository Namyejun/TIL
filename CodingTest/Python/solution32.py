# 그거 안됨 출차 안한차 계산에 넣어야함
def solution(fees, records):
    answer = []
    table = {}
    time = {}
    for record in records:
        tm, num, val = record.split(" ")
        if num not in table and val == "IN":
            table[num] = tm
            if num not in time:
                time[num] = 0
        elif table[num] and val == "OUT":
            in_tm = table[num]
            del table[num]
            time[num] = time[num] + calc_tm(in_tm, tm)
    tm_lst = sorted(time.items())
    print(tm_lst)
    for num, t in tm_lst:
        answer.append(calc_fee(t, fees[0], fees[1], fees[2], fees[3]))
    return answer

def calc_tm(in_tm, out_tm):
    ih, im = map(int, in_tm.split(":"))
    oh, om = map(int, out_tm.split(":"))
    
    return (oh*60 + om) - (ih*60 + im)

def calc_fee(tm, default_tm, default_fee, unit_tm, unit_fee):
    if default_tm < tm:
        return default_fee + ((tm - default_tm)//unit_tm + 1) * unit_fee
    else:
        return default_fee