'''
无重复字符的最长子串
'''
def lengthOfLongestSubstring(str):
    map = {}
    l = -1
    res = 0
    length = len(str)
    for j in range(length):
        if str[j] in map:
            l = max(map[str[j]], l)
        map[str[j]] = j
        res = max(res, j - l)
    return res


def name2List(name):
    arr = [ord(c) for c in name]
    return arr
def make_tensors(names):
    return [name2List(name) for name in names]
if __name__ == '__main__':
    # str = input()
    # res = lengthOfLongestSubstring(str)
    # print(res)
    # print(name2List("hello"))
    names = ["hello", "leetcode"]
    print(ord('h'))
    print(make_tensors(names))



