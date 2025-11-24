def reverse_num(n):
    return int(str(n)[::-1])

num = int(input("Enter a Number: "))

rev_num = reverse_num(num)
rev_sq = rev_num ** 2

sq = num ** 2
rev_sq_of_num = reverse_num(sq)

if rev_sq == rev_sq_of_num:
    print(num, "is an Adam Number")

else:
    print(num, "is NOT an Adam Number")