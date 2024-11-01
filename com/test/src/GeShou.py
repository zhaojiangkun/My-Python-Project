'''
一个歌手准备从A城去B城参加演出
1、按照合同，他必须在T天内赶到
2、歌手途径N座城市
3、歌手不能往回走
4、每两座城市之间需要的天数都可以提前获知
5、歌手在每座城市都可以在路边卖场赚钱
经过调研，歌手提前获知了每座城市卖场的收入预期，如果在一座城市第一天卖场可以赚M，
后续每天的收入会减少D（第二天赚的钱是M-D，第三天是M-2D。。。）如果收入减少到0就不会再减少了
6、歌手到达后的第二天才能开始卖唱，如果今天唱过，则第二天才能出发

思路：
先计算穿过N座城市的所有时间，然后得到可以唱歌的时间 t = t - times_total
用列表记录每个城市每天可以赚的钱，比如：[120, 100, 80, 60, 40, 20, 0, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
然后对该列表从大小大进行排序，取前t个的和就是总共可以赚取的最大收入了
'''


def solution():
    input_1 = input().split(" ")
    t = int(input_1[0])
    n = int(input_1[1])
    input_2 = input().split(" ")
    times = []
    # 耗费的总时间
    times_total = 0
    for i_2 in input_2:
        times.append(int(i_2))
        times_total += int(i_2)
    # 剩余时间(可以唱歌的时间)
    t = t - times_total
    # 利润
    profit = []
    # print(times)
    for i in range(n):
        input_1 = input().split(" ")
        m = int(input_1[0])
        d = int(input_1[1])
        while m >= 0:
            profit.append(m)
            # 每隔一天，利润就减d
            m = m - d
    # 将利润从大到小排序
    print(profit)
    profit.sort(reverse=True)
    t = max(0, t)
    print(sum(profit[0: t]))


if __name__ == '__main__':
    solution()
