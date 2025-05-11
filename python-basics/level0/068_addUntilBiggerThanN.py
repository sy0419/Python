# 정수 배열 numbers와 정수 n이 매개변수로 주어집니다. 
# numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.
# 제한사항
# 1 ≤ numbers의 길이 ≤ 100
# 1 ≤ numbers의 원소 ≤ 100
# 0 ≤ n < numbers의 모든 원소의 합

def solution(numbers, n):
    sumOfNum = 0
    for num in numbers:
        sumOfNum += num
        if sumOfNum > n:
            break
    return sumOfNum

print(solution([34, 5, 71, 29, 100, 34], 123))
print(solution([58, 44, 27, 10, 100], 139))