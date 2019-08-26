# To store a multiple values for key in dictionary
# For nested dictionary use link - https://www.quora.com/In-the-Python-dictionary-can-1-key-hold-more-than-1-value
from statistics import mean
from functools import *
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores 
# print(student_marks)
query_name = input()
list1 = student_marks[query_name]
print("%.2f"%mean(list1))

# https://www.geeksforgeeks.org/find-average-list-python/
list1 = [15, 9, 55, 41, 35, 20, 62, 49]
print(reduce(lambda a, b: a + b, list1)/len(list1))