"""
one_step = {[1, 0]}
two_steps = {[2, 1, 0], [2, 0]}
three_steps = {[3, 2, 1, 0], [3, 2, 0], [3, 1, 0]}
four_steps = {[4, 3, 2, 1, 0], [4, 3, 2, 0], [4, 3, 1, 0], [4, 2, 1, 0], [4, 2, 0]}

num_ways(3) = num_ways(2) + num_ways(1)
num_ways(n) = num_ways(n-1) + num_ways(n-2)

num_ways(0) = 1
num_ways(1) = 1
"""

def num_ways(n):
    """Returns the number of ways to climb a staircase of N steps"""
    if n == 0 or n == 1:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)

def num_ways_bottom_up(n):
    """Returns the number of ways to climb a staircase of N steps"""
    if n == 0 or n == 1: return 1
    nums = [1, 1]
    for i in range(2, n+1):
        nums.append(nums[i-1] + nums[i-2])
    return nums

def fibonacci(n):
    """Returns the N first numbers in the Fibonacci sequence"""
    if n == 0 or n == 1: return 1
    ns = [1, 1]
    for i in range(2, n+1):
        ns.append(ns[i-1] + ns[i-2])
    return ns

def fibonacci_memoized(n, memo):
    """Memoized variation of the Fibonacci sequence solution"""
    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        result = 1
    else:
        result = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fibonacci_memoized(n, memo)

print(fib_memo(5))