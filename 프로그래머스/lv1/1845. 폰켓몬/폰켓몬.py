def solution(nums):
    nums_set = set(nums)

    N = len(nums) // 2 # 가져가도 되는 폰켓몬

    result = min(len(nums_set), N)
    return result