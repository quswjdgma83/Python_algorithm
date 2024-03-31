def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    idx = 0
    count_t = 0
    count_l = 0
    for target in range(len(s)):
        idx = target
        flag = False
        count_l = 0
        if target == 0 or target == len(s)-1:
            continue
        count = 1
        #대칭검사
        while(flag == False):
            l = idx - count
            r = idx + count
            if s[l] != s[r]:
                flag = True
                break
            else:
                count_l += 1
                count += 1
                if l == 0 or r == len(s):
                    break

        if count_l > count_t:
            count_t = count_l
    answer = 2*count + 1
    print(answer)
    return answer

longestPalindrome("babad")