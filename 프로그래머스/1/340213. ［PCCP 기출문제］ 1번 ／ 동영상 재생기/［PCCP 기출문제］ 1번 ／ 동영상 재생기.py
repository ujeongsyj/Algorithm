def changeToMin(str):
    hour = int(str[0:2])
    min = int(str[3:5])
    time = hour * 60 + min
    return time

def changeToString(min):
    hour = min//60
    min = min%60
    if hour<10:
        s_hour = '0'+str(hour)
    else:
        s_hour = str(hour)
    if min<10:
        s_min = '0'+str(min)
    else:
        s_min = str(min)
    answer = s_hour + ':' + s_min
    return answer

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    i_video_len = changeToMin(video_len)
    i_pos = changeToMin(pos)
    i_op_start = changeToMin(op_start)
    i_op_end = changeToMin(op_end)
    for c in commands:
        if i_op_start <= i_pos <= i_op_end:
            i_pos = i_op_end
        if c == "prev":
            if i_pos < 10:
                i_pos = 0
            else:
                i_pos -= 10
        elif c == "next":
            if i_pos+10 > i_video_len:
                i_pos = i_video_len
            else:
                i_pos += 10 
        if i_op_start <= i_pos <= i_op_end:
            i_pos = i_op_end
        
    answer = changeToString(i_pos)
    return answer