def decimalToBinary(num):
    if 0 <= num <= 15:
        binary_string = format(num, '04b')
        print(binary_string)
    else:
        print("Enter a number between 0 and 15.")

decimalToBinary(14)
decimalToBinary(9)
decimalToBinary(0)
decimalToBinary(15)

def binaryToDecimal(binary_string):
    try:
        decimal_value = int(binary_string, 2)
        return decimal_value
    except ValueError:
        print("Enter a valid binary number.")

print(binaryToDecimal('1110'))
print(binaryToDecimal('1001'))
print(binaryToDecimal('0000'))
print(binaryToDecimal('1111'))
