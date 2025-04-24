a, b = map(int, input().strip().split(' '))
print("a =", a,"\nb =", b)
# The .strip() method removes any leading and trailing whitespace (spaces, newlines, etc.) from the string.
# 문자열 양쪽 끝의 공백 제거하는 함수.

# The .split(' ') method splits the string into a list using the specified separator, in this case, a space (' ').
# 문자열을 공백 문자(' ')를 기준으로 분리해서 리스트로 반환하는 함수

# The map() function applies the given function to each element of an iterable (like a list).
# 주어진 함수를 반복 가능한 객체에 적용하는 함수.