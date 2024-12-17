# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x
# и возвращающую самое маленькое целое число y, такое что:
# y больше или равно x
# y делится нацело на 5

def closest_mod_5(x):
    # y = 5
    # if x < y:
    #     return y
    # elif x % 5 == 0:
    #     return x
    # else:
    #     return x + (5 - x % 5)

    return x + (5 - x % 5) % 5

number = int(input())

print(closest_mod_5(number))

