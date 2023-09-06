import math


def binaryToDecimal(binary: str) -> int:
    binary = binary.split(' ')
    binary.reverse()

    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** i)

    return decimal

def decimalToBinary(number: int) -> str:
    # The following two lines are only to show the left zeros
    totalSteps = math.ceil(0 if number == 0 else math.log2(number))

    binary = ''

    while number > 0:
        binary = str(number % 2) + ' ' + binary
        number = number // 2

    binary = ( '0 ' * (8 - totalSteps) ) + binary

    return binary

binary1 = "1 1 1 1 1 1 1 1"
print(f"{binary1} -> {binaryToDecimal(binary1)}")

binary2 = "0 0 0 0 1 0 1 0"
print(f"{binary2} -> {binaryToDecimal(binary2)}")

binary3 = "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"
print(f"{binary3} -> {binaryToDecimal(binary3)}")

decimal1 = 201
print(f"{decimal1} -> {decimalToBinary(decimal1)}")

decimal2 = 11
print(f"{decimal2} -> {decimalToBinary(decimal2)}")
