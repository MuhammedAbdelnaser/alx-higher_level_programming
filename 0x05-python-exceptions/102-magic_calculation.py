#!/usr/bin/python3


def magic_calculation(j, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > j:
                raise Exception('Too far')
            else:
                result += j ** b / i
        except:
            result = b + j
            break
    return (result)
