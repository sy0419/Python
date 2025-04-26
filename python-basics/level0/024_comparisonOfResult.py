# 정수가 담긴 리스트 num_list가 주어질 때, 
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.
# 제한사항) 2 ≤ num_list의 길이 ≤ 10 , 1 ≤ num_list의 원소 ≤ 9

def solution(num_list):
    all_multi = 1
    all_sum = 0
    for char in num_list:
        all_multi *= char
        all_sum += char
    if (all_sum**2) > all_multi:
        return 1
    else:
        return 0 

print(solution([3, 4, 5, 2, 1])) # all_multi = 120 , all_sum**2 = 225
print(solution([5, 7, 8, 3])) # all_multi = 840 , all_sum**2 = 529