from random import randint

nums=[]
for i in range (5):
    n=randint(0,10)
    nums.append(n)
print(nums)
for num in nums:
    avg = sum / len(nums)
    print(avg)