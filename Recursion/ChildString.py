def ChildString(pos: int, end: int, s: str, result: str):
    if pos >= end:
        print(result)
    else:
        ChildString(pos + 1, end, s, result + s[pos])
        ChildString(pos + 1, end, s, result)
s = '132'
ChildString(0, len(s), s, '')
