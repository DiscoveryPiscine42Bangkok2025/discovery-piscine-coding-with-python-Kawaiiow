original_array = [1, 2, 3]
gt_5 = list(filter(lambda x: x > 5, original_array))
plus_two = list(map(lambda x: x + 2, gt_5))

print(f'{original_array}')
print(f'{plus_two}')