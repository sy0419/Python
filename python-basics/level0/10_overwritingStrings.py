def solution(my_string, overwrite_string, s):
    prefix = my_string[:s] # This slices the original string from the beginning up to index s (but not including s).
                           # my_string의 앞부분 중에서, 인덱스 s 전까지 잘라서 prefix에 저장한다.
    surffix = my_string[s+len(overwrite_string):] # It slices the rest of the original string starting from s + length of overwrite_string
                                                  # overwrite_string만큼 덮어쓴 후, 남은 뒷부분을 잘라서 suffix에 저장한다.
    return prefix + overwrite_string + surffix

my_string = input("my_string: ")
overwrite_string = input("overwrite_string: ")
s = int(input("start number: "))

result = solution(my_string, overwrite_string, s)
print("result_string:", result)