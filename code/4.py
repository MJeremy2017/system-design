"""
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""


def solve(A):
    n = len(A)
    A = [(x, i) for i, x in enumerate(A)]
    ans = [0] * n

    def _merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        la = _merge_sort(arr[0:mid])
        ra = _merge_sort(arr[mid:])
        l, r = 0, 0
        ma = []
        cnt = 0
        while l < len(la) and r < len(ra):
            if ra[r][0] < la[l][0]:
                cnt += 1
                ma.append(ra[r])
                r += 1
            else:
                ma.append(la[l])
                ans[la[l][1]] += cnt
                l += 1
        while l < len(la):
            ma.append(la[l])
            ans[la[l][1]] += cnt
            l += 1

        while r < len(ra):
            ma.append(ra[r])
            r += 1
        return ma

    _merge_sort(A)
    return ans


if __name__ == '__main__':
    test_cases = [
        ([5, 2, 6, 1], [2, 1, 1, 0]),
        ([2, 0, 1], [2, 0, 0]),
        ([-1, -1], [0, 0])
    ]
    for x, want in test_cases:
        got = solve(x)
        print('got', got)
        assert got == want
