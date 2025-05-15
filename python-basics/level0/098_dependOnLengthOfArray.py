# 정수 배열 arr과 정수 n이 매개변수로 주어집니다. arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, 
# arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요.
# 제한사항) 1 ≤ arr의 길이 ≤ 1,000 , 1 ≤ arr의 원소 ≤ 1,000 , 1 ≤ n ≤ 1,000

def solution(arr, n):
    newArr = []
    if len(arr) % 2 == 1:
        for i in range(len(arr)):
            if i % 2 == 0:
                newArr.append(arr[i] + n)
            else:
                newArr.append(arr[i])
    else:
        for i in range(len(arr)):
            if i % 2 == 1:
                newArr.append(arr[i] + n)
            else:
                newArr.append(arr[i])
    return newArr

def solution2(arr, n):
    if len(arr) % 2 == 1:
        for i in range(0, len(arr), 2):
            arr[i] += n
    else:
         for i in range(1, len(arr), 2):
            arr[i] += n
    return arr

print(solution([49, 12, 100, 276, 33], 27))
print(solution([444, 555, 666, 777], 100))
print("----------------------")
print(solution2([49, 12, 100, 276, 33], 27))
print(solution2([444, 555, 666, 777], 100))