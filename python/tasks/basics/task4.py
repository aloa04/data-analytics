'''
Write a program that is able to display the elements of a list in reverse order to the original.
'''

def task4():
  nums = [1,2,3,4,5,6,7,8,9,10]
  nums2 = list(reversed(nums))
  print(*nums2)