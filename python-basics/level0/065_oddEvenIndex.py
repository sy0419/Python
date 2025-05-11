# 정수 리스트 num_list가 주어집니다. 가장 첫 번째 원소를 1번 원소라고 할 때, 
# 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요. 
# 두 값이 같을 경우 그 값을 return합니다.
# 제한사항) 5 ≤ num_list의 길이 ≤ 50 , -9 ≤ num_list의 원소 ≤ 9

def solution(num_list):
    oddSum = 0
    evenSum = 0
    for i, num in enumerate(num_list):
        if i % 2 == 1:
            oddSum += num
        else:
            evenSum += num
    if oddSum > evenSum:
        return oddSum
    else:
        return evenSum

def solution2(num_list):
    odd_sum = sum(num_list[0::2])   
    even_sum = sum(num_list[1::2]) 
    return max(odd_sum, even_sum)   
    
print(solution([4, 2, 6, 1, 7, 6]))
print(solution([-1, 2, 5, 6, 3]))
print("----------------------------")
print(solution2([4, 2, 6, 1, 7, 6]))
print(solution2([-1, 2, 5, 6, 3]))