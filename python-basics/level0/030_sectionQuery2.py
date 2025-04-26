# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.
# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.
# 각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
# 단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.
# 제한사항
# 1 ≤ arr의 길이 ≤ 1,000
# 0 ≤ arr의 원소 ≤ 1,000,000
# 1 ≤ queries의 길이 ≤ 1,000
# 0 ≤ s ≤ e < arr의 길이
# 0 ≤ k ≤ 1,000,000

def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query[0], query[1], query[2]
    # for s, e, k in queries: 좀 더 파이썬스러운 방법
        sub_arr = arr[s : e+1]
        answercandidates = []
        for x in sub_arr:
            if x > k:
                answercandidates.append(x)
        if answercandidates:
            answer.append(min(answercandidates))
        else:
            answer.append(-1)
    return answer

def solution2(arr,queries):
    answer = []
    for query in queries:
        s, e, k = query[0], query[1], query[2]
        answercandidates = []
        for i in range(s, e+1):
            if arr[i] > k:
                answercandidates.append(arr[i])
        if answercandidates:
            answer.append(min(answercandidates))
        else:
            answer.append(-1)
    return answer

print(solution([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]]))
print(solution2([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]]))
            