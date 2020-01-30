def lcs(s1, s2, i, j):
    if i == -1 or j == -1:
        return 0
    elif s1[i] == s2[j]:
        return lcs(s1, s2, i - 1, j - 1) + 1
    else:
        return max(lcs(s1, s2, i - 1, j), lcs(s1, s2, i, j - 1))


def lcs_dp(s1, s2):
    s1 = [0] + [i for i in s1]
    s2 = [0] + [j for j in s2]
    l1 = len(s1)
    l2 = len(s2)

    lcs = [[0 for j in range(l2)] for i in range(l1)]
    for i in range(1, l1):
        for j in range(1, l2):
            if s1[i] == s2[j]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            elif lcs[i - 1][j] >= lcs[i][j - 1]:
                lcs[i][j] = lcs[i - 1][j]
            else:
                lcs[i][j] = lcs[i][j - 1]

    print(lcs[l1 - 1][l2 - 1])
