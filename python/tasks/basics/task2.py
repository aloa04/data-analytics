'''
Write a program capable of displaying all odd numbers from a starting and ending number.
'''

def task2():
  print(*range(1,20,2))
  for i in range(1,20):
    if i%2!=0:
        print(i)
    print(*[n for n in range(1,20) if n % 2 != 0])