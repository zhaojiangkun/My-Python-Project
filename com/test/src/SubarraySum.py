class SubarraySum(object):

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, -1, -1):
                sum += nums[j]
                if sum == k:
                    res += 1
        return res


if __name__ == '__main__':
    method = SubarraySum()
    nums = [1, 1, 2]
    k = 3
    print(method.subarraySum(nums, k))
