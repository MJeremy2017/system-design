"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
"""
from collections import defaultdict
import bisect as bs


def solve(s: str, words: list) -> list:
    ans_words = []
    ms = defaultdict(list)
    for i, ch in enumerate(s):
        ms[ch].append(i)

    for word in words:
        v = -1
        can = True
        for ch in word:
            if ch not in ms:
                can = False
                break
            pos = bs.bisect(ms[ch], v)
            if pos >= len(ms[ch]):
                can = False
                break
            v = ms[ch][pos]
        if can: ans_words.append(word)
    return ans_words


if __name__ == '__main__':
    test_cases = [
        ("abcde", ["a", "bb", "acd", "ace"], 3),
    ]
    for s, words, want in test_cases:
        got = solve(s, words)
        print('got', got)
        assert len(got) == want
