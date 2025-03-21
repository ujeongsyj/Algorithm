def solution(citations):
    #[6,5,3,1,0]
    answer = 0
    citations.sort(reverse=True)
    N = len(citations)
    h_index = citations[0]
    while (h_index>=0):
        l,s = 0,0
        for i in range(N):
            if citations[i] >= h_index:
                l += 1
            else:
                s += 1
        if l>=h_index and s<=h_index:
            break
        
        h_index -= 1
            
    return h_index