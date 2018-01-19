# 打印菱形
def print_diamond(n):
    for i in range(1,n+1):
        print ' '*(n-i), '*'*(2*i-1)
    for i in range(n-1,0,-1):
        print ' '*(n-i), '*'*(2*i-1)


# 替换空格
def replaceSpace(s):
    temp = ''
    if type(s) != str:
        return
    for i in s:
        if i == ' ':
            temp += '%20'
        else:
            temp += i
    return temp
