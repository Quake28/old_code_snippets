def fabulous_digit(num, leng):
    if leng == 1:
        return num
    else:
        x = int(num / (10 ** (leng - 1))) + fabulous_digit(
            num % (10 ** (leng - 1)), leng - 1
        )
        return fabulous_digit(x, len(str(x)))


print(fabulous_digit(7254, 4))  # 9
print(fabulous_digit(144441, 6))  # 9
print(fabulous_digit(144441144441, 12))  # 9
print(fabulous_digit(192291, 6))  # 6
