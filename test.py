# # odd = lambda x : bool(x % 2)
# # numbers = [n for n in range(10)]
# # for i in range(len(numbers)):
# #     if odd(numbers[i]):
# #         del numbers[i]

# # no

# # odd = lambda x : bool(x % 2)
# # numbers = [n for n in range(10)]
# # numbers[:] = [n for n in numbers if not odd(n)]
# # print(numbers)

# def createMultipliers():
#     return [lambda x : i * x for i in range(5)]

# for multiplier in createMultipliers():
#     print(multiplier(2))

