nums = [3,7,5,9]
nums.append(7)
nums.append(2)
nums.pop()
count = len(nums)
print(count)
print(nums)
num = 31
i = 2
while i < num:
    if num % i == 0:
        print("i am not done")
    break