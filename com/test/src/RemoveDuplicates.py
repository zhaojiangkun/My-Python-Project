'''
删除有序数组中的重复项
'''
import util.InputUtils


def remove_duplicates(nums):
    left = 0
    right = 1
    while right < len(nums):
        if nums[right] != nums[left]:
            nums[left + 1] = nums[right]
            left += 1
        right += 1
    return left + 1


if __name__ == '__main__':
    InputUtils = util.InputUtils.InputUtils()
    nums = InputUtils.input_to_int_list()
    print(remove_duplicates(nums))
    print(nums)
