class InputUtils:

    def input_to_int_list(self, split_str = " "):
        return list(map(int, input().split(split_str)))