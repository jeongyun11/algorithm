def solution(participants, completions):
    dic = {}

    for participant in participants:
        dic[participant] = dic.get(participant, 0) + 1
    
    for completion in completions:
        dic[completion] -= 1
        
    for d in dic:
        if dic[d] != 0: 
            return d