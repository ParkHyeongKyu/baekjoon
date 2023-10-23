# 문제
# 알파벳 대문자 A~Z는 다음 mapping을 통해 인코드(encode) 가 가능하다
# 'A'-> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# 인코드(encode) 된 문자를 디코드(decode) 하려면 숫자들을 위 mapping의 reverse를 이용해 디코드(decode)하면 된다.
# ex) "11106"
# (1 1 10 6) → "AAJF"
# (11 10 6) → "KJF"
# (1 11 06) → invalid 왜냐하면 06은 'F'로 매핑될 수 없기 때문이다. '6'과 '06'은 다르다.
# 주어진 문자 s가 오직 숫자만 포함할 때, 이 숫자를 디코드(decode) 할 수 있는 모든 방법의 수를 return 하라


def numDecodings(s):
    if s[0] == "0":
        return 0

    dp = [0 for x in range(len(s) + 1)]
    dp[0] = 1
    dp[1] = 0 if s[0] == "0" else 1

    for i in range(2, len(s) + 1):
        if 0 < int(s[i - 1:i]) <= 9:
            dp[i] += dp[i - 1]
    if 10 <= int(s[i - 2:i]) <= 26:
        dp[i] += dp[i - 2]

    return dp[len(s)]
