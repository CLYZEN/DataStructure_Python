# 순환적으로 구현한 Factorial 함수

def factorial(n):
    if n == 1:  # 순환을 멈추는 부분
        return 1
    else:  # 순환 호출을 하는 부분
        return (n * factorial(n - 1))


# 반복 구조로 구현한 Factorial 함수
def factorial_iter(n):
    result = 1
    for k in range(n, 0, -1):  # n, n-1, n-2, ..., 1
        result = result * k
    return result


print("Factorial순환(3) = ", factorial(3))
print("Factorial반복(3) = ", factorial_iter(3))
