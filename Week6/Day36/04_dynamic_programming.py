"""
Day 36 - Dynamic Programming Basics
====================================
Learn: Fundamentals of DP - Memoization and Tabulation

Key Concepts:
- What is Dynamic Programming?
- Overlapping Subproblems
- Optimal Substructure
- Memoization (Top-Down)
- Tabulation (Bottom-Up)
- Common DP patterns
"""

# ========== INTRODUCTION ==========
print("=" * 60)
print("DYNAMIC PROGRAMMING BASICS")
print("=" * 60)

print("""
Dynamic Programming (DP) is an optimization technique that solves
complex problems by breaking them into simpler overlapping subproblems.

Two key properties for DP:
1. Overlapping Subproblems: Same subproblems are solved multiple times
2. Optimal Substructure: Optimal solution contains optimal sub-solutions

Two approaches:
1. Memoization (Top-Down): Recursion + caching
2. Tabulation (Bottom-Up): Iterative + building table
""")


# ========== FIBONACCI - CLASSIC DP EXAMPLE ==========
print("=" * 60)
print("FIBONACCI - COMPARING APPROACHES")
print("=" * 60)


# Naive Recursion - O(2^n) - Very slow!
def fib_naive(n):
    """Naive recursive - exponential time complexity"""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# Memoization (Top-Down) - O(n)
def fib_memo(n, memo=None):
    """Memoization - store results of subproblems"""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# Tabulation (Bottom-Up) - O(n)
def fib_tab(n):
    """Tabulation - build solution iteratively"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


# Space Optimized - O(1) space
def fib_optimized(n):
    """Space optimized - only keep last two values"""
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


n = 10
print(f"\nFibonacci({n}):")
print(f"  Memoization: {fib_memo(n)}")
print(f"  Tabulation: {fib_tab(n)}")
print(f"  Optimized: {fib_optimized(n)}")

# Show call comparison
import time

n = 35
start = time.time()
result_naive = fib_naive(n)
naive_time = time.time() - start

start = time.time()
result_memo = fib_memo(n, {})
memo_time = time.time() - start

print(f"\nFibonacci({n}) Performance:")
print(f"  Naive:       {result_naive} ({naive_time:.4f}s)")
print(f"  Memoization: {result_memo} ({memo_time:.6f}s)")


# ========== CLIMBING STAIRS ==========
print("\n" + "=" * 60)
print("CLIMBING STAIRS (LC 70)")
print("=" * 60)

print("""
Problem: You can climb 1 or 2 steps at a time.
How many distinct ways to climb n stairs?

This is essentially Fibonacci!
ways(n) = ways(n-1) + ways(n-2)
""")


def climb_stairs(n):
    """Number of ways to climb n stairs"""
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2
    
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


for n in range(1, 8):
    print(f"Stairs={n}, Ways={climb_stairs(n)}")


# ========== HOUSE ROBBER ==========
print("\n" + "=" * 60)
print("HOUSE ROBBER (LC 198)")
print("=" * 60)

print("""
Problem: Rob houses along a street, but can't rob adjacent houses.
Maximize the amount robbed.

DP relation:
rob(i) = max(rob(i-1), rob(i-2) + nums[i])
Either skip this house, or rob it + best from 2 houses back
""")


def house_robber(nums):
    """Maximum amount that can be robbed"""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # prev2 = max robbed excluding previous house
    # prev1 = max robbed including previous house
    prev2, prev1 = 0, 0
    
    for num in nums:
        current = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = current
    
    return prev1


houses = [2, 7, 9, 3, 1]
print(f"\nHouse values: {houses}")
print(f"Maximum robbery: {house_robber(houses)}")

houses = [1, 2, 3, 1]
print(f"\nHouse values: {houses}")
print(f"Maximum robbery: {house_robber(houses)}")


# ========== MAXIMUM SUBARRAY (KADANE'S ALGORITHM) ==========
print("\n" + "=" * 60)
print("MAXIMUM SUBARRAY - KADANE'S ALGORITHM (LC 53)")
print("=" * 60)

print("""
Problem: Find contiguous subarray with largest sum.

DP relation:
current_max = max(num, current_max + num)
Either start fresh from num, or extend previous subarray
""")


def max_subarray(nums):
    """Maximum sum of contiguous subarray"""
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def max_subarray_with_indices(nums):
    """Return max sum and the subarray"""
    max_sum = current_sum = nums[0]
    start = end = temp_start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum = current_sum + nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, nums[start:end+1]


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"\nArray: {nums}")
max_val, subarray = max_subarray_with_indices(nums)
print(f"Maximum subarray sum: {max_val}")
print(f"Subarray: {subarray}")


# ========== COIN CHANGE ==========
print("\n" + "=" * 60)
print("COIN CHANGE (LC 322)")
print("=" * 60)

print("""
Problem: Find minimum number of coins to make up amount.
Unlimited supply of each coin denomination.

DP relation:
dp[amount] = min(dp[amount - coin] + 1) for each coin
""")


def coin_change(coins, amount):
    """Minimum coins needed to make amount"""
    # dp[i] = minimum coins to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


coins = [1, 2, 5]
amount = 11
print(f"\nCoins: {coins}, Amount: {amount}")
print(f"Minimum coins needed: {coin_change(coins, amount)}")

coins = [2]
amount = 3
print(f"\nCoins: {coins}, Amount: {amount}")
print(f"Minimum coins needed: {coin_change(coins, amount)}")


# ========== 0/1 KNAPSACK ==========
print("\n" + "=" * 60)
print("0/1 KNAPSACK PROBLEM")
print("=" * 60)

print("""
Problem: Given weights and values of items, find maximum value
that fits in knapsack of capacity W. Each item can be used once.

DP relation:
dp[i][w] = max(dp[i-1][w], values[i] + dp[i-1][w - weights[i]])
Either don't take item i, or take it and add its value
""")


def knapsack(weights, values, capacity):
    """Maximum value that fits in knapsack"""
    n = len(weights)
    
    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i-1][w]
            
            # Take item i if it fits
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], 
                              values[i-1] + dp[i-1][w - weights[i-1]])
    
    return dp[n][capacity]


def knapsack_optimized(weights, values, capacity):
    """Space optimized - O(W) instead of O(n*W)"""
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Traverse right to left to avoid using same item twice
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[capacity]


weights = [1, 2, 3, 4]
values = [10, 20, 30, 40]
capacity = 5

print(f"\nWeights: {weights}")
print(f"Values:  {values}")
print(f"Capacity: {capacity}")
print(f"Maximum value: {knapsack(weights, values, capacity)}")
print(f"Maximum value (optimized): {knapsack_optimized(weights, values, capacity)}")


# ========== LONGEST COMMON SUBSEQUENCE ==========
print("\n" + "=" * 60)
print("LONGEST COMMON SUBSEQUENCE (LC 1143)")
print("=" * 60)

print("""
Problem: Find length of longest subsequence common to both strings.

DP relation:
if s1[i] == s2[j]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
""")


def longest_common_subsequence(text1, text2):
    """Find LCS length"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


text1 = "abcde"
text2 = "ace"
print(f"\nText1: '{text1}', Text2: '{text2}'")
print(f"LCS length: {longest_common_subsequence(text1, text2)}")

text1 = "AGGTAB"
text2 = "GXTXAYB"
print(f"\nText1: '{text1}', Text2: '{text2}'")
print(f"LCS length: {longest_common_subsequence(text1, text2)}")


# ========== DP PATTERNS SUMMARY ==========
print("\n" + "=" * 60)
print("COMMON DP PATTERNS")
print("=" * 60)

print("""
1. FIBONACCI-LIKE (Linear)
   - Climbing Stairs, House Robber
   - dp[i] depends on dp[i-1], dp[i-2]
   - Can often optimize to O(1) space

2. 0/1 KNAPSACK
   - Subset Sum, Partition Equal Subset Sum
   - Each item used at most once
   - dp[i][w] = max(take, don't take)

3. UNBOUNDED KNAPSACK
   - Coin Change, Rod Cutting
   - Unlimited use of each item
   - Traverse capacity left to right

4. LONGEST COMMON SUBSEQUENCE (LCS)
   - Edit Distance, Longest Common Substring
   - Compare two strings character by character
   - 2D DP table

5. LONGEST INCREASING SUBSEQUENCE (LIS)
   - Max Increasing Subsequence Sum
   - dp[i] = max(dp[j] + 1) where arr[j] < arr[i]

6. MATRIX PATH
   - Unique Paths, Minimum Path Sum
   - dp[i][j] depends on dp[i-1][j] and dp[i][j-1]

7. INTERVAL DP
   - Palindrome Partitioning, Matrix Chain Multiplication
   - Consider all subintervals
""")


# ========== STEPS TO SOLVE DP PROBLEMS ==========
print("=" * 60)
print("HOW TO APPROACH DP PROBLEMS")
print("=" * 60)

print("""
1. IDENTIFY if it's a DP problem
   - Counting ways?
   - Optimization (min/max)?
   - Can break into subproblems?
   - Same subproblems repeated?

2. DEFINE the state
   - What do you need to track?
   - What does dp[i] or dp[i][j] represent?

3. FORMULATE the recurrence relation
   - How does current state depend on previous?
   - What are the choices at each step?

4. IDENTIFY base cases
   - What are the trivial solutions?
   - dp[0], dp[1], or dp[0][0]?

5. IMPLEMENT
   - Top-down (memoization) or Bottom-up (tabulation)
   - Consider space optimization

6. VERIFY
   - Trace through small example
   - Check edge cases
""")


# ========== PRACTICE PROBLEMS ==========
print("\n" + "=" * 60)
print("PRACTICE PROBLEMS BY PATTERN")
print("=" * 60)

print("""
FIBONACCI-LIKE:
- LC 70 - Climbing Stairs
- LC 198 - House Robber
- LC 746 - Min Cost Climbing Stairs
- LC 213 - House Robber II

0/1 KNAPSACK:
- LC 416 - Partition Equal Subset Sum
- LC 494 - Target Sum
- LC 474 - Ones and Zeroes

UNBOUNDED KNAPSACK:
- LC 322 - Coin Change
- LC 518 - Coin Change 2
- LC 279 - Perfect Squares

LCS/STRINGS:
- LC 1143 - Longest Common Subsequence
- LC 72 - Edit Distance
- LC 583 - Delete Operation for Two Strings

LIS:
- LC 300 - Longest Increasing Subsequence
- LC 673 - Number of Longest Increasing Subsequence

MATRIX PATH:
- LC 62 - Unique Paths
- LC 64 - Minimum Path Sum
- LC 120 - Triangle

KADANE'S:
- LC 53 - Maximum Subarray
- LC 152 - Maximum Product Subarray
""")


print("\n" + "=" * 60)
print("✅ Dynamic Programming Basics - Complete!")
print("=" * 60)
