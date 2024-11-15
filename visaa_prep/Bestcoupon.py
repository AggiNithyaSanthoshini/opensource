X = int(input())
discount_1 = X * 0.90
discount_2 = X - 100
final_Bill = min(discount_1, discount_2)
print(int(final_Bill))
