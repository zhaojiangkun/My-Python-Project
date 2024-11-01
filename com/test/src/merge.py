import util.InputUtils as input_util


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    i = m
    j = 0
    while i < len(nums1):
        nums1[i] = nums2[j]
        i += 1
        j += 1

    return sorted(nums1)


if __name__ == '__main__':
    nums1 = input_util.input_to_int_list()
    nums2 = input_util.input_to_int_list()
    m, n = input_util.input_to_more_int()
    print(merge(nums1, m, nums2, n))
