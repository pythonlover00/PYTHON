nums = (2, 5, 6, 9, 7, 3)
odd = 0
even = 0
for num in nums:
    if not num % 2:
        even+=1
    else:
        odd+=1
print("Num of even nums :",even)
print("Num of odd nums :",odd)