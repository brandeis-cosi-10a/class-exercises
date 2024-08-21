import copy


######### 1. What is printed? #########
def increment1(nums):
  new_nums = []
  for num in nums:
    new_nums.append(num + 1)
  return new_nums


print("\nPuzzle 1")
nums1 = [11, 13, 5]
nums2 = increment1(nums1)
print(nums1)
print(nums2)


######### 2. What is printed? #########
def increment2(nums, new_nums):
  for num in nums:
    new_nums.append(num + 1)


print("\nPuzzle 2")
nums3 = [11, 13, 5]
nums4 = []
increment2(nums3, nums4)
print(nums3)
print(nums4)


######### 3. What is printed? #########
def increment3(nums):
  new_nums = []
  for num in nums:
    new_nums.append(num + 1)
  nums = new_nums


print("\nPuzzle 3")
nums5 = [11, 13, 5]
increment3(nums5)
print(nums5)


######### 4. What is printed? #########
def increment4(nums):
  for i in range(len(nums)):
    nums[i] = nums[i] + 1
  return nums


print("\nPuzzle 4")
nums6 = [11, 13, 5]
nums7 = increment4(nums6)
print(nums6)
print(nums7)

######### 4a. What is printed? #########
print("\nPuzzle 4a")
nums8 = [11, 13, 5]
nums9 = increment4(copy.copy(nums8))
print(nums8)
print(nums9)


######### 5. What is printed? #########
def increment5(nums):
  new_nums = copy.copy(nums)
  for i in range(len(new_nums)):
    new_nums[i] = new_nums[i] + 1
  return new_nums


print("\nPuzzle 5")
nums10 = [11, 13, 5]
nums11 = increment5(nums10)
print(nums10)
print(nums11)

# Bonus: If you run this line, it will never complete, and eventually crash.
# Why? Try it in Python Tutor to see what's going on.
# increment2(nums2, nums2)
