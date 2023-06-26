def solution(bridge_length, weight, trucks):
    time = 0
    end = []

    trucks_copy = trucks[:]

    bridge = [0] * bridge_length 
    bridge_sum = 0

    # 순회 시작

    # 대기 트럭의 무게와 다리를 건너는 트럭의 무게 합이 weight의 이하라면 
    while True:
        if trucks and ((bridge_sum - bridge[0] + trucks[0]) <= weight):
            truck_append = trucks.pop(0)
        else : 
            truck_append = 0
            
        truck_pop = bridge.pop(0)
        bridge_sum -= truck_pop
        

        bridge.append(truck_append)
        bridge_sum += truck_append

        time += 1

        if truck_pop != 0:
            end.append(truck_pop)

        if end == trucks_copy:
            break

    return time