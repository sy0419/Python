# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.
# 각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
# 제한사항
# 1 ≤ arr의 길이 ≤ 1,000
# 0 ≤ arr의 원소 ≤ 1,000,000
# 1 ≤ queries의 길이 ≤ 1,000
# 0 ≤ i < j < arr의 길이

def solution(arr, queries):
    for query in queries:  
        i = query[0]  
        j = query[1]  
        arr[i], arr[j] = arr[j], arr[i] 
    # for i, j in queries:
        # arr[i], arr[j] = arr[j], arr[i] 
    # Both are same meaning and different way to indicate.
    # 'for query in queries:' 에서 query는 queries에서 리스트에서 하나씩 가리키니까 
    # 첫번째 실행에서 queries[0] = [3,0]을 가리키고, 
    # 거기서 i = query[0]을 하면 3, j = query[1]을 하면 0이 되는 것
    # 첫 번째 for문은 풀어서 표현한 것이고 두 번째는 함축해서 사용한 것.  
    return arr

print(solution([0, 1, 2, 3, 4], [[0, 3],[1, 2],[1, 4]]))