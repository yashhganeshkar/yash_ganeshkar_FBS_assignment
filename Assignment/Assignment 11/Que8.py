
# Print 1 to 100 in snakes and ladder pattern.

def snakes_and_ladders_pattern(start=1, end=100, row_length=10):
    result = []
    row_count = 0
    for row_start in range(start, end + 1, row_length):
        row = list(range(row_start, min(row_start + row_length, end + 1)))
        if row_count % 2 == 1:
            row = row[::-1]
        result.append(row)
        row_count += 1
    return result

pattern = snakes_and_ladders_pattern()
for row in pattern:
    print(row)
