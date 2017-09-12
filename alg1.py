#   Author: Jason
#   实现功能：将任意一组字符串中的最长字母序列打印出来
#   实现思路：使用动态规划，先取一个局部最好的，然后依次遍历，并update longest_order
#   函数的时间复杂度为O(N)

s = 'twczytvaux'
def printLongestOrder(s):
    smallest = 0
    longest_order = ''
    for i in range(len(s)):
        if i != (len(s)-1) and s[i+1] < s[i]:
            longest = i+1
            if len(longest_order) < (longest-smallest):
                longest_order = s[smallest:longest]
            smallest = longest
    if len(s) - smallest > len(longest_order):
        longest_order = s[smallest:]
    print(longest_order)
printLongestOrder(s)
