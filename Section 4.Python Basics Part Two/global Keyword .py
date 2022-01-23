total = 0


def count(total):
    total += 1
    return total


print(count(count(count(total))))  # count is 3
print(count(count(count(1))))  # count is 4
