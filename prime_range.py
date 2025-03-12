"""
Write a Python program that takes two numbers, start and end, and prints all prime numbers in that range.

Example:
  For start = 10, end = 30:
  11, 13, 17, 19, 23, 29
"""


startNo = int(input("Enter the starting no.: "))
endNo = int(input("Enter the ending no.: "))

for i in range(startNo, endNo):
    flag = 1
    for j in range(2, i-1):
        if i%j == 0:
            flag = 0
    if flag == 1:
        print(i)
