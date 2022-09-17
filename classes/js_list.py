from types import FunctionType


class js_list:
    def __init__(self, custom_list: list) -> None:
        self.is_js_list = True
        self.custom_list = custom_list

    def for_each(self, callback: FunctionType):
        index = 0
        for element in self.custom_list:
            callback(element, index)
            index += 1

    def map(self, callback):
        index = 0
        result = []
        for element in self.custom_list:
            result.append(callback(element))
            index += 1
        return result

    def reduce(self, callback, initial):
        result = initial
        for element in self.custom_list:
            result = callback(result, element)
        return result


numbers = js_list(range(11))


def to_square(num):
    return num * num


def exp_two(num):
    return 2 ** num


scaleNums = numbers.map(to_square)
expNums = numbers.map(exp_two)

print("numbers: ", expNums)
