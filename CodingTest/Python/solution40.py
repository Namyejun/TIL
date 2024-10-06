def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    vm, vs = video_len.split(":")
    pm, ps = pos.split(":")
    sm, ss = op_start.split(":")
    em, es = op_end.split(":")
    
    vt = int(vm)*60 + int(vs)
    pt = int(pm)*60 + int(ps)
    st = int(sm)*60 + int(ss)
    et = int(em)*60 + int(es)
    
    commands = [""] + commands
    
    for command in commands:
        if command == "prev":
            pt -= 10
            if pt < 0:
                pt = 0
        elif command == "next":
            pt += 10
            if pt > vt:
                pt = vt
        else:
            pass
        if pt >= st and pt <= et:
            pt = et
    
    answer = str(pt//60).zfill(2)+":"+str(pt%60).zfill(2)
    
    return answer