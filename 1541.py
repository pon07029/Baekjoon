input_value = input()

symbols = []
numbers = []

current_number = ''

for char in input_value:
    if char.isdigit():
        current_number += char
    else:
        if current_number:
            numbers.append(int(current_number))
            current_number = ''
        symbols.append(char)

# 마지막 숫자 처리
if current_number:
    numbers.append(int(current_number))

if '-' in symbols:
    minus_index = symbols.index('-')
    numbers = numbers[:minus_index+1] + [-sum(numbers[minus_index+1:])]

print(sum(numbers))
