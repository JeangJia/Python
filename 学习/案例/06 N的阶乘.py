def factorial(n):
    """
    求 N 的阶乘
    Args:
        n: 待求数

    Returns: N 的阶乘

    """
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
print(factorial(50))