# 정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.
# 단, arr에 2가 없는 경우 [-1]을 return 합니다.
# 제한사항)  1 ≤ arr의 길이 ≤ 100,000 , 1 ≤ arr의 원소 ≤ 10

def solution(arr):
    if 2 in arr:
        for i in range(len(arr)):
            if arr[i] == 2:
                start = i
                break 
        for i in range(len(arr)-1, -1, -1):  
            if arr[i] == 2:
                end = i
                break
        return arr[start:end+1]
    else:
        return [-1]
    
def solution2(arr):
    answer = []
    for i, num in enumerate(arr):
        if num == 2:
            answer.append(i)
    if not answer:
        return [-1]
    else:
        start_idx = min(answer)
        end_idx = max(answer)
        return arr[start_idx:end_idx+1]

print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))
print("----------------------------------")
print(solution2([1, 2, 1, 4, 5, 2, 9]))
print(solution2([1, 2, 1]))
print(solution2([1, 1, 1]))
print(solution2([1, 2, 1, 2, 1, 10, 2, 1]))