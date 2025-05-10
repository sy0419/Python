# 정수 배열 arr가 주어집니다. 이때 arr의 원소는 1 또는 0입니다. 
# 정수 idx가 주어졌을 때, idx보다 크거나 같은 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요.
# 단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.
# 제한사항
# 3 ≤ arr의 길이 ≤ 100'000
# arr의 원소는 전부 1 또는 0입니다.

def solution(arr, idx):
    answer = -1
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            answer = i
            break
    return answer

print(solution([0, 0, 0, 1], 1))
print(solution([1, 0, 0, 1, 0, 0], 4))
print(solution([1, 1, 1, 1, 0], 3))