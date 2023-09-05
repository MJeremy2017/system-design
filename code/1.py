"""
Q:You are given an integer array prices where prices[i] is the price of a given stock on the ith day. We need to find the longest possible subarray in prices which will have it’s first price greater than it’s last price.

Example 1:
Input: prices = [10, 20, 30, 40, 50, 1, 20, 9, 60]
Output = [10, 20, 30, 40, 50, 1, 20, 9]
Explanation: [10, 20, 30, 40, 50, 1, 20, 9] is the longest possible subarray of prices with the 1st element being greater than the last element.

Example 2:
Input: prices = [10, 20, 30, 15]
Output: [20, 30, 15]
Explanation: [20, 30, 15] is the longest possible subarray of prices with the 1st element being greater than the last element.

Example 3:
Input prices = [80, 100, 60, 50, 50, 70, 100, 110, 50, 70, 110, 80, 100]
Output: [100, 60, 50, 50, 70, 100, 110, 50, 70, 110, 80]
Explanation: [100, 60, 50, 50, 70, 100, 110, 50, 70, 110, 80] is the longest possible subarray of prices with the 1st element being greater than the last element.

"""


def solve(arr):
    l, r = 1, len(arr)
    n = len(arr)

    def _valid(v):
        nonlocal n
        for i in range(n - v + 1):
            if arr[i] - arr[i + v - 1] > 0:
                return True, i, i + v - 1
        return False, 0, 0

    largest_len = 0
    ans = []
    while l <= r:
        mid = (l + r) // 2
        can, i, j = _valid(mid)
        if can:
            if mid > largest_len:
                ans = arr[i:j + 1]
                largest_len = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans


if __name__ == '__main__':
    test_cases = [
        ([10, 20, 30, 40, 50, 1, 20, 9, 60], [10, 20, 30, 40, 50, 1, 20, 9]),
        ([10, 20, 30, 15], [20, 30, 15]),
        ([80, 100, 60, 50, 50, 70, 100, 110, 50, 70, 110, 80, 100], [100, 60, 50, 50, 70, 100, 110, 50, 70, 110, 80])
    ]

    for arr, want in test_cases:
        got = solve(arr)
        print(got, want)
        assert got == want
        print("================================")
