from_number = int(input('enter from number: '))
to_number = int(input('enter to number: '))
is_even = True if input('even or odd ?') == 'even' else False
print(is_even)
current_number = from_number
summ = 0
while current_number <= to_number:
    if is_even and current_number % 2 == 0:
      summ += current_number
    elif not is_even and current_number % 2 != 0:
      summ += current_number
    current_number += 1

print(f'Sum even numbers from 1 to {to_number}: {summ}')