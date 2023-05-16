# 리스트의 중복 항목 검사 알고리즘

def unique_elements(A):  # 리스트 A 입력
    n = len(A)  # 입력의 크기 = 리스트의 크기
    for i in range(n - 1):  # i : 0, 1, ... n-2
        for j in range(i + 1, n):  # j : i+1, i+2, ... n-1
            if A[i] == A[j]:  # 기본 연산
                return False  # 같은 항목이 있으면 False 반환
    return True  # 같은 항목이 없으면 True 반환


# Sample Code

A = [32, 14, 5, 17, 23, 9, 11, 14, 26, 29]
B = [13, 6, 8, 7, 12, 25]
C = [22, 16, 14, 12, 7, 13, 27, 17]

print(A, unique_elements(A))
print(B, unique_elements(B))
print(C, unique_elements(C))
