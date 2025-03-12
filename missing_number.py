"""
Problem Explanation:

You are given an array that contains n-1 distinct numbers. These numbers are chosen from the range 1 to n, where 
n is the total number of elements you expect. Since there is one missing number, the array contains every number 
from the range except one.

For example, if n = 6, the complete set of numbers would be: [1, 2, 3, 4, 5, 6]
If the array contains the numbers: [1, 2, 3, 5, 6]
Then the missing number is 4.

"""

num = int(input("Enter the no. of elements: "))
arr = []

for i in range(num-1):
    ele = int(input(f"Enter the {i+1}th no.: "))
    arr.append(ele)

for i in range(num-1):
    if arr[i] != i+1:
        missingNo = i+1
        break
    else:
        missingNo = num

print("Missing no.:", missingNo)
