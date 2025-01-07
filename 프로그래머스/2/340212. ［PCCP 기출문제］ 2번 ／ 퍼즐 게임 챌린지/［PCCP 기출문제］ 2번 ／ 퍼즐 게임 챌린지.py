def solution(diffs, times, limit):
    start, end = 1, max(diffs)
    while(start<=end):
        t = times[0]
        mid = (start+end)//2
        for i in range(1,len(diffs)):
            if diffs[i] <= mid:
                t += times[i]
            else:
                t += (times[i] + times[i-1]) * (diffs[i]-mid) + times[i]
        if t > limit:
            start = mid+1
        else:
            end = mid-1
        
    return start