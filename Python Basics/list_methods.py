basket = [1, 2, 3, 4, 5, 6, 7]

basket.append(100)
print(basket)  # [1, 2, 3, 4, 5, 6, 7, 100]

basket.insert(0, 200)
print(basket)  # [200, 1, 2, 3, 4, 5, 6, 7, 100]

basket.insert(9, 300)
print(basket)  # [200, 1, 2, 3, 4, 5, 6, 7, 100, 300]

basket.extend([500, 600, 700])
print(basket)  # [200, 1, 2, 3, 4, 5, 6, 7, 100, 300, 500, 600, 700]

print(basket.pop()) # 700
print(basket)  # [200, 1, 2, 3, 4, 5, 6, 7, 100, 300, 500, 600]

basket.pop(8)
print(basket)  # [200, 1, 2, 3, 4, 5, 6, 7, 300, 500, 600]

basket.append(300)
basket.remove(300)  # removed only the first occurrence of value = 300
print(basket)  # [200, 1, 2, 3, 4, 5, 6, 7, 500, 600, 300]

basket.clear()
print(basket)  # []
