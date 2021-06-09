# 7. Implement a recursive algorithm to find the n-th Fibonacci number using memoization.
# TASK 7

memoization101 = [1, 1, 2, 3, 5, 8]


def fibonacci(n, prev=0, curr=1):
    if prev == 0 and curr == 1:
        if n <= len(memoization101):
            return memoization101[n - 1]
        elif n > len(memoization101):
            return fibonacci(
                n - len(memoization101), memoization101[-2], memoization101[-1]
            )
    elif n != 0:
        memoization101.append(prev + curr)
        return fibonacci(n - 1, curr, memoization101[-1])
    else:
        return curr


print(fibonacci(11))
print(memoization101)
